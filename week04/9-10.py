"""
finally starting python today
"""

import time

def salary_calculator():
    hourly_wage = int(input("hourly wage: "))
    weeks_worked = int(input("weeks worked: "))

    annual_salary = hourly_wage * 40 * weeks_worked
    print(annual_salary)

# i'm bored im gonna make an ai simulator in the middle of lecture
def chatgpt():
    question = input("hello! what's your question: ")
    for i in range(1,20):
        time.sleep(0.4)
        print("drinking water...")
    print("answer: that's not just a question - that's a burst of knowledge - waiting to happen.")
    print("and honestly - you're so perceptive - for that.")
    print("let me know - if you need anything else! happy coding!")

# chatgpt()

a = """  NO PARKING
2:00 - 6:00 a.m.
"""
print(a)