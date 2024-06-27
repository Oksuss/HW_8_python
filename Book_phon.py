fileName = "phon.txt"
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt(fileName)
    while choice != 8:
        if choice == 1:  # 1.Отобразить весь справочник
            print_result(phone_book)
            print()
        elif choice == 2:  # 2.Найти абонента по фамилии
            last_name = str(input("Фамилия: "))
            print(find_by_lastname(phone_book, last_name))

        elif choice == 3:  # 3.Найти абонента по номеру телефона
            number = input("Номер телефона: ")
            if number.isdigit():
                print(find_by_number(phone_book, number))

        elif choice == 4:  # 4.Добавить абонента в справочник
            user_data = input("Введите данные - Фамилия,Имя,Телефон,Описание\n")  
            add_or_change_user(phone_book, user_data)
            write_txt(fileName, phone_book)
            print('Данные добавлены')

        elif choice == 5:  # 5.Удалить абонента по фамилии
            last_name = str(input("Фамилия: "))
            if delete_by_lastname(phone_book, last_name):
                print("Данные удалены")
          
        elif choice == 6:  # 6.Сохранить справочник
            write_txt(fileName, phone_book)
            print("Данные сохранены")

        elif choice == 7:  # 7. Скопировать данные в другой файл
            line_number = int(input("Введите номер строки для копирования: "))
            filename_destination = input("Введите имя файла назначения: ")
            copy_line_to_file(phone_book, line_number, filename_destination)
            print("Данные успешно скопированы.")

        choice = show_menu()
def show_menu():
    print(
        "Выберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Удалить абонента по фамилии\n"
        "6. Сохранить справочник\n"
        "7. Скопировать данные в другой файл\n"
        "8. Закончить работу"
    )
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(fileName, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            clean_record = {key: value.strip() for key, value in record.items()}
            if clean_record["Фамилия"].strip() != "":
                phone_book.append(clean_record)
    return phone_book

def write_txt(fileName, phone_book):
    with open(fileName, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s = s + v + ","
            phout.write(f"{s[:-1]}\n")

def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст")
    else: 
        print("Фамилия   ","Имя   ","Телефон   ","Описание   ")
    i = 0
    for item in phone_book:
        i = i + 1
        print(i, item["Фамилия"],item["Имя"],item["Телефон"],item["Описание"])

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            return phone_book[i]
    return "Не найден"

def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i].get("Телефон", "Нет такого номера") == number:
            return phone_book[i]
    return "Не найден"

def add_or_change_user(phone_book, user_data):
    fields = user_data.split(",")  
    fields = [item.strip() for item in fields] 
    print(f"\nДобавляем запись: {fields}")
    if len(fields) != 4 or not fields[2].isdigit():
        print("Неверный формат ввода данных.")
        return

    new_entry = dict(zip(["Фамилия", "Имя", "Телефон", "Описание"], fields))
    for i, entry in enumerate(phone_book):
        if entry["Фамилия"] == new_entry["Фамилия"]: 
            phone_book[i] = new_entry  
            return
    phone_book.append(new_entry)


def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            del phone_book[i]
            return True
    return False

def copy_line_to_file(phone_book, line_number, filename_destination):
    if 1 <= line_number <= len(phone_book):
        entry = phone_book[line_number - 1]
        with open(filename_destination, "a", encoding="utf-8") as file:
            file.write(
                f"{entry['Фамилия']},{entry['Имя']},{entry['Телефон']},{entry['Описание']}\n"
            )
    else:
        print("Неверный номер строки.")

work_with_phonebook()