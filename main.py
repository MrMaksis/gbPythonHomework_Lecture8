import socket
def show_data(filename):
    print("\nID | ФИО | Телефон")

    with open(filename, "r", encoding="utf-8") as data:
        print("".join(data.readlines()))
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "a", encoding="utf-8") as data:
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        new_line = f"{len(data.readlines())+1} | {fio} | {phone_number}\n"
        data.write(new_line)
        print(f"Добавлена запись : {new_line}")

# Изменяет информацию из файла
def edit_data(filename):
    print("\nID | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.readlines()

    [print(f"{i+1} | {line}") for i, line in enumerate(tel_book)]
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    elements = tel_book[index_delete_data].split(" | ")
    fio = input("Введите ФИО: ") or elements[1]
    phone = input("Введите номер телефона: ") or elements[2]
    edited_line = f"{index_delete_data+1} | {fio} | {phone}\n"
    tel_book[index_delete_data] = edited_line

    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(tel_book)
    print(f"Запись - {elements}, изменена на - {edited_line}")

# Удаляет информацию из файла
def delete_data(filename):
    print("\nID | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.readlines()

    [print(f"{i+1} | {line}") for i, line in enumerate(tel_book)]
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    del_tel_book_lines = tel_book[index_delete_data]

    del tel_book[index_delete_data]

    with open(filename, "w", encoding='utf-8') as data:
        data.writelines(tel_book)
    print(f"Удалена запись: {del_tel_book_lines}")
def main():
    file_tel = "tel.txt"

    # Создает файл если его нет в папке
    open(file_tel, "a").close()

    while True:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экпорт данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = input("Действие: ")
        if action == '1':
            show_data(file_tel)
        elif action == '2':
            export_data(file_tel)
        elif action == '3':
            edit_data(file_tel)
        elif action == '4':
            delete_data(file_tel)
        elif action == '0':
            break

    print(f"Всего доброго! {socket.gethostname()}")

if __name__ == "__main__":
    main()
