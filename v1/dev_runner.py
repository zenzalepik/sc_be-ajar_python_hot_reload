# dev_runner.py
import os
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PythonFileHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.start_app()
    
    def start_app(self):
        """Start aplikasi Python"""
        if self.process:
            print("🔄 Restarting application...")
            self.process.terminate()
            self.process.wait()
        
        print(f"🚀 Starting {self.script_path}...")
        self.process = subprocess.Popen([sys.executable, self.script_path])
    
    def on_modified(self, event):
        """Dijalankan ketika file di-modify"""
        if event.src_path.endswith('.py') and not event.src_path.endswith('dev_runner.py'):
            print(f"📁 File changed: {os.path.basename(event.src_path)}")
            self.start_app()
    
    def on_created(self, event):
        """Dijalankan ketika file baru dibuat"""
        if event.src_path.endswith('.py'):
            print(f"➕ New file: {os.path.basename(event.src_path)}")
            self.start_app()

def main():
    if len(sys.argv) < 2:
        print("Usage: python dev_runner.py your_app.py")
        sys.exit(1)
    
    script_path = sys.argv[1]
    
    if not os.path.exists(script_path):
        print(f"Error: File {script_path} tidak ditemukan!")
        sys.exit(1)
    
    print(f"🔍 Watching for changes in Python files...")
    print(f"📱 Running: {script_path}")
    print("⏹️  Press Ctrl+C to stop\n")
    
    event_handler = PythonFileHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping dev server...")
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
    
    observer.join()

if __name__ == '__main__':
    main()