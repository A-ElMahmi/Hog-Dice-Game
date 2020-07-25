from hog_dice_game.view import HogDiceGameView
from hog_dice_game.controller import HogDiceGameController


def main():
  view = HogDiceGameView()
  controller = HogDiceGameController(view)

  while not view.winner_found:
    view.display()
    controller.handle_input()

  view.display_winner()


if __name__ == "__main__":
  main()