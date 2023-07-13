import os

def run_affinity_script():
    try:
        os.system("python3 affinity.py")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта affinity.py: {e}")

def run_tvr_script():
    try:
        os.system("python3 tvr.py")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта tvr.py: {e}")

def run_reach_script():
    try:
        os.system("python3 reach.py")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта reach.py: {e}")

def run_positioning_script():
    try:
        os.system("python3 positioning.py")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта positioning.py: {e}")

def print_menu():
    print("Добро пожаловать в программу!")
    print("Выберите скрипт для запуска:\n")
    print("1. Affinity")
    print("2. TVR")
    print("3. Reach")
    print("4. Positioning")
    print("0. Выход")

def print_instructions():
    print("\nВведите номер скрипта, который вы хотите запустить.")
    print("Для выхода из программы введите 0.")

def main():
    # Словарь для хранения связи между номером скрипта и функцией
    scripts = {
        "1": run_affinity_script,
        "2": run_tvr_script,
        "3": run_reach_script,
        "4": run_positioning_script
    }

    while True:
        print_menu()
        print_instructions()
        choice = input("\nВведите номер скрипта: ")

        if choice in scripts:
            # Вызов функции из словаря по выбранному номеру скрипта
            script_func = scripts[choice]
            script_func()
        elif choice == "0":
            break
        else:
            print("\nНеверный ввод. Пожалуйста, выберите номер из меню.")

if __name__ == "__main__":
    main()
