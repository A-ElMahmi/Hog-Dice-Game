from .model import HogDiceGame


class HogDiceGameView:

  model = HogDiceGame()

  def display(self):
    self._display_total_scores()
    self._display_turn_info()

  def display_help(self):
    print("Help screen")
  
  def display_winner(self):
    message = "\n".join([
      "\n+-------------------------+",
      f"| Player {self.model.winner} is the winner! |",
      "+-------------------------+"
    ])
    print(message)

  @property
  def winner_found(self):
    return False if self.model.winner is None else True


  def _display_total_scores(self):
    table = "\n".join([
      "\n+----------------+",
      "| SCORE:         |",
      "+----------------+",
      "| Player 1 - {} |",
      "| Player 2 - {} |",
      "+----------------+\n\n"
    ])
    
    scores = self._format_scores(self.model.player_scores.values())
    p1_score, p2_score = scores
    print(table.format(p1_score, p2_score))

  def _display_turn_info(self):
    current_player = self.model.current_player
    info = "Player {}'s turn -- {} turn points"
    info = info.format(current_player, self.model.turn_total[current_player])
    print(info)

  def _format_scores(self, scores):
    formated_scores = []
    for score in scores:
      score = self._format_single_score(score)
      formated_scores.append(score)
    return formated_scores
  
  def _format_single_score(self, score):
    return str(score).center(3)