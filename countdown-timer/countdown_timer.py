import time
import threading

class CountdownTimer:
    def __init__(self):
        self.duration = 0
        self.running = False

    def countdown(self):
        """
        Countdown timer function.

        Returns:
            None
        """
        while self.duration > 0 and self.running:
            mins, secs = divmod(self.duration, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.duration -= 1
        if self.running:
            print('Time Up!!')

    def start(self):
        """
        Start countdown.

        Returns:
            None
        """
        self.running = True
        threading.Thread(target=self.countdown).start()

    def pause(self):
        """
        Pause countdown.

        Returns:
            None
        """
        self.running = False

    def reset(self, duration):
        """
        Reset countdown.

        Args:
            duration (int): New duration in seconds.

        Returns:
            None
        """
        self.duration = duration
        self.running = False


def main():
    timer = CountdownTimer()

    while True:
        print("\nCountdown Timer Menu:")
        print("1. Set duration and start")
        print("2. Pause")
        print("3. Reset")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            duration = input("Enter duration in seconds: ")
            try:
                duration = int(duration)
                if duration <= 0:
                    print("Duration must be a positive integer.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            timer.duration = duration
            timer.start()

        elif choice == "2":
            timer.pause()
            print("Countdown paused.")

        elif choice == "3":
            duration = input("Enter new duration in seconds: ")
            try:
                duration = int(duration)
                if duration <= 0:
                    print("Duration must be a positive integer.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            timer.reset(duration)
            print("Countdown reset.")

        elif choice == "4":
            timer.pause()
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()