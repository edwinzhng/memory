from src.Game import Game

class CPUGame(Game):
  def __init__(self, difficulty):
    self.cpu_score = 0
    self.player_score = 0
    super().__init__()

  def reset(self) -> None:
    super().reset()
    self.cpu_score = 0
    self.player_score = 0

  def move(self, first_card: (int, int), second_card: (int, int)) -> int:
    pass
