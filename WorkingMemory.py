class WorkingMemory:

    # constructor
    def __init__(self):
        self.facts = []
        self.rule_numbers = []

    # adds fact to working memory
    def addFacts(self, fact):

        if type(fact) == str:
            self.facts.append(fact)

        elif type(fact) == list:
            self.facts.extend(fact)

    # getter for facts
    def getFacts(self):
        return self.facts

    # getter for rule numbers
    def getRuleNumbers(self):
        return self.rule_numbers