import notebook


def main():
    notebook.load_all_notes()
    print("Добро пожаловать в приложение \"Заметки\"")
    show_main_actions()


def show_main_actions():
    print_main_actions()
    process_main_action(input("Введите букву для действия:\n>"))


def print_main_actions():
    print("=======================")
    print("Для работы с программой введите букву для действия (на английском языке)")
    print("C - Создать заметку")
    print("R - Вывести заметку")
    print("U - Обновить заметку")
    print("D - Удалить заметку\n")
    print("Q - Выход")


def process_main_action(letter):
    if letter == 'C' or letter == 'c':
        create_note_action()
    elif letter == 'R' or letter == 'r':
        read_note_action()
    elif letter == 'U' or letter == 'u':
        update_note_action()
    elif letter == 'D' or letter == 'd':
        delete_note_action()
    elif letter == 'Q' or letter == 'q':
        exit()
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
    print('=========================')
    print('Чтение заметки')

    note_id_text = input('Введите номер заметки для чтения:\n>')

    try:
        note_id = int(note_id_text)
        notebook.read_note(note_id)
        show_main_actions()
    except ValueError:
        print('Введите корректное число')
        read_note_action()


def update_note_action():
    print('=========================')
    print('Обновление заметки')

    note_id_text = input('Введите номер заметки для обновления:\n>')

    try:
        note_id = int(note_id_text)
        note_title = input('Введите новое название заметки:\n>')
        note_value = input('Введите новый текст заметки:\n>')
        notebook.update_note(note_id, note_title, note_value)
        show_main_actions()
    except ValueError:
        print('Введите корректное число')
        read_note_action()


def delete_note_action():
    print('=========================')
    print('Удаление заметки')

    note_id_text = input('Введите номер заметки для удаления:\n>')

    try:
        note_id = int(note_id_text)
        notebook.delete_note(note_id)
        show_main_actions()
    except ValueError:
        print('Введите корректное число\n')
        read_note_action()


if __name__ == '__main__':
    main()
