from Rule import Rule

class KnowledgeBase:

    # static variable that all the object
    rules = [
        Rule(1, ["For children"], "PG13"),
        Rule(2, ["For adult"], "PG18"),
        Rule(3, ["For Universal"], "U"),

        Rule(4, ["High rating"], "7-10"),
        Rule(5, ["Medium rating"], "5-7"),

        Rule(6, ["Trending"], "2020"),
        Rule(7, ["Old movies"], "2009-2015"),
        Rule(8, ["Recent movies"], "2016-2019"),

        Rule(9, ["PG13", "2020", "7-10", "Action"], "Mulan"),
        Rule(10, ["PG18", "2020", "7-10", "Action"], "Extraction"),
        Rule(11, ["U", "2020", "7-10", "Action"], "Monster Hunter"),
        Rule(12, ["PG13", "2016-2019", "7-10", "Action" ], "The Kid Who Would Be King"),
        Rule(13, ["PG18", "2016-2019", "7-10", "Action"], "Gemini Man"),
        Rule(14, ["U", "2016-2019", "7-10", "Action"], "Skyscraper"),
        Rule(15, ["PG13", "2009-2015", "7-10", "Action" ], "San Andreas"),
        Rule(16, ["PG18", "2009-2015", "7-10", "Action"], "Hansel & Gretel: Witch Hunters"),
        Rule(17, ["U", "2009-2015", "7-10", "Action"], "Journey 2: The mysterous island"),
        Rule(18, ["PG13", "2020", "5-7", "Action"], "Pacific Rim"),
        Rule(19, ["PG18", "2020", "5-7", "Action"], "Bloodshot"),
        Rule(20, ["U", "2020", "5-7", "Action"], "Sonic the Hedgehog"),
        Rule(21, ["PG13", "2016-2019", "5-7", "Action" ], "The Fate of the Furious"),
        Rule(22, ["PG18", "2016-2019", "5-7", "Action"], "King Arthur: Legend of the Sword"),
        Rule(23, ["U", "2016-2019", "5-7", "Action"], "The Darkest Mind"),
        Rule(24, ["PG13", "2009-2015", "5-7", "Action" ], "LimitLess"),
        Rule(25, ["PG18", "2009-2015", "5-7", "Action"], "Hotline"),
        Rule(26, ["U", "2009-2015", "5-7", "Action"], "Unknown"),

        Rule(27, ["PG13", "2020", "7-10", "Sci-Fi"], "Artemis Fowl"),
        Rule(28, ["PG18", "2020", "7-10", "Sci-Fi"], "Underwater"),
        Rule(29, ["U", "2020", "7-10", "Sci-Fi"], "The New Mutants"),
        Rule(30, ["PG13", "2016-2019", "7-10", "Sci-Fi" ], "Guardian of the Galaxy: Vol.2"),
        Rule(31, ["PG18", "2016-2019", "7-10", "Sci-Fi"], "Alien: Covenant"),
        Rule(32, ["U", "2016-2019", "7-10", "Sci-Fi"], "Wonder Woman"),
        Rule(33, ["PG13", "2009-2015", "7-10", "Sci-Fi" ], "Spider-Man: Homecoming"),
        Rule(34, ["PG18", "2009-2015", "7-10", "Sci-Fi"], "Blade Runner 2049"),
        Rule(35, ["U", "2009-2015", "7-10", "Sci-Fi"], "Ready Player One"),
        Rule(36, ["PG13", "2020", "5-7", "Sci-Fi"], "Alita: Battle Angel"),
        Rule(37, ["PG18", "2020", "5-7", "Sci-Fi"], "Life"),
        Rule(38, ["U", "2020", "5-7", "Sci-Fi"], "Venom"),
        Rule(39, ["PG13", "2016-2019", "5-7", "Sci-Fi" ], "Interstellar"),
        Rule(40, ["PG18", "2016-2019", "5-7", "Sci-Fi"], "Mortal Engines"),
        Rule(41, ["U", "2016-2019", "5-7", "Sci-Fi"], "Valerian and the City of a Thousand Planets"),
        Rule(42, ["PG13", "2009-2015", "5-7", "Sci-Fi" ], "Cloud Atlas"),
        Rule(43, ["PG18", "2009-2015", "5-7", "Sci-Fi"], "Black Butler"),
        Rule(44, ["U", "2009-2015", "5-7", "Sci-Fi"], "Spectral"),

        Rule(45, ["PG13", "2020", "7-10", "Comedies"], "Onward"),
        Rule(46, ["PG18", "2020", "7-10", "Comedies"], "Bad Boys for life"),
        Rule(47, ["U", "2020", "7-10", "Comedies"], "My Spy"),
        Rule(48, ["PG13", "2016-2019", "7-10", "Comedies" ], "Ralph Breaks the Internet"),
        Rule(49, ["PG18", "2016-2019", "7-10", "Comedies"], "Deadpool"),
        Rule(50, ["U", "2016-2019", "7-10", "Comedies"], "Despite Everything"),
        Rule(51, ["PG13", "2009-2015", "7-10", "Comedies" ], "The Inbetweeners Movie"),
        Rule(52, ["PG18", "2009-2015", "7-10", "Comedies"], "Bad Neighbours"),
        Rule(53, ["U", "2009-2015", "7-10", "Comedies"], "This is the End"),
        Rule(54, ["PG13", "2020", "5-7", "Comedies"], "The SpongeBob Movie"),
        Rule(55, ["PG18", "2020", "5-7", "Comedies"], "Hooking Up"),
        Rule(56, ["U", "2020", "5-7", "Comedies"], "The Kings Man"),
        Rule(57, ["PG13", "2016-2019", "5-7", "Comedies" ], "Happy Family"),
        Rule(58, ["PG18", "2016-2019", "5-7", "Comedies"], "Bad Moms"),
        Rule(59, ["U", "2016-2019", "5-7", "Comedies"], "Crazy Rich Asians"),
        Rule(60, ["PG13", "2009-2015", "5-7", "Comedies" ], "Up"),
        Rule(61, ["PG18", "2009-2015", "5-7", "Comedies"], "Love & Friendship"),
        Rule(62, ["U", "2009-2015", "5-7", "Comedies"], "Moonrise Kingdom"),
    ]

    # constructor
    def __init__(self):
        pass

    # prints all the rules
    def printRules(self):

        for rule in self.rules:
            print(rule)