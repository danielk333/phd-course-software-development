"""

Run this script with e.g.

python process.py "2 3 + 2 3 + +"

"""

import sys

FUNCTIONS = {}


def add_function(operator):
    def decorator(func):
        FUNCTIONS[operator] = func
        return func

    return decorator


@add_function("+")
def add(a, b):
    return a + b


@add_function("*")
def multiply(a, b):
    raise NotImplementedError("TODO")


def parser(tokens: list[str | int]):
    """Parses the input token stream assuming reverse polish notation."""
    # TODO: this is quite inefficient, we are doing too many loops
    # tokenizing could group for us
    while len(tokens) > 1:
        for ind, token in enumerate(tokens):
            if token in FUNCTIONS:
                a = tokens.pop(ind - 2)
                b = tokens.pop(ind - 2)
                op = tokens.pop(ind - 2)
                result = FUNCTIONS[op](a, b)
                tokens.insert(ind - 2, result)
                print(f" {a} {op} {b} = {result} ({tokens})")
                break
    return tokens[0]


def tokenize(expression: str) -> list[str | int]:
    tokens = [
        token if token in FUNCTIONS else int(token)
        for token in expression.strip().split(" ")
    ]
    return tokens


if __name__ == "__main__":
    exp = " ".join(sys.argv[1:])
    # TODO: should probably use argparse
    tokens = tokenize(exp)
    result = parser(tokens)
    print(f"{exp} =  {result}")
