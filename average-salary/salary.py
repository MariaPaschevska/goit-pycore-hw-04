from pathlib import Path

# Отримуємо директорію, де знаходиться скрипт
script_dir = Path(__file__).parent

# Створення файлу для тестування
def create_test_file():
    # Створюємо шлях до файлу біля скрипта
    test_file_path = script_dir / "salary_file.txt"
    
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write("Ann Oniks,7000\n")
        file.write("Serhi Lim,5000\n")
        file.write("Ivan Kotu,1800\n")
    
    return test_file_path

def total_salary(file_path):
    file_path = script_dir / file_path
    
    try:
        total = 0
        count = 0
        # Використовуємо менеджер контексту для читання файлу
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві пробіли та символи нового рядка
                line = line.strip()

                # Пропускаємо порожні рядки
                if not line:
                    continue
                # Розділяємо рядок на ім'я та зарплату
                try:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    
                    total += salary
                    count += 1
                    
                except ValueError:
                    print(f"Помилка: некоректний формат рядка '{line}'")
                    continue

        # Перевіряємо, чи є дані у файлі
        if count == 0:
            print("Файл порожній або не містить коректних даних")
            return (0, 0)
        
        # Обчислюємо середню зарплату
        average = total / count

        return (int(total), int(average))

    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено")
        return (0, 0)
    
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return (0, 0)


# Створити файл і протестувати
file_path = create_test_file()
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")