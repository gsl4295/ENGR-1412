"""
week 6 done!
1/24 done with degree
"""

def lab6_problem1():
    base_char = input()
    head_char = input()

    row1 = "      " + head_char
    row2 = f"{base_char*6}{head_char*2}"
    row3 = f"{base_char*6}{head_char*3}"

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)
    pass

def lab6_problem2():
    phone_number = str(input())

    area_code = phone_number[0:3]
    second_set = phone_number[3:6]
    four_others = phone_number[6:10]

    print(f"({area_code}) {second_set}-{four_others}")

def lab6_problem3():
    initial_mg = int(input())
    current_mg = initial_mg / 2
    print(f"After 6 hours: {current_mg:.2f} mg")
    current_mg /= 2
    print(f"After 12 hours: {current_mg:.2f} mg")
    current_mg /= 4
    print(f"After 24 hours: {current_mg:.2f} mg")

def lab6_problem4():
    current_price = int(input())
    last_months_price = int(input())
    change = current_price - last_months_price
    print(f"This house is ${current_price}. The change is ${change} since last month.")
    print(f"The estimated monthly mortgage is ${((current_price * 0.051) / 12):.2f}.")

def lab6_problem5():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    total = num1 + num2 + num3 + num4
    product = num1 * num2 * num3 * num4

    print(f"{product:.0f} {(total / 4):.0f}")
    print(f"{product:.3f} {(total / 4):.3f}")

def lab6_problem6():
    favorite_color = str(input())
    pet_name = str(input())
    user_num = int(input())

    pw1 = f"{favorite_color}_{pet_name}"
    pw2 = f"{user_num}{favorite_color}{user_num}"

    print(f"You entered: {favorite_color} {pet_name} {user_num}\n")
    print(f"First password: {pw1}")
    print(f"Second password: {pw2}\n")

    print(f"Number of characters in {pw1}: {len(pw1)}")
    print(f"Number of characters in {pw2}: {len(pw2)}")

def lab6_problem8():
    score_set1 = {10, 64}
    score_set2 = {24, 32, 44, 51}
    passed_set = {44, 51, 64}

    all_score_set = set()
    all_score_set.update(score_set1)
    all_score_set.update(score_set2)
    print(all_score_set)

    # sets really are not fun
    failed_set = all_score_set.difference(passed_set)
    print(failed_set)

    num_of_failed = len(failed_set)

    print('Total {} student failed'.format(num_of_failed), end='')

lab6_problem8()
