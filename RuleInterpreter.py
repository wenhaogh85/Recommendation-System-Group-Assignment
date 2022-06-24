from KnowledgeBase import KnowledgeBase

class RuleInterpreter:

    # constructor
    def __init__(self, working_memory):

        knowledge_base = KnowledgeBase()
        extract_rules = knowledge_base.rules
        self.rules = extract_rules

        self.working_memory = working_memory

    # algorithm for forward chaining
    def forward_chaining(self):

        temp_rules = []

        # while loop to make sure the checking algorithm loops repeatedly
        while True:

            # Boolean for whether the rule is fired
            ruleIsFired = False

            print("Facts in working memory:", self.working_memory.getFacts())

            # loops through all the rules in one cycle
            # The length of the list is first obtained
            for index in range(len(self.rules)):

                # If the conditions are met the rules are fired
                if self.met_conditions(self.rules[index]) == True:

                    print("\n" + ("-" * 30))
                    print("\nFiring rule:", self.rules[index])

                    self.fireRule(self.rules[index])

                    # Adding the rule number into the rule_numbers list for easy reference
                    self.working_memory.rule_numbers.append(self.rules[index].getRuleNumber())

                    print("List of rules fired: ", self.working_memory.rule_numbers)
                    print("\nAdding consequent [",self.rules[index].getConsequent(),"] to Working Memory...")

                    temp_rules.append(self.rules[index])
                    
                    # Rule removed after fired
                    del self.rules[index]

                    print("Rule has been removed...")

                    # Loop breaks after rule is fired
                    ruleIsFired = True
                    break

            # algorithm stops when no rules are fired
            if ruleIsFired == False:
                print("\nNo rules has been fired after scanning all the rules....")
                print("Ending the algorithm...")
                break

        return temp_rules

    def backward_chaining(self, hypothesis):

        master_list = []
        
        print("*** BACKWARD CHAINING ***\n")
        print("User given hypothesis: ", hypothesis, "\n")

        # initialises rules put aside
        rules_put_aside = []

        # if during backtracking, the rule is found,
        # then append the rule into the rules put aside list
        check_rule = self.backtracking(hypothesis)
        if check_rule != None:

            rules_put_aside.append(check_rule)
            master_list.append(check_rule)

            print("Matching rule", check_rule)

        # get initial subgoal
        subgoals = self.getSubGoal(hypothesis)

        print("\nGet subgoals....")
        print("Subgoals:", subgoals)

        if len(subgoals) != 0:

            print("\nCheck if hypothesis is possible to solve....")

            # initialses boolean value of whether to perform
            # forward chaining at the end of the result
            execute = True

            # keeps looping until all the subgoals is removed
            while len(subgoals) != 0:

                print("\n" + "-" * 50)
                print("Start to resolve subgoals....")
                print("Subgoals being resolved is ---->", subgoals[0])
                print("Facts in working memory so far:", self.working_memory.getFacts())
                print("Putting aside rule number(s):", [rule.rule_number for rule in rules_put_aside])

                # scans through each rule for its consequent for every subgoal

                # rule is found means that for any one of the subgoals,
                # if the subgoal matches the rule's consequent, then it
                # is set to True, it is initialzed to False for every loop
                print("\nLooping for each rule...")

                ruleIsFound = False
                for index in range(len(subgoals)):

                    # breaks if a rule's consequent matches the subgoal
                    rule = self.backtracking(subgoals[index])

                    if rule != None:
                        print("Matched rule with subgoal ----> ", rule)
                        ruleIsFound = True
                        break

                    else:
                        ruleIsFound = False
                        master_list.append(subgoals[index])
                        break

                if ruleIsFound == True:

                    new_subgoals = self.getSubGoal(subgoals[index])

                    print("\nGet new subgoal...")
                    print("New subgoal:", new_subgoals)

                    # determine if the subgoal that activated
                    # the rule needs to be removed
                    if len(new_subgoals) == 0:

                        master_list.append(subgoals[index])
                        master_list.append(rule)

                        print("Subgoal is removed...")

                        self.working_memory.addFacts(subgoals[index])
                        del subgoals[index]

                    else:
                        master_list.append(subgoals[index])
                        master_list.append(rule)

                        print("New subgoals is added")
                        print("New rule is added...")
                        
                        i = 0
                        while i < len(new_subgoals):
                            subgoals.insert(0, new_subgoals[i])
                            i += 1

                        rules_put_aside.insert(0, rule)

                else:
                    print("Hypothesis is not proven!!")
                    master_list.append(False)
                    execute = False
                    break

            # if all subgoal is fulfilled, forward chaining is performed
            if execute == True:
                print("**** Perform forward chaining... *****")

                self.forward_chaining_bc(hypothesis, rules_put_aside)
                master_list.append(True)

        else:
            if self.backtracking(hypothesis) != None:

                print("Found hypothesis on first try")
                print("Perform forward chaining...")

                self.forward_chaining_bc(hypothesis, rules_put_aside)
                master_list.append(True)

            else:
                master_list.append(False)

        return master_list

    # forward chaining to prove hypothesis
    def forward_chaining_bc(self, hypothesis, rules_put_aside):

        while True:

            print("Order of rules put aside:", [rule.getRuleNumber() for rule in rules_put_aside])

            ruleIsFired = False

            for rule in rules_put_aside:

                print("\n" + ("-" * 30))
                print("Next iteration")
                print("Total number of rules to scan:", len(rules_put_aside))
                print("Scanning all rules put aside....\n")

                if self.met_conditions(rule) == True:

                    print("\nFiring rule:", rule.getRuleNumber())

                    self.fireRule(rule)

                    self.working_memory.rule_numbers.append(rule.getRuleNumber())

                    print("List of rules fired: ", self.working_memory.rule_numbers)

                    # Rule removed after fired
                    temp_index = rules_put_aside.index(rule)
                    print("Retrieving index:",temp_index)

                    del rules_put_aside[temp_index]
                    print("Rule has been removed...")

                    # Loop breaks after rule is fired
                    ruleIsFired = True
                    break

                else:
                    print("Rules fired: ", self.working_memory.rule_numbers)

            # Algorithm stops when no rules are fired
            if self.working_memory.getFacts()[-1] == hypothesis:

                print("Matches hypothesis....")
                print("Ending...")
                break

    def getSubGoal(self, hypothesis):

        rule = self.backtracking(hypothesis)
        subgoals = []

        # if the hypothesis matches a rule's consequent
        if rule != None:

            for antedecent in rule.getAntecedent():

                # get subgoals if the antecedent is not in the working memory
                if self.in_working_memory(antedecent) == False:
                    subgoals.append(antedecent)

        return subgoals

    # get a subgoal based on hypothesis
    def backtracking(self, hypothesis):

        # backtracks to find the a rule's consequent that match the hypothesis
        for index in range(len(self.rules)):

            if self.rules[index].getConsequent() == hypothesis:
                return self.rules[index]

        return None

    def in_working_memory(self, antedecent):

        isDuplicate = False
        for fact in self.working_memory.getFacts():
            if fact == antedecent:
                isDuplicate = True
                break

        return isDuplicate

    # checks if all conditions in a rule is met
    def met_conditions(self, rule):

        result = False
        total_conditions = 0
        conditions = rule.getAntecedent()

        iteration = 1

        # loops through all the antecedents
        for condition in conditions:

            # loops through all the facts in the working memory
            for fact in self.working_memory.getFacts():

                # checks if the fact meets the condition
                if fact == condition:
                    total_conditions += 1
                    break

        # checks if all the conditions are met for a particular rule
        if total_conditions == len(conditions):
            result = True

        else:
            result = False

        return result

    # fire the rule and get the consequent,
    # and add to the working memory
    def fireRule(self, rule):

        # extract new fact from consequent
        new_fact = rule.getConsequent()

        #add the new fact into the working memory
        self.working_memory.addFacts(new_fact)