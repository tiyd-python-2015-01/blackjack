class Interface:
    """ Interface class will provide all of the methods of interacting with
    the user.  It will contain all of the methods for displaying to the
    console as well as receiving and checking input from the player.

    Responsibilities:
    * Outputting game information and menus to the player
    * Receiving input from the player
    """
    

    def main_menu(self):
        """ Displays the title, programmer info, and main menu for the game.
        Takes user input and returns to the calling Game class"""
        title_text = ("\n"
        ".------..------..------..------..------."
        ".------..------..------..------.\n"
        "|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |"
        "|J.--. ||A.--. ||C.--. ||K.--. |\n"
        "| :(): || :/\: || (\/) || :/\: || :/\: |"
        "| :(): || (\/) || :/\: || :/\: |\n"
        "| ()() || (__) || :\/: || :\/: || :\/: |"
        "| ()() || :\/: || :\/: || :\/: |\n"
        "| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|"
        "| '--'J|| '--'A|| '--'C|| '--'K|\n"
        "`------'`------'`------'`------'`------'"
        "`------'`------'`------'`------'")

        info = ("Programmed by: Alan Grissett\n"
                "The Iron Yard - Durham\n"
                "January 2015\n")

        menu_text = ("<><><><><><><><><><><><><><><><><><><><><><>"
                     "<><><><><><><><><><><><><><")

        print("\n"*80, menu_text)
        print(title_text)
        print("\n", menu_text)
        print(info)
        print("Main Menu:")
        print("♡ 1 - Play Blackjack!")
        print("♧ 2 - Set Game Options")
        print("♢ 3 - Quit")
        print("-----------------------")
        selection = input("♤ ")

        return selection
