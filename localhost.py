import threading
import webbrowser
from pathlib import Path

from flask import Flask, render_template_string
from flask_sock import Sock
from winpty import PtyProcess

app = Flask(__name__)
sock = Sock(app)

PROJECT_DIR = Path(__file__).parent


HTML = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Terminal</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/xterm/css/xterm.css">
    <style>
        html, body, #terminal {
            width: 100%;
            height: 100%;
            margin: 0;
            background: #000;
        }
    </style>
</head>
<body>
    <div id="terminal"></div>

    <script src="https://cdn.jsdelivr.net/npm/xterm/lib/xterm.js"></script>
    <script>
        const terminal = new Terminal({
            cursorBlink: true,
            fontSize: 15,
            theme: { background: "#000000" }
        });

        terminal.open(document.getElementById("terminal"));

        const protocol = location.protocol === "https:" ? "wss" : "ws";
        const socket = new WebSocket(`${protocol}://${location.host}/ws`);

        socket.onmessage = event => {
            terminal.write(event.data);
        };

        terminal.onData(data => {
            if (socket.readyState === WebSocket.OPEN) {
                socket.send(data);
            }
        });

        socket.onclose = () => {
            terminal.write("\\r\\n\\r\\nConexão encerrada.\\r\\n");
        };

        terminal.focus();
    </script>
</body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(HTML)


@sock.route("/ws")
def terminal(websocket):
    command = 'cmd.exe /k ".venv\\Scripts\\activate.bat"'
    process = PtyProcess.spawn(command, cwd=str(PROJECT_DIR))

    def send_output():
        try:
            while process.isalive():
                output = process.read(4096)
                if output:
                    websocket.send(output)
        except Exception:
            pass

    output_thread = threading.Thread(target=send_output, daemon=True)
    output_thread.start()

    try:
        while process.isalive():
            data = websocket.receive()
            if data is None:
                break
            process.write(data)
    finally:
        if process.isalive():
            process.terminate()


def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(host="127.0.0.1", port=8000, debug=False)