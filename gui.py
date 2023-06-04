import functions
import PySimpleGUI as sg

label = sg.Text("Type in A to-do")
input_box = sg.InputText(tooltip ="Enter To-do", key="todo")
add_button = sg.Button("Add")
# add_action = sg.

window = sg.Window('My To-Do App',
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break




window.close()



