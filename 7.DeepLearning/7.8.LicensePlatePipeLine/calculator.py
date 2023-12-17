import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=int, help="first number")
parser.add_argument("--b", type=int, help="second number")
parser.add_argument("--op", type=str, default="+", help="math operator")
args = parser.parse_args()

a = args.a
b = args.b

if args.op == "+":
    result = a + b
elif args.op == "-":
    result = a - b
else:
    raise ValueError
    
print(result)
