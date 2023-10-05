'''
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
'''

import os.path


def user_action(phonebook):
    while True:
        print('Телефонный справочник приветствует Вас!!\n1 - Просмотр всех контактов\n2 - Найти контакт\n\
3 - Добавить контакт\n4 - Изменить контакт\n5 - Удалить контакт\n0 - Выйти из приложения\n')
        user_choice = input('Введите команду: ')
        if user_choice == '1':
            print_phonebook(phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_list(phonebook)
            find_subscriber(contact_list)
        elif user_choice == '3':
            add_new_subscriber(phonebook)
        elif user_choice == '4':
            change_phonebook(phonebook)
        elif user_choice == '5':
            delete_contacts(phonebook)
        elif user_choice == '0':
            print('Гуд бай!')
            break
        else:
            print('Некорректный выбор действия! Повторите!')
            print()
            continue


def print_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_list(file_name))
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def find_parameters():  # параметры поиска
    print('Как будем выполнять поиск?')
    print('1 - По фамилии\n2 - По имени\n3 - По отчеству\n4 - По номеру телефона\n0 - Не хочу искать!\n')
    print()
    search_field = input('Введите поле для поиска: ')
    search_value = None
    while True:
        if search_field == '1':
            search_value = input('Введите фамилию для поиска: ')
            print()
            break
        elif search_field == '2':
            search_value = input('Введите имя для поиска: ')
            print()
            break
        elif search_field == '3':
            search_value = input('Введите отчество для поиска: ')
            print()
            break
        elif search_field == '4':
            search_value = input('Введите номер для поиска: ')
            print()
            break
        elif search_field == '0':
            print()
            break
        else:
            print('Некорректный выбор поля поиска! Повторите!')
            print()
            continue
    return search_field, search_value


def find_subscriber(contact_list):  # поиск абонентов
    search_field, search_value = find_parameters()
    if search_field == 0:
        print('Отказ от поиска!')
        return
    found_contacts = []
    for i in range(len(contact_list)):
        list_new = list(contact_list[i])
        if list_new[int(search_field) - 1] == search_value:
            found_contacts.append(list_new)
    if len(found_contacts) == 0:
        print('Абонент не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_subscriber():  # вводим данные нового абонента
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, patronymic, phone_number


def add_new_subscriber(file_name):  # добавляем нового абонента
    info = ' '.join(get_new_subscriber())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    print()


def change_phonebook(file_name):  # изменение данных
    contact_list = sorted(list(read_file_to_list(file_name)))
    print_contacts(contact_list)
    number_of_contact = int(input('Введите номер контакта который хотите изменить (0 ничего не изменять): '))
    if number_of_contact == 0 or len(contact_list) < number_of_contact:
        print('Отказ от операции либо номер превышает количество абонентов в базе!')
        print(number_of_contact, len(contact_list))
        return
    print()
    print(f'Меняем абонента - {contact_list[number_of_contact - 1]}')
    new_list = list(contact_list[number_of_contact - 1])
    print('Изменение контакта!')
    print('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - Номер телефона\n0 - Ничего не меняем\n')
    print()
    field = input('Выберите номер поля для изменений: ')
    if field == '1':
        number_of_change = input('Введите новую фамилию: ')
    elif field == '2':
        number_of_change = input('Введите новое имя: ')
    elif field == '3':
        number_of_change = input('Введите новое отчество: ')
    elif field == '4':
        number_of_change = input('Введите новый телефон: ')
    elif field == '0':
        print()
        return
    new_list[int(field) - 1] = number_of_change
    contact_list[number_of_contact - 1] = new_list
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print()
    print('Измененный справочник!')
    print_phonebook(file_name)


def delete_contacts(file_name):
    contact_list = sorted(read_file_to_list(file_name))
    print_contacts(contact_list)
    number_of_del = int(input('Введите номер контакта который хотите удалить (0 ничего не удалять): '))
    if number_of_del == 0 or len(contact_list) < number_of_del:
        print('Отказ от операции либо номер превышает количество абонентов в базе!')
        print()
        return
    contact_list.pop(number_of_del - 1)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print()


def read_file_to_list(file_name):  # считываем Phonebook.txt в массив
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def print_contacts(contact_list):  # вывод на консоль
    for i in range(len(contact_list)):
        list_out = list(contact_list[i])
        print("{:<4}".format(i + 1), "{:<12}".format(list_out[0]), "{:<12}".format(list_out[1]),
              "{:<12}".format(list_out[2]), "{:<12}".format(list_out[3]))
    print()


filename = 'Phonebook.txt'
if not os.path.isfile(filename):
    with open(filename, 'w', encoding='UTF-8') as data:
        data.write(' Фамилия Имя Отчество Телефон\n')
user_action(filename)
