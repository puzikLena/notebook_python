import datetime

import notebook


def main():
    notebook.load_all_notes()
    show_main_actions()


def show_main_actions():
    print_main_actions()
    process_main_action(input("Введите букву для действия:\n> "))


def print_main_actions():
    print("Добро пожаловать в приложение \"Заметки\"")
    print("Для работы с программой введите букву для действия (на английском языке)")
    print("C - Создать заметку")
    print("R - Вывести заметку")
    print("U - Обновить заметку")
    print("D - Удалить заметку")


def process_main_action(letter):
    if letter == 'C' or letter == 'c':
        create_note_action()
    elif letter == 'R' or letter == 'r':
        read_note_action()
    elif letter == 'U' or letter == 'u':
        update_note_action()
    elif letter == 'D' or letter == 'd':
        delete_note_action()
    else:
        print("Команда не распознана, повторите\n\n")
        show_main_actions()


def create_note_action():
    print('=========================')
    print('Создание заметки')

    note_title = input('Введите название заметки:\n>').strip()
    if len(note_title) == 0:
        print('Название заметки не должно быть пустым!!!')
        create_note_action()

    note_value = input('Введите текст заметки:\n>').strip()
    if len(note_value) == 0:
        print('Заметка не должна быть пустой!!!')
        create_note_action()

    notebook.add_note(note_title, note_value)
    show_main_actions()


def read_note_action():
    pass


def update_note_action():
    pass


def delete_note_action():
    pass


if __name__ == '__main__':
    main()
