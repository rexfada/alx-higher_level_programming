#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    ar = sys.argv
    le = len(ar)

    if le != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(ar[1])
    op = ar[2]
    b = int(ar[3])

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, calc.add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, calc.sub(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, calc.mul(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
