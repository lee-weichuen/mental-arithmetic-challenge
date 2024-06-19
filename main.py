import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 0
MAX_OPERAND = 9

TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr, answer

expr, answer = generate_problem()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
        guess = input("Problem " + str(i+1) + ") " + expr + " : ")

        if guess == str(answer):
            break