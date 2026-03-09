def add(a, b):
    answer = a + b
    return str(a) + " + " + str(b) + " = " + str(answer)

def sub(a, b):
    answer = a - b
    return str(a) + " - " + str(b) + " = " + str(answer)

def mul(a, b):
    answer = a * b
    return str(a) + " * " + str(b) + " = " + str(answer)

def div(a, b):
    answer = a / b
    return str(a) + " / " + str(b) + " = " + str(answer)


print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
print("e. Exit")

choice = input("Enter your choice: ").lower()

if choice == "a":
    print("Addition")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    print(add(a, b))

elif choice == "b":
    print("Subtraction")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    print(sub(a, b))

elif choice == "c":
    print("Multiplication")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    print(mul(a, b))
elif choice == "d":
    print("Division")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    print(div(a, b))
