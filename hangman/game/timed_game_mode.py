import time
import threading

class TimedGameMode:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = 0
        self.game_over = False
        self.timer_thread = None

    def start_timer(self):
        self.start_time = time.time()
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()

    def countdown(self):
        while time.time() - self.start_time < self.time_limit and not self.game_over:
            remaining_time = int(self.time_limit - (time.time() - self.start_time))
            print(f"Time remaining: {remaining_time} seconds", end='\r')
            time.sleep(1)
        if not self.game_over:
            print("\nTime's up!")
            self.game_over = True

    def check_game_over(self):
        return self.game_over

# Example usage in hangman.py
timed_game_mode = TimedGameMode(60)  # 1 minute
timed_game_mode.start_timer()
while not timed_game_mode.check_game_over():
    # Hangman game logic here
    pass