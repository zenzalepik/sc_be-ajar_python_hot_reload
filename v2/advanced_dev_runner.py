# advanced_dev_runner.py
import os
import sys
import subprocess
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import platform

class AdvancedDevRunner:
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.restart_count = 0
        self.start_time = time.time()
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    def print_header(self):
        """Print beautiful header"""
        self.clear_screen()
        print("🔄" * 50)
        print("🎯 PYTHON TKINTER DEV SERVER WITH AUTO-RELOAD")
        print("🔄" * 50)
        print(f"📁 Watching: {self.script_path}")
        print(f"🕒 Uptime: {time.strftime('%H:%M:%S')}")
        print(f"🔢 Restarts: {self.restart_count}")
        print("🔍 Monitoring all .py files in current directory")
        print("⏹️  Press Ctrl+C to stop")
        print("-" * 50)
    
    def start_app(self):
        """Start aplikasi Python"""
        if self.process:
            print(f"🔄 Restarting... (Reason: File change)")
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
        
        self.restart_count += 1
        self.print_header()
        
        try:
            self.process = subprocess.Popen(
                [sys.executable, self.script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Thread untuk capture output
            threading.Thread(target=self.capture_output, daemon=True).start()
            
        except Exception as e:
            print(f"❌ Error starting app: {e}")
    
    def capture_output(self):
        """Capture output dari aplikasi"""
        while self.process and self.process.poll() is None:
            try:
                output = self.process.stdout.readline()
                if output:
                    print(f"📱 App: {output.strip()}")
            except:
                pass
    
    def stop(self):
        """Stop aplikasi dan cleanup"""
        if self.process:
            print("\n🛑 Stopping application...")
            self.process.terminate()
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.kill()

class DevEventHandler(FileSystemEventHandler):
    def __init__(self, dev_runner):
        self.dev_runner = dev_runner
        self.last_restart = 0
        self.restart_delay = 1  # Minimal delay antara restart
    
    def should_restart(self):
        """Prevent terlalu sering restart"""
        current_time = time.time()
        if current_time - self.last_restart < self.restart_delay:
            return False
        self.last_restart = current_time
        return True
    
    def on_modified(self, event):
        if event.src_path.endswith('.py') and not event.src_path.endswith('dev_runner.py'):
            if self.should_restart():
                print(f"📄 File changed: {os.path.basename(event.src_path)}")
                self.dev_runner.start_app()
    
    def on_created(self, event):
        if event.src_path.endswith('.py'):
            print(f"🆕 New file: {os.path.basename(event.src_path)}")
            self.dev_runner.start_app()

def main():
    if len(sys.argv) < 2:
        print("Usage: python advanced_dev_runner.py your_app.py")
        print("Example: python advanced_dev_runner.py my_app.py")
        sys.exit(1)
    
    script_path = sys.argv[1]
    
    if not os.path.exists(script_path):
        print(f"❌ Error: File {script_path} tidak ditemukan!")
        sys.exit(1)
    
    # Setup dev runner
    dev_runner = AdvancedDevRunner(script_path)
    dev_runner.start_app()
    
    # Setup file watcher
    event_handler = DevEventHandler(dev_runner)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down dev server...")
        dev_runner.stop()
        observer.stop()
    
    observer.join()

if __name__ == '__main__':
    main()