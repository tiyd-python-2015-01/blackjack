from game import Game
from game_options import GameOptions
from interface import Interface


class Main:

    def main(self):
        """This is the launching method for the game.  It displays the main menu,
        receives menu selection and launches the options menu and the game when
        prompted."""
        interface = Interface()
        options = GameOptions()

        while True:
            selection = 0
            selection = interface.main_menu()
            if selection == "1":
                name = interface.get_name()
                game = Game(options, name)
                interface.play_game(game)
            elif selection == "2":
                game = Game(options, "None")
                game = interface.load_game_menu(game)
                if game:
                    interface.play_game(game)
            elif selection == "3":
                options = interface.options_menu(options)
            elif selection == "4":
                break


if __name__ == '__main__':

    Main().main()
