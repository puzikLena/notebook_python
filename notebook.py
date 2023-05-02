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
    print(f"Заметка #{note_id}")
    notes[note_id].print_note()


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


def update_note(note: Note):
    pass


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
