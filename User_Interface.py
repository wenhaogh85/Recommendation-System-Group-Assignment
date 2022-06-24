from WorkingMemory import WorkingMemory
from RuleInterpreter import RuleInterpreter
from KnowledgeBase import KnowledgeBase
from Rule import Rule
from question import *

print(
    ("-" * 30) +
    "\nRecommendation system\n" +
    ("-" * 30)
)

# initialises variables
facts = []
working_memory = WorkingMemory()
knowledge_base = KnowledgeBase()

# ask questions
chaining = main_question()

if chaining == "Forward":

    # prompts the user for questions
    fc_question_1(facts)
    fc_question_2(facts)
    fc_question_3(facts)
    fc_question_4(facts)

    # adds facts into working memory
    working_memory.addFacts(facts)
    print("*** FORWARD CHAINING ***\n")
    print("User defined facts: ", facts)

    # initialise the rule interpreter
    rule_interpreter = RuleInterpreter(working_memory)

    # perform forward chaining
    temp_rules = rule_interpreter.forward_chaining()
    
    print("-" * 30)
    print("*** INFERENCE TABLE ***\n")
    print(facts)
    for rule in temp_rules:
        print("{} => {}".format(rule.getAntecedent(), rule.getConsequent()))

elif chaining == "Backward":

    genre = genre_question()

    # adds facts into working memory
    working_memory.addFacts(genre)

    facts.append(genre)

    # initialise the rule interpreter
    rule_interpreter = RuleInterpreter(working_memory)

    if genre == "Action":

        hypothesis = action_questions()

        category = bc_question_1()
        rating = bc_question_2()
        trend = bc_question_3()

        facts.append(category)
        facts.append(rating)
        facts.append(trend)

        working_memory.addFacts(category)
        working_memory.addFacts(rating)
        working_memory.addFacts(trend)

        master_list = rule_interpreter.backward_chaining(hypothesis)

    elif genre == "Sci-Fi":

        hypothesis = sci_fi_questions()

        category = bc_question_1()
        rating = bc_question_2()
        trend = bc_question_3()

        facts.append(category)
        facts.append(rating)
        facts.append(trend)

        working_memory.addFacts(category)
        working_memory.addFacts(rating)
        working_memory.addFacts(trend)

        master_list = rule_interpreter.backward_chaining(hypothesis)

    elif genre == "Comedies":

        hypothesis = comedies_questions()

        category = bc_question_1()
        rating = bc_question_2()
        trend = bc_question_3()

        facts.append(category)
        facts.append(rating)
        facts.append(trend)

        working_memory.addFacts(category)
        working_memory.addFacts(rating)
        working_memory.addFacts(trend)

        master_list = rule_interpreter.backward_chaining(hypothesis)

    print("-" * 30)
    print("*** INFERENCE TABLE ***\n")
    print("Facts: {} \n\nHypothesis: {}".format(facts, hypothesis), end="")

    align = 0
    if master_list[-1] == False:
        del master_list[-1]

        for item in master_list:

            if isinstance(item, Rule):
                print(" || {}".format(item))
            else:
                print("Subgoal: {}".format(item), end="")

            if align % 2 == 0:
                print()

            align += 1

        print("|| Hypothesis is not proven")

    else:
        del master_list[-1]

        for item in master_list:

            if isinstance(item, Rule):
                print(" || {}".format(item), end="")
            else:
                print("Subgoal: {}".format(item), end="")

            if align % 2 == 0:
                print()

            align += 1

        print("|| Hypothesis is proven")