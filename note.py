from datetime import datetime


class Note:
    note_id = 0
    title = ""
    value = ""
    changed_at = datetime.now()

    def from_dict(self, data):
        self.note_id = data['id']
        self.title = data['title']
        self.value = data['value']
        self.changed_at = datetime.strptime(data['changed_at'], '%d.%m.%Y %H:%M')

    def to_dict(self):
        return {
            'id': self.note_id,
            'title': self.title,
            'value': self.value,
            'changed_at': datetime.strftime(self.changed_at, '%d.%m.%Y %H:%M'),
        }

    def print_note(self):
        print(f"Заголовок: {self.title}\nТекст заметки: {self.value}\nДата изменения: {datetime.strftime(self.changed_at, '%d.%m.%Y %H:%M')}")
