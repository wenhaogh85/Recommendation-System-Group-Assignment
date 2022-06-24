def main_question():

    while True:

            print(
                "Would you like to perform forward or backward chaining" +
                "\n+----------------+------------------+" +
                "\n|    Option      |    Chanining     |" +
                "\n+----------------+------------------+" +
                "\n|       1        |     Forward      |" +
                "\n+----------------+------------------+" +
                "\n|       2        |     Backward     |" +
                "\n+----------------+------------------+"
            )

            try:
                user_input = int(input("Enter choice: "))

                if user_input == 1:
                    return "Forward"

                elif user_input == 2:
                    return "Backward"

                else:
                    print("\nValue entered should be between 1 and 2!!\n")

            except ValueError:
                print("\nThe choice entered is not valid!")

def fc_question_1(facts):

    while True:

        print(
            "\nQuestion 1: Choose a genre based on the options provided" +
            "\n+----------------+------------------+" +
            "\n|    Option      |      Genre       |" +
            "\n+----------------+------------------+" +
            "\n|       1        |      Action      |" +
            "\n+----------------+------------------+" +
            "\n|       2        |     Comedies     |" +
            "\n+----------------+------------------+" +
            "\n|       3        |      Sci-fi      |" +
            "\n+----------------+------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return facts.append("Action")

            elif user_genre == 2:
                return facts.append("Comedies")

            elif user_genre == 3:
                return facts.append("Sci-fi")

            else:
                print("\nValue entered should be between 1 and 3!!\n")

        except ValueError:
            print("\nThe choice entered is not valid!")

def fc_question_2(facts):

    while True:

        print(
            "\nQuestion 2: Choose a category based on the movie you want to choose" +
            "\n+----------------+-------------------+" +
            "\n|     Option     |      Category     |" +
            "\n+----------------+-------------------+" +
            "\n|       1        |    For Childrens  |" +
            "\n+----------------+-------------------+" +
            "\n|       2        |     For Adults    |" +
            "\n+----------------+-------------------+" +
            "\n|       3        |     Universal     |" +
            "\n+----------------+-------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return facts.append("For children")

            elif user_genre == 2:
                return facts.append("For adult")

            elif user_genre == 3:
                return facts.append("For Universal")

            else:
                print("\nChoice of action should be between 1 and 3!!\n")

        except ValueError:
            print("\nThe choice entered is not valid!")

def fc_question_3(facts):

    while True:

        print(
            "\nQuestion 3: Choose a movie based on the trend" +
            "\n+----------------+------------------+" +
            "\n|     Option     |      Trend       |" +
            "\n+----------------+------------------+" +
            "\n|       1        |     Trending     |" +
            "\n+----------------+------------------+" +
            "\n|       2        |   Recent Movies  |" +
            "\n+----------------+------------------+" +
            "\n|       3        |    Old Movies    |" +
            "\n+----------------+------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return facts.append("Trending")

            elif user_genre == 2:
                return facts.append("Recent movies")

            elif user_genre == 3:
                return facts.append("Old movies")

            else:
                print("\nChoice of action must be between 1 and 3")

        except ValueError:
            print("\nThe choice entered is not valid!")

def fc_question_4(facts):

    while True:

        print(
            "\nQuestion 4: Choose a movie based on the rating" +
            "\n+----------------+------------------+" +
            "\n|     Option     |      Rating      |" +
            "\n+----------------+------------------+" +
            "\n|       1        |    High Rating   |" +
            "\n+----------------+------------------+" +
            "\n|       2        |   Medium Rating  |" +
            "\n+----------------+------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return facts.append("High rating")

            elif user_genre == 2:
                return facts.append("Medium rating")

            else:
                print("\nChoice of action should be between 1 and 2")

        except ValueError:
            print("\nThe choice entered is not valid!")


def genre_question():

    while True:

        print(
            "\nQuestion 2: Choose a movie based on the trend" +
            "\n+----------------+------------------+" +
            "\n|     Option     |      Genre       |" +
            "\n+----------------+------------------+" +
            "\n|       1        |      Action      |" +
            "\n+----------------+------------------+" +
            "\n|       2        |      Sci-Fi      |" +
            "\n+----------------+------------------+" +
            "\n|       3        |     Comedies     |" +
            "\n+----------------+------------------+"
        )

        try:
            user_input = int(input("\nEnter options: "))

            if user_input == 1:
                return "Action"

            elif user_input == 2:
                return "Sci-Fi"

            elif user_input == 3:
                return "Comedies"

            else:
                print("\nChoice of action must be between 1 and 3")

        except ValueError:
            print("\nThe choice entered is not valid!")

def action_questions():

    while True:

        print(
            "\nQuestion 3: Choose a movie" +
            "\n+----------------+----------------------------------+" +
            "\n|     Option     |               Movie              |" +
            "\n+----------------+----------------------------------+" +
            "\n|       1        |               Mulan              |" +
            "\n+----------------+----------------------------------+" +
            "\n|       2        |             Extraction           |" +
            "\n+----------------+----------------------------------+" +
            "\n|       3        |           Monster Hunter         |" +
            "\n+----------------+----------------------------------+" +
            "\n|       4        |     The Kid Who Would Be King    |" +
            "\n+----------------+----------------------------------+" +
            "\n|       5        |             Gemini Man           |" +
            "\n+----------------+----------------------------------+" +
            "\n|       6        |             Skyscraper           |" +
            "\n+----------------+----------------------------------+" +
            "\n|       7        |            San Andreas           |" +
            "\n+----------------+----------------------------------+" +
            "\n|       8        |  Hansel & Gretel: Witch Hunters  |" +
            "\n+----------------+----------------------------------+" +
            "\n|       9        |  Journey 2: The mysterous island |" +
            "\n+----------------+----------------------------------+" +
            "\n|      10        |             Pacific Rim          |" +
            "\n+----------------+----------------------------------+" +
            "\n|      11        |              Bloodshot           |" +
            "\n+----------------+----------------------------------+" +
            "\n|      12        |         Sonic the Hedgehog       |" +
            "\n+----------------+----------------------------------+" +
            "\n|      13        |      The Fate of the Furious     |" +
            "\n+----------------+----------------------------------+" +
            "\n|      14        | King Arthur: Legend of the Sword |" +
            "\n+----------------+----------------------------------+" +
            "\n|      15        |         The Darkest Mind         |" +
            "\n+----------------+----------------------------------+" +
            "\n|      16        |             LimitLess            |" +
            "\n+----------------+----------------------------------+" +
            "\n|      17        |              Hotline             |" +
            "\n+----------------+----------------------------------+" +
            "\n|      18        |              Unknown             |" +
            "\n+----------------+----------------------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return "Mulan"

            elif user_genre == 2:
                return "Extraction"

            elif user_genre == 3:
                return "Monster Hunter"

            elif user_genre == 4:
                return "The Kid Who Would Be King"

            elif user_genre == 5:
                return "Gemini Man"

            elif user_genre == 6:
                return "Skyscraper"

            elif user_genre == 7:
                return "San Andreas"

            elif user_genre == 8:
                return "Hansel & Gretel: Witch Hunters"

            elif user_genre == 9:
                return "Journey 2: The mysterous island"

            elif user_genre == 10:
                return "Pacific Rim"

            elif user_genre == 11:
                return "Bloodshot"

            elif user_genre == 12:
                return "Sonic the Hedgehog"

            elif user_genre == 13:
                return "The Fate of the Furious"

            elif user_genre == 14:
                return "King Arthur: Legend of the Sword"

            elif user_genre == 15:
                return "The Darkest Mind"

            elif user_genre == 16:
                return "LimitLess"

            elif user_genre == 17:
                return "Hotline"

            elif user_genre == 18:
                return "Unknown"

            else:
                print("\nChoice of action must be between 1 and 18")

        except ValueError:
            print("\nThe choice entered is not valid!")

def sci_fi_questions():

    while True:

        print(
            "\nQuestion 3: Choose a movie" +
            "\n+----------------+---------------------------------------------+" +
            "\n|     Option     |                   Movie                     |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       1        |               Artemis Fowl                  |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       2        |                 Underwater                  |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       3        |               The New Mutants               |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       4        |         Guardian of the Galaxy: Vol.2       |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       5        |              Alien: Covenant                |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       6        |                Wonder Woman                 |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       7        |            Spider-Man: Homecoming           |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       8        |              Blade Runner 2049              |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|       9        |              Ready Player One               |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      10        |             Alita: Battle Angel             |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      11        |                   Life                      |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      12        |                  Venom                      |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      13        |                Interstellar                 |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      14        |               Mortal Engines                |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      15        | Valerian and the City of a Thousand Planets |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      16        |                 Cloud Atlas                 |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      17        |                 Black Butler                |" +
            "\n+----------------+---------------------------------------------+" +
            "\n|      18        |                   Spectral                  |" +
            "\n+----------------+---------------------------------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return "Artemis Fowl"

            elif user_genre == 2:
                return "Underwater"

            elif user_genre == 3:
                return "The New Mutants"

            elif user_genre == 4:
                return "Guardian of the Galaxy: Vol.2"

            elif user_genre == 5:
                return "Alien: Covenant"

            elif user_genre == 6:
                return "Wonder Woman"

            elif user_genre == 7:
                return "Spider-Man: Homecoming"

            elif user_genre == 8:
                return "Blade Runner 2049"

            elif user_genre == 9:
                return "Ready Player One"

            elif user_genre == 10:
                return "Alita: Battle Angel"

            elif user_genre == 11:
                return "Life"

            elif user_genre == 12:
                return "Venom"

            elif user_genre == 13:
                return "Interstellar"

            elif user_genre == 14:
                return "Mortal Engines"

            elif user_genre == 15:
                return "Valerian and the City of a Thousand Planets"

            elif user_genre == 16:
                return "Cloud Atlas"

            elif user_genre == 17:
                return "Black Butler"

            elif user_genre == 18:
                return "Spectral"

            else:
                print("\nChoice of action must be between 1 and 18")

        except ValueError:
            print("\nThe choice entered is not valid!")

def comedies_questions():

    while True:

        print(
            "\nQuestion 3: Choose a movie" +
            "\n+----------------+-----------------------------+" +
            "\n|     Option     |           Movie             |" +
            "\n+----------------+-----------------------------+" +
            "\n|       1        |          Onward             |" +
            "\n+----------------+-----------------------------+" +
            "\n|       2        |     Bad Boys for life       |" +
            "\n+----------------+-----------------------------+" +
            "\n|       3        |           My Spy            |" +
            "\n+----------------+-----------------------------+" +
            "\n|       4        |  Ralph Breaks the Internet  |" +
            "\n+----------------+-----------------------------+" +
            "\n|       5        |         Deadpool            |" +
            "\n+----------------+-----------------------------+" +
            "\n|       6        |      Despite Everything     |" +
            "\n+----------------+-----------------------------+" +
            "\n|       7        |   The Inbetweeners Movie    |" +
            "\n+----------------+-----------------------------+" +
            "\n|       8        |       Bad Neighbours        |" +
            "\n+----------------+-----------------------------+" +
            "\n|       9        |      This is the End        |" +
            "\n+----------------+-----------------------------+" +
            "\n|      10        |   The SpongeBob Movie       |" +
            "\n+----------------+-----------------------------+" +
            "\n|      11        |         Hooking Up          |" +
            "\n+----------------+-----------------------------+" +
            "\n|      12        |       The Kings Man         |" +
            "\n+----------------+-----------------------------+" +
            "\n|      13        |        Happy Family         |" +
            "\n+----------------+-----------------------------+" +
            "\n|      14        |          Bad Moms           |" +
            "\n+----------------+-----------------------------+" +
            "\n|      15        |     Crazy Rich Asians       |" +
            "\n+----------------+-----------------------------+" +
            "\n|      16        |            Up               |" +
            "\n+----------------+-----------------------------+" +
            "\n|      17        |     Love & Friendship       |" +
            "\n+----------------+-----------------------------+" +
            "\n|      18        |     Moonrise Kingdom        |" +
            "\n+----------------+-----------------------------+"
        )

        try:
            user_genre = int(input("\nEnter options: "))

            if user_genre == 1:
                return "Onward"

            elif user_genre == 2:
                return "Bad Boys for life"

            elif user_genre == 3:
                return "My Spy"

            elif user_genre == 4:
                return "Ralph Breaks the Internet"

            elif user_genre == 5:
                return "Deadpool"

            elif user_genre == 6:
                return "Despite Everything"

            elif user_genre == 7:
                return "The Inbetweeners Movie"

            elif user_genre == 8:
                return "Bad Neighbours"

            elif user_genre == 9:
                return "This is the End"

            elif user_genre == 10:
                return "The SpongeBob Movie"

            elif user_genre == 11:
                return "Hooking Up"

            elif user_genre == 12:
                return "The Kings Man"

            elif user_genre == 13:
                return "Happy Family"

            elif user_genre == 14:
                return "Bad Moms"

            elif user_genre == 15:
                return "Crazy Rich Asians"

            elif user_genre == 16:
                return "Up"

            elif user_genre == 17:
                return "Love & Friendship"

            elif user_genre == 18:
                return "Moonrise Kingdom"

            else:
                print("\nChoice of action must be between 1 and 18")

        except ValueError:
            print("\nThe choice entered is not valid!")

def bc_question_1():

    while True:

        print(
            "\nQuestion 4: Choose a category" +
            "\n+----------------+-----------------+" +
            "\n|     Option     |    Category     |" +
            "\n+----------------+-----------------+" +
            "\n|       1        |  For children   |" +
            "\n+----------------+-----------------+" +
            "\n|       2        |    For adult    |" +
            "\n+----------------+-----------------+" +
            "\n|       3        |  For Universals |" +
            "\n+----------------+-----------------+"
        )

        try:
            user_input = int(input("\nEnter options: "))

            if user_input == 1:
                return "For children"

            elif user_input == 2:
                return "For adult"

            elif user_input == 3:
                return "For Universals"

            else:
                print("\nChoice of action must be between 1 and 3")

        except ValueError:
            print("\nThe choice entered is not valid!")

def bc_question_2():

    while True:

        print(
            "\nQuestion 5: Choose a rating" +
            "\n+----------------+-----------------+" +
            "\n|     Option     |      Rating     |" +
            "\n+----------------+-----------------+" +
            "\n|       1        |   High rating   |" +
            "\n+----------------+-----------------+" +
            "\n|       2        |  Medium rating  |" +
            "\n+----------------+-----------------+"
        )

        try:
            user_input = int(input("\nEnter options: "))

            if user_input == 1:
                return "High rating"

            elif user_input == 2:
                return "Medium rating"

            else:
                print("\nChoice of action must be between 1 and 2")

        except ValueError:
            print("\nThe choice entered is not valid!")

def bc_question_3():

    while True:

        print(
            "\nQuestion 6: Choose a trend" +
            "\n+----------------+-----------------+" +
            "\n|     Option     |     Trend       |" +
            "\n+----------------+-----------------+" +
            "\n|       1        |    Trending     |" +
            "\n+----------------+-----------------+" +
            "\n|       2        |   Old movies    |" +
            "\n+----------------+-----------------+" +
            "\n|       3        |  Recent movies  |" +
            "\n+----------------+-----------------+"
        )

        try:
            user_input = int(input("\nEnter options: "))

            if user_input == 1:
                return "Trending"

            elif user_input == 2:
                return "Old movies"

            elif user_input == 3:
                return "Recent movies"

            else:
                print("\nChoice of action must be between 1 and 3")

        except ValueError:
            print("\nThe choice entered is not valid!")
