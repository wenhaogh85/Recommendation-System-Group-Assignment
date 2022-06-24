class Rule:

    # constructor
    def __init__(self, rule_number, antecedent, consequent):
        self.rule_number = rule_number
        self.antecedent = antecedent
        self.consequent = consequent

    # getter for antecedent
    def getAntecedent(self):
        return self.antecedent

    # getter for consequent
    def getConsequent(self):
        return self.consequent

    # getter for rule number
    def getRuleNumber(self):
        return self.rule_number

    # overrides dunder str (similar to overriding toString)
    def __str__(self):
        return "Rule {}: If {} then {}".format(self.rule_number, self.antecedent, self.consequent)