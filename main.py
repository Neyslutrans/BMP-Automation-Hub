import os
import platform

def run_script(script_name):
    try:
        if platform.system() == "Windows":
            os.system(f"python {script_name}")
        elif platform.system() == "Darwin":  # macOS
            os.system(f"python3 {script_name}")
        elif platform.system() == "Linux":  # Linux
            os.system(f"python3 {script_name}")
        else:
            print(f"Ошибка: Неподдерживаемая операционная система")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта {script_name}: {e}")

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
    # Словарь для хранения связи между номером скрипта и именем файла
    scripts = {
        "1": "affinity.py",
        "2": "tvr.py",
        "3": "reach.py",
        "4": "positioning.py"
    }

    while True:
        print_menu()
        print_instructions()
        choice = input("\nВведите номер скрипта: ")

        if choice in scripts:
            # Запуск выбранного скрипта
            script_name = scripts[choice]
            run_script(script_name)
        elif choice == "0":
            break
        else:
            print("\nНеверный ввод. Пожалуйста, выберите номер из меню.")

if __name__ == "__main__":
    main()
