from enum import Enum

class GameMode(Enum):
    """Game modes."""
    SINGLE_PLAYER = 1
    MULTIPLAYER = 2
    TIMED = 3
    TEAM = 4

class GameModeSettings:
    """Game mode settings."""

    def __init__(self):
        self.game_modes = {
            GameMode.SINGLE_PLAYER: {"word_list": "animals", "score_limit": 10, "guesses": 6},
            GameMode.MULTIPLAYER: {"word_list": "countries", "score_limit": 20, "guesses": 5},
            GameMode.TIMED: {"word_list": "programming", "score_limit": 30, "guesses": 4, "time_limit": 60},
            GameMode.TEAM: {"word_list": "history", "score_limit": 40, "guesses": 3, "team_size": 2}
        }

    def get_game_mode_settings(self, game_mode: GameMode) -> dict:
        """Retrieve game mode settings."""
        return self.game_modes[game_mode]

    def set_game_mode(self, game_mode: GameMode) -> GameMode:
        """Set the game mode."""
        if game_mode in self.game_modes:
            return game_mode
        else:
            raise ValueError("Invalid game mode")

    def add_custom_game_mode(self, game_mode_name: str, settings: dict) -> None:
        """Add custom game mode."""
        self.game_modes[GameMode[game_mode_name.upper()]] = settings

# Example usage
game_mode_settings = GameModeSettings()
print(game_mode_settings.get_game_mode_settings(GameMode.SINGLE_PLAYER))

# Add custom game mode
game_mode_settings.add_custom_game_mode("CUSTOM", {"word_list": "science", "score_limit": 50})