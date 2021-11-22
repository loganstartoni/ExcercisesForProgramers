# Twist on the Hello World program.
# Prompt for a name and give a personalized Greeting

# Scenario 1
# Keep the input, string concatenation and output Separate
from typing import List


def saying_hello_scenario_1():
    name = input("What is your name? ")

    output = f"Hello, {name}, nice to meet you."

    print(output)


saying_hello_scenario_1()


# Scenario 2
# Write a version that does not use any variables
def saying_hello_scenario_2():
    print(f"Hello {input('What is your name? ')}, nice to meet you.")


saying_hello_scenario_2()


# Scenario 3
# Write a version of the program that displays different greetings.
def saying_hello_scenario_3():
    import random
    possible_outputs: List[str] = [
        "Hello {name}, nice to meet you.",
        "Hello {name}, I'm happy to finally meet you.",
        "Hi {name}, I'm happy to finally meet you.",
    ]

    name = input("What is your name? ")

    output = random.SystemRandom().choice(possible_outputs)
    output = output.format(name=name)

    print(output)


saying_hello_scenario_3()
