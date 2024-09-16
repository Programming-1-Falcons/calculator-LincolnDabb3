while True:
    eq = input("Enter your type Math problem (+ , * , - , // , ** , %): ")
    num1 = float(input("Type your first Number: "))
    num2 = float(input("Type your Second Number: "))
    if eq == "+":
        solved = num1 + num2
    if eq == "-":
        solved = num1 - num2
    if eq == "//":
        solved = num1 // num2
    if eq == "*":
        solved = num1 * num2
    if eq == "**":
        solved = num1 ** num2
    if eq == "%":
        solved = num1 % num2


    print(" " + str(num1) + " " + str(eq) +" "+ str(num2) +" = " + str(round(solved, 5)))
