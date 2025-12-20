def calculate(a, b, operation):
    if operation == "addition":
        import addition
        return addition.operate(a, b)
    elif operation == "subtraction":
        import subtraction
        return subtraction.operate(a, b)
    elif operation == "multiplication":
        import multiplication
        return multiplication.operate(a, b)
    elif operation == "division":
        import division
        return division.operate(a, b)
    else:
        print("неизвестная операция")