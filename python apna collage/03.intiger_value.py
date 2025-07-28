# a=int(input("enter a="))
# b=int(input("enter b="))

# print("enrter all value = ",a+b)
# print("enrter all value = ",a-b)
# print("enrter all value = ",a*b)
# print("enrter all value = ",a/b)



def basic_operations():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Division: Cannot divide by zero")
basic_operations()





def swap_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}")
swap_numbers()