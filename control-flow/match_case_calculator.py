num1 = int (input("enter the first number"))
num2= int (input("enter the second number"))
operation = input ("Choose the operation (+, -, *, /):")

match operation :

    case "+" :

        the_result = num1 + num2
        print(f"The result is {the_result}.")

    case "-" :

        the_result = num1 - num2
        print(f"the result is {the_result}")

    case "*" :

        the_result = num1 * num2
        print(f"the result is{the_result}")

    case "/":

        if num2 == 0 :
            print("Cannot divide by zero.")
        else :
             the_result = num1 / num2
             print(f"the result is{the_result}")