def parse_command(user_input: str):
    parts = user_input.strip().split()
    if len(parts) != 3:
        return None, "Ошибка: нужно ввести ровно 3 части: операция число1 число2"
    op, *nums = parts
    if op not in ('add', 'sub', 'mul', 'div'):
        return None, f"Ошибка: неизвестная операция '{op}'. Допустимые: add, sub, mul, div"
    try:
        a = float(nums[0])
        b = float(nums[1])
    except ValueError:
        return None, "Ошибка: оба аргумента должны быть числами"
    return (op, a, b), None