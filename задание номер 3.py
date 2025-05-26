import re

def tokenize(expression):
    """Tokenizes a mathematical expression."""

    regex = re.compile(r"""
        \s*                                  # Skip whitespace
        (?P<constant>pi|e|sqrt2|ln2|ln10)  |   # Constant
        (?P<function>sin|cos|tg|ctg|tan|cot|sinh|cosh|th|cth|tanh|coth|ln|lg|log|exp|sqrt|cbrt|abs|sign) |   # Function
        (?P<number>(?:\d+(?:\.\d*)?|\.\d+)) |  # Number (integer or float)
        (?P<variable>[a-zA-Z_][a-zA-Z0-9_]*) | # Variable
        (?P<operator>\^|\*|/|-|\+)           |   # Operator
        (?P<left_parenthesis>\()              |   # Left Parenthesis
        (?P<right_parenthesis>\))             # Right Parenthesis
    """, re.VERBOSE)  

    tokens = []
    for match in regex.finditer(expression):
        if match:
            token = {
                "type": match.lastgroup,
                "span": match.span()
            }
            tokens.append(token)
    return tokens


expressions = [
    "sin(x) + cos(y) * 2.5",
    "pi + usO5NlMvU",
    "( 63393394.98 /8505 )"
]

for expression in expressions:
    print(f"Expression: '{expression}'")
    tokens = tokenize(expression)
    for token in tokens:
        print(token)
    print("-" * 20)
