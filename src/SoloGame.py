from src.Game import Game

class SoloGame(Game):
  def __init__(self):
    self.score = 0
    self.highscore = 0
    super().__init__()

  def reset(self) -> None:
    super().reset()
    self.score = 0

  def move(self, first_card: (int, int), second_card: (int, int)) -> int:
    pass
