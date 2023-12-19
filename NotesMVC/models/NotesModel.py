from datetime import datetime
from Phyton.NotesMVC.models.Note import Note

import json
import os


class NotesModel:
    def __init__(self, notes_file):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                try:
                    notes_data = json.load(file)
                    return [Note(**note) for note in notes_data]
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_notes(self):
        with open(self.notes_file, "w") as file:
            json.dump([note.__dict__ for note in self.notes], file)

    def add_note(self, title, body):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(len(self.notes) + 1, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return True
        return False

    def find_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def filter_notes_by_date(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return [note for note in self.notes if datetime.strptime(note.timestamp, "%Y-%m-%d %H:%M:%S").date() == date]
