import random


class HogDiceGame:
  """A Basic Simulator of the Hog - Dice Game 

  ...

  Attributes
  ----------
  player_scores : dict
    total score for both players
  current_player : int
    the current player
  turn_total : dict
    temporary score for the turn
  winner : int/None
    winner of the game, if any

  Methods
  -------
  roll_dice(number_of_dice):
    Rolls mulitple dice and adds the score to turn_total
  hold_turn_total():
    Adds turn score to player's total score and ends player turn
  
  Rules of the game can be found here ->
  https://inst.eecs.berkeley.edu/~cs61a/fa13/proj/hog/hog.html
  """

  def roll_dice(self, number_of_dice):
    """Rolls mulitple dice (based on parameter) and adds the score to turn_total

    Parameters
    ----------
    number_of_dice : int
      Must be between 0 and 10 (inclusive)
    """

    if self.winner is not None:
      return

    if not (0 <= number_of_dice < 10):
      raise ValueError("Number of dice has to be at least 0 and no greater than 10")

    if number_of_dice == 0:
      self._free_bacon_rule()
      return

    for i in range(number_of_dice):
      value = random.randint(1, self._dice_sides)
      if value == 1:
        self._pig_out_rule()
        return
    
      self._turn_total += value
    
  def hold_turn_total(self):
    """Adds the turn score to player's total score and ends player turn."""
    self._end_turn()

  @property
  def player_scores(self):
    """Dictionary with player number refering to the player's total score."""
    return {
      1: self._p1_score,
      2: self._p2_score
    }

  @property
  def current_player(self):
    """Current player."""
    return self._current_player

  @property
  def turn_total(self):
    """Dictionary with player number refering to the player's turn score."""
    return {
      1: self._turn_total if self._current_player == 1 else 0,
      2: self._turn_total if self._current_player == 2 else 0
    }

  @property
  def winner(self):
    """Player that won (int) or None if no player has won."""
    if self._p1_score >= 100:
      return 1
    elif self._p2_score >= 100:
      return 2
    else:
      return None
  

  _p1_score = _p2_score = 0
  _current_player = 1
  _turn_total = 0
  _dice_sides = 6

  def _change_player(self):
    if self._current_player == 1:
      self._current_player = 2
    else:
      self._current_player = 1

  def _add_to_total_score(self, points):
    if self._current_player == 1:
      self._p1_score += points
    else:
      self._p2_score += points

  def _end_turn(self):
    self._add_to_total_score(self._turn_total)
    self._turn_total = 0

    self._swine_swap_rule()
    self._dice_sides = 6
    self._hog_wild_rule()

    self._change_player()
  
  def _pig_out_rule(self):
    self._turn_total = 1
    self._end_turn()

  def _free_bacon_rule(self):
    if self.current_player == 1:
      opponent = self._p2_score
    else:
      opponent = self._p1_score
    
    self._turn_total = int(max(str(opponent))) + 1
    self._end_turn()
  
  def _hog_wild_rule(self):
    if (self._p1_score+self._p2_score) % 7 == 0:
      self._dice_sides = 4

  def _swine_swap_rule(self):
    if (self._p1_score == 2*self._p2_score or 
    self._p2_score == 2*self._p1_score):
      self._p1_score, self._p2_score = self._p2_score, self._p1_score



def display_stats(obj):
  print(f"Current player: {obj.current_player}")
  print(f"Score:\n{obj.player_scores}")
  print(f"Turn total:\n{obj.turn_total}")

if __name__ == "__main__":
  game = HogDiceGame()
  display_stats(game)
  