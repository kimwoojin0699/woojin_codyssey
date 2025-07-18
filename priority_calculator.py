def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b

def precedence(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def apply_op(operators, values):
    op = operators.pop()
    right = values.pop()
    left = values.pop()
    if op == '+':
        values.append(add(left, right))
    elif op == '-':
        values.append(subtract(left, right))
    elif op == '*':
        values.append(multiply(left, right))
    elif op == '/':
        try:
            values.append(divide(left, right))
        except ZeroDivisionError:
            raise

def calculate(tokens):
    values = []
    operators = []
    i = 0
    n = len(tokens)

    while i < n:
        token = tokens[i]

        if token == '(':
            # Find matching ')'
            count = 1
            j = i + 1
            while j < n and count > 0:
                if tokens[j] == '(':
                    count += 1
                elif tokens[j] == ')':
                    count -= 1
                j += 1
            if count != 0:
                # 괄호 짝 맞지 않음
                raise ValueError("Invalid input.")
            # 재귀 계산
            val = calculate(tokens[i+1:j-1])
            values.append(val)
            i = j  # 괄호 끝 다음 토큰으로 이동
            continue

        elif token.isdigit() or (token.count('.') == 1 and token.replace('.', '').isdigit()):
            # 숫자 처리
            values.append(float(token))
        elif token in '+-*/':
            # 연산자 처리, 우선순위 적용
            while (operators and precedence(operators[-1]) >= precedence(token)):
                apply_op(operators, values)
            operators.append(token)
        else:
            # 숫자도 연산자도 아니면 에러
            raise ValueError("Invalid input.")
        i += 1

    # 남은 연산 처리
    while operators:
        apply_op(operators, values)

    if len(values) != 1:
        raise ValueError("Invalid input.")

    return values[0]

def main():
    expr = input()
    tokens = expr.strip().split()

    try:
        result = calculate(tokens)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception:
        print("Invalid input.")

if __name__ == "__main__":
    main()
