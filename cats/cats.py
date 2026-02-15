
from pathlib import Path

def get_cats_info(file_path):
    # Якщо передано відносний шлях, шукаємо біля скрипта
    path = Path(file_path)
    if not path.is_absolute():
        script_dir = Path(__file__).parent
        path = script_dir / file_path
    
    cats = []

    try:
         # Використовуємо менеджер контексту для читання файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві пробіли та символи нового рядка
                line = line.strip()

                # Пропускаємо порожні рядки
                if not line:
                    continue
                # Розділяємо рядок на ID, ім'я та вік кота
                try:
                    cat_id, name, age = line.split(',')
                    cats.append({"id": cat_id, "name": name, "age": int(age)})
                    
                except ValueError:
                    print(f"Помилка: некоректний формат рядка '{line}'")
                    continue

        return cats
    
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        return []
    
    except PermissionError:
        print(f"Помилка: немає доступу до файлу '{path}'")
        return []
    
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return []

cats_info = get_cats_info("cats_data.txt")
print(cats_info)