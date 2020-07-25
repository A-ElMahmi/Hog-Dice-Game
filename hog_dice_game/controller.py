class HogDiceGameController:

  def __init__(self, view):
    self.view = view
    self.model = view.model
  
    self.commands = {
      "roll": self.model.roll_dice,
      "hold": self.model.hold_turn_total,
      "help": self.view.display_help,
      "quit": exit
    }

  def handle_input(self):
    inp = input("> ").lower().split()

    if inp[0] == "roll":
      self.commands["roll"](int(inp[1]))

    elif inp[0] in self.commands:
      self.commands[inp[0]]()

    else:
      self._invalid_command(inp[0])

  
  def _invalid_command(self, cmd):
    print(f"{cmd}: is an invalid command")
    self.handle_input()