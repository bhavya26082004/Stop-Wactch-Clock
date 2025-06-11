import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch / Clock")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Clock Label
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.clock_label.pack(pady=10)

        # Stopwatch Label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
        self.stopwatch_label.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_button.pack(side="left", padx=10, pady=20)

        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        # Stopwatch variables
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Start threads
        self.update_clock()
        self.update_stopwatch()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Current Time: " + now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            current_time = time.time()
            total_time = self.elapsed_time + (current_time - self.start_time)
            mins, secs = divmod(int(total_time), 60)
            hours, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        self.root.after(200)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Run the application
root = tk.Tk()
app = StopwatchClockApp(root)
root.mainloop()
