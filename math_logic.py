from math import sqrt


def quad_formula(a, b, c):
    formula = (-b + sqrt((b*b) - (4*a*c)))/2*a or (-b - sqrt((b*b) - (4*a*c)))/2*a
    solution = ("Therefore .`. : x = ", formula)
    for i in str(formula):
        print(i)
    return solution

my_answer = quad_formula(1, -2, 1)
print("My Answer is : ", my_answer)