from note import Note
from json import loads, dumps

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


def write_note(note: Note):
    pass


def update_note(note: Note):
    pass
