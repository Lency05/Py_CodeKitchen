while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("Enter Your choice (1-5) ", end="")
    ch = int(input())

    if ch >= 1 and ch <= 4:
        print("\nEnter Two Numbers: ", end="")
        numOne = float(input())
        numTwo = float(input())

        if ch == 1:
            res = numOne + numTwo
            print("\nResult = ", res)
        elif ch == 2:
            res = numOne - numTwo
            print("\nResult = ", res)
        elif ch == 3:
            res = numOne * numTwo
            print("\nResult = ", res)
        elif ch == 4:
            if numTwo != 0:
                res = numOne / numTwo
                print("\nResult = ", res)
            else:
                print("\nDivision by zero is not allowed")
    elif ch == 5:
        print("\nExiting the calculator")
        print("___________________________")
        break
    else:
        print("\nInvalid choice. Please enter a valid option (1-5)")
