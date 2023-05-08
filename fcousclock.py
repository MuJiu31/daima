import time
import tkinter as tk

SECOND = 60
MINUTE = 25 * SECOND


class Pomodoro:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("250x100")

        self.minutes = 25
        self.seconds = 0

        self.timer_label = tk.Label(self.master, text="25:00", font=("Arial", 30))
        self.timer_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

    def start_timer(self):
        self.seconds += 1  # to prevent 59:60 display issue
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        while self.minutes or self.seconds:
            if self.seconds == 0:
                self.seconds = 59
                self.minutes -= 1
            else:
                self.seconds -= 1

            self.update_timer()
            time.sleep(1)

        self.stop_timer()
        self.master.bell()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.minutes = 25
        self.seconds = 0
        self.update_timer()
        self.stop_timer()

    def update_timer(self):
        self.timer_label.config(text="{:02d}:{:02d}".format(self.minutes, self.seconds))


if __name__ == "__main__":
    root = tk.Tk()
    pomodoro = Pomodoro(root)
    root.mainloop()
