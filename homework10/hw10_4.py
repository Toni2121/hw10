def string_oper():
    oper_dict: dict = {"lower": lambda w: w.lower(), "upper": lambda w: w.upper(), "len": lambda w: len(w),\
                   "reverse" : lambda w: w[::-1]}
    string_input = input("please enter a string: ")
    operation_input = input("please enter an operation name (lower, upper, len, reverse): ")
    result = oper_dict.get(operation_input, lambda w: "Invalid operation")(string_input)
    print(result)


string_oper()