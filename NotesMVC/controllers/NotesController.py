class NotesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        self.model.add_note(title, body)
        print("Заметка успешно сохранена")

    def read_notes(self):
        self.view.print_notes(self.model.notes)

    def delete_note(self):
        note_id = int(input("Введите ID заметки: "))
        if self.model.delete_note(note_id):
            print(f"Заметка с ID {note_id} успешно удалена.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def edit_note(self):
        note_id = int(input("Введите ID заметки: "))
        new_title = input("Введите новый заголовок заметки: ")
        new_body = input("Введите новое тело заметки: ")
        if self.model.edit_note(note_id, new_title, new_body):
            print(f"Заметка с ID {note_id} успешно отредактирована.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def find_by_id(self):
        note_id = int(input("Введите номер заметки: "))
        note = self.model.find_by_id(note_id)
        if note:
            self.view.print_note(note)
        else:
            print("Заметка с укзаным ID не найдена")

    def filter_notes_by_date(self):
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        filtered_notes = self.model.filter_notes_by_date(date_str)
        if filtered_notes:
            self.view.print_notes(filtered_notes)
        else:
            print("Заметки с указанной датой не найдены.")