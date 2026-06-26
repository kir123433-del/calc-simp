from parcer import parse_command
from operations import calculate
from history import History

def main():
    hist = History()
    hist.load('history.json')
    print("Консольный калькулятор. Доступные команды:")
    print("  add, sub, mul, div <число1> <число2>")
    print("  history  - показать историю")
    print("  exit     - выход")
    print("Введите команду:")

    while True:
        try:
            user_input = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nЗавершение работы.")
            break

        if not user_input:
            continue

        if user_input.lower() == 'exit':
            hist.save('history.json')
            print("До свидания!")
            break

        if user_input.lower() == 'history':
            entries = hist.show()
            if entries:
                for i, entry in enumerate(entries, 1):
                    print(f"{i}. {entry}")
            else:
                print("История пуста.")
            continue

        parsed, error = parse_command(user_input)
        if error:
            print(error)
            continue

        op, a, b = parsed
        result = calculate(op, a, b)
        if isinstance(result, str) and result.startswith("Ошибка"):
            print(result)
            entry = f"{op} {a} {b} = {result}"
        else:
            entry = f"{op} {a} {b} = {result}"
            print(f"Результат: {result}")

        hist.add(entry)

if __name__ == "__main__":
    main()