"""

Run this script with e.g.

python reverse_polish_calculator.py "2 3 + 2 3 + +"
python reverse_polish_calculator.py "2 3 + 2 3 * +"

"""

import sys
import re

OPERATORS = {}
DECIMAL = "."


def add_function(operator):
    def decorator(func):
        OPERATORS[operator] = func
        return func

    return decorator


@add_function("+")
def add(a, b):
    return a + b


@add_function("*")
def multiply(a, b):
    raise NotImplementedError()


@add_function("/")
def divison(a, b):
    raise NotImplementedError()


@add_function("%")
def modulus(a, b):
    raise NotImplementedError()


def chunk_parse(chunk: str, token, stack: list[float | int]):
    if len(chunk) > 0:
        num = int(chunk) if chunk.isdecimal() else float(chunk)
        stack.append(num)

    if token in OPERATORS:
        if len(stack) < 2:
            raise RuntimeError(
                "Cannot perform calculation, panicing\n"
                "binary operation did not get enough inputs"
            )
        stack.append(OPERATORS[token](stack.pop(-1), stack.pop(-1)))


def calculate(expression: str) -> float | int:
    """Parses the input token stream assuming reverse polish notation."""
    last_ind = 0
    stack: list[float | int] = []
    breaks = list(OPERATORS.keys()) + [" "]
    for ind, token in enumerate(expression):
        if token in breaks:
            chunk = expression[last_ind:ind].strip()
            chunk_parse(chunk, token, stack)
            last_ind = ind + 1

    if len(stack) != 1:
        raise RuntimeError("Too many numbers, panicing")
    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"usage {__file__}" + "{CALCULATION}")
        print("\nA calculator that uses reverse polish notation")
        print("For example '3 4 + 2 *' is = 14")

    calculation = " ".join(sys.argv[1:])
    if len(calculation) == 0:
        raise ValueError("Cannot do calculation on a length 0")

    syntax_check = re.compile(
        r"(?!1|2|3|4|5|6|7|8|9|0|"
        + r"|".join([rf"\{op}" for op in OPERATORS])
        + rf"|\s|\{DECIMAL})."
    )
    if syntax_check.search(calculation):
        raise SyntaxError(
            f"Input calculation '{calculation}' cannot be parsed\n"
            "Contains unsupported charachters\n"
            f"Supported operations are {' '.join(OPERATORS.keys())}\n"
            f"Decimal notation uses {DECIMAL}"
        )

    result = calculate(calculation)
    print(f"{calculation} =  {result}")
