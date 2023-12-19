from Phyton.NotesMVC.controllers.NotesController import NotesController
from Phyton.NotesMVC.models.NotesModel import NotesModel
from Phyton.NotesMVC.views.NotesView import NotesView


if __name__ == "__main__":
    model = NotesModel("../NotesMVC/notes.json")
    view = NotesView()
    controller = NotesController(model, view)

    commands = {
        "add": controller.add_note,
        "read": controller.read_notes,
        "edit": controller.edit_note,
        "delete": controller.delete_note,
        "filter": controller.filter_notes_by_date,
        "find": controller.find_by_id,
    }

    command = ""
    while command != "exit":
        print()
        print("Список доступных команд:")
        print("1. add - добавить заметку")
        print("2. read - прочитать все заметки")
        print("3. edit - отредактировать заметку")
        print("4. delete - удалить заметку")
        print("5. filter - отфильтровать заметки по дате")
        print("6. find - найти по ID заметки")
        print("7. exit - выйти из приложения")

        command = input("Введите команду: ")
        print()

        if command in commands:
            commands[command]()
        elif command != "exit":
            print("Неправильная команда. Попробуйте снова.")
