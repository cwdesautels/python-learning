import sys
import math
import traceback
from dataclasses import dataclass, field


@dataclass
class Token:
    lexeme: str


@dataclass
class Operand(Token):
    value: float = field(default=None, repr=False)


@dataclass
class Operator(Token):
    priority: int = field(default=None, repr=False)
    executor: callable = field(default=None, repr=False)
    params: int = field(default=None, repr=False)


@dataclass
class Infix(Operator):
    params: int = field(default=2, repr=False)


@dataclass
class Prefix(Operator):
    params: int = field(default=1, repr=False)


left_parenthesis = Token('(')
right_parenthesis = Token(')')
reserved_tokens = {
    '(': left_parenthesis,
    ')': right_parenthesis
}

# Map of operators allows quick retrieval
infix_operators = {
    '+': Infix(lexeme='+', priority=2, executor=lambda a, b: a + b),
    '-': Infix(lexeme='-', priority=2, executor=lambda a, b: a - b),
    '*': Infix(lexeme='*', priority=3, executor=lambda a, b: a * b),
    '/': Infix(lexeme='/', priority=4, executor=lambda a, b: a / b),
    '^': Infix(lexeme='^', priority=6, executor=lambda a, b: math.pow(a, b) if a >= 0 else 1/0)
}

prefix_operators = {
    '+': Prefix(lexeme='+', priority=5, executor=lambda a: +a),
    '-': Prefix(lexeme='-', priority=5, executor=lambda a: -a),
    'abs': Prefix(lexeme='abs', priority=7, executor=lambda a: abs(a)),
    'sqrt': Prefix(lexeme='sqrt', priority=7, executor=lambda a: math.sqrt(a))
}


def next_token(string_data: str, offset: int, limit: int) -> Token:
    lexeme = string_data[offset]

    # Hack because I know all reserved and infix tokens are single characters
    if lexeme in reserved_tokens:
        return reserved_tokens[lexeme]
    elif lexeme in infix_operators:
        return infix_operators[lexeme]
    else:
        while offset < limit:
            offset += 1
            if offset == limit:
                break
            else:
                next = string_data[offset]
                if next in infix_operators or next in prefix_operators or next in reserved_tokens or next.isalpha() != lexeme.isalpha():
                    break
                else:
                    lexeme += next
        if lexeme in prefix_operators:
            return prefix_operators[lexeme]
        else:
            return Operand(lexeme=lexeme, value=float(lexeme))


def parse_tokens(string_input: str) -> list:
    string_data = string_input.strip().replace(" ", "")
    result = []
    limit = len(string_data)
    offset = 0
    while offset < limit:
        token = next_token(string_data, offset, limit)
        # Infix parsing is eager, swap to prefix where possible
        if isinstance(token, Infix) and \
                token.lexeme in prefix_operators and \
                prefix_operators[token.lexeme].priority > token.priority and \
                (len(result) == 0 or result[-1] is left_parenthesis or isinstance(result[-1], Operator)):
            token = prefix_operators[token.lexeme]
        offset += len(token.lexeme)
        result.append(token)

    return result


def execute_ops(ops, args, condition):
    while ops and condition():
        operator = ops.pop()
        params = []
        #print(f"Operator: {operator}")
        for _ in range(operator.params):
            params.insert(0, args.pop().value)
        result = operator.executor(*params)
        args.append(Operand(lexeme=result,
                            value=result))
        #print(f"Operator: {operator} with {params}, result = {result}")


def evaluate_expression(string_input):
    tokens = parse_tokens(string_input)
    ops = []
    args = []
    # print(tokens)
    for token in tokens:
        if token is left_parenthesis:
            ops.append(token)
        elif token is right_parenthesis:
            execute_ops(ops, args, lambda: ops[-1] is not left_parenthesis)
            ops.pop()
        elif isinstance(token, Operand):
            args.append(token)
        elif isinstance(token, Infix):
            priority = token.priority
            execute_ops(
                ops, args, lambda: ops[-1] is not left_parenthesis and ops[-1].priority >= priority)
            ops.append(token)
        elif isinstance(token, Prefix):
            ops.append(token)
    execute_ops(ops, args, lambda: True)
    return args[-1] if len(args) == 1 else None


try:
    res = evaluate_expression(sys.stdin.readline())
    sys.stdout.write(f"{res.value:.2f}")
except Exception as e:
    # traceback.print_exc()
    sys.stdout.write("Invalid mathematical expression.")
sys.stdout.write("")
