import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide
              }

def calculator(sign, n1, n2):
    if sign == "+":
        return add(n1, n2)
    elif sign == "-":
        return subtract(n1, n2)
    elif sign == "*":
        return multiply(n1, n2)
    elif sign == "/":
        return divide(n1, n2)
    return None

def restart():
    first_number = int(input("Type your first number: "))
    operator = input("Type your operator: '+', '-', '*', '/'")
    second_number = int(input("Type your second number: "))
    latest_answer = calculator(operator, first_number, second_number)
    print(f"Your value is: {latest_answer}")
    return latest_answer

value = restart()
continue_cal = True
while continue_cal:
    previous_continue = input("Yes or no: ")
    if previous_continue == "yes":
        operator = input("Type your operator: '+', '-', '*', '/'")
        second_number = int(input("Type your second number: "))
        value = calculator(operator, value, second_number)
        print(f"Your value is: {value}")
    elif previous_continue == "no":
        print("\n" * 100)
        restart()
    else:
        print("Math Complete")
        continue_cal = False


#Multiply 4 * 8 using the dictionary
# print(dictionary["*"](4,8)

