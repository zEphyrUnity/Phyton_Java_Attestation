class NotesView:
    def print_note(self, note):
        print(f"-------------------------")
        print(f"ID: {note.id}")
        print(f"Заголовок: {note.title}")
        print(f"Тело: {note.body}")
        print(f"Время создания: {note.timestamp}")

    def print_notes(self, notes):
        for note in notes:
            self.print_note(note)
