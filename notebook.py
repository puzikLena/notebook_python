import datetime
from note import Note
from json import loads, dump

notes = []


def load_all_notes():
    notes.clear()
    with open('notes.json') as file:
        raw_data = file.read()
        raw_notes = loads(raw_data)
        for data in raw_notes:
            note = Note()
            note.from_dict(data)
            notes.append(note)


def read_note(note_id: int):
    if len(notes) == 0:
        print('Заметки еще не добавлены')
        return
    if 0 <= note_id < len(notes):
        print(f"Заметка #{note_id}")
        notes[note_id].print_note()
    else:
        print(f'Номер заметки должен быть от 0 до {len(notes) - 1}')


def add_note(title, value):
    note = Note()
    note.note_id = get_last_note_id() + 1
    note.title = title
    note.value = value
    note.changed_at = datetime.datetime.now()
    notes.append(note)
    write_notes()
    print(f'Заметка с номером {note.note_id} успешно добавлена')
    print('==============================================')


def update_note(note_id, note_title, note_value):
    if len(notes) == 0:
        print('Заметки еще не добавлены')
        return
    if 0 <= note_id < len(notes):
        note = notes[note_id]
        note.title = note_title
        note.value = note_value
        note.changed_at = datetime.datetime.now()
        write_notes()
        print(f'Заметка #{note_id} обновлена')
    else:
        print(f'Номер заметки должен быть от 0 до {len(notes) - 1}')


def delete_note(note_id):
    if len(notes) == 0:
        print('Заметки еще не добавлены')
        return
    if 0 <= note_id < len(notes):
        notes.remove(notes[note_id])
        write_notes()
        print(f'Заметка #{note_id} удалена')
    else:
        print(f'Номер заметки должен быть от 0 до {len(notes) - 1}')


def get_last_note_id() -> int:
    if len(notes) == 0:
        return 0
    return notes[len(notes) - 1].note_id


def write_notes():
    notes_data = []
    for note in notes:
        notes_data.append(note.to_dict())
    with open('notes.json', 'w') as file:
        dump(notes_data, file)
