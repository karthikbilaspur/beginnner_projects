import random

class PowerUps:
    def __init__(self):
        self.power_ups = ["extra_life", "revealed_letter"]

    def apply_power_up(self):
        power_up = random.choice(self.power_ups)
        if power_up == "extra_life":
            print("Power-up: Extra Life!")
            return 1  # Additional life
        else:
            print("Power-up: Revealed Letter!")
            return random.choice(self.word)  # Revealed letter