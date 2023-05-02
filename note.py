import datetime


class Note:
    title = ""
    value = ""
    changed_at = datetime.datetime.now()

    def __init__(self, note_id):
        self.note_id = note_id

    def to_dict(self) -> dict:
        return {
            'id': self.note_id,
            'title': self.title,
            'value': self.value,
            'changed_at': self.changed_at,
        }
