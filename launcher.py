import os
import subprocess
import threading
import time
import webbrowser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def open_browser():
    time.sleep(5)
    webbrowser.open("http://localhost:8501")

threading.Thread(target=open_browser, daemon=True).start()

streamlit_exe = os.path.join(BASE_DIR, "venv", "Scripts", "streamlit.exe")

subprocess.Popen([
    streamlit_exe,
    "run",
    os.path.join(BASE_DIR, "app.py"),
    "--server.headless=true"
])

while True:
    time.sleep(1)