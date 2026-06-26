def calculate(op: str, a: float, b: float):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Ошибка: неизвестная операция"