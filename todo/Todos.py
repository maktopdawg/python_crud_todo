import csv
from GenerateID import generate_id

# ADD method to change status to incomplete too

class Todos:
    def __init__(self) -> None:
        self.todos = []
        self.filename = './todo/todos.csv'
        self.completed = False


    def add_todo(self,todo: str):
        status = 'COMPLETE ✅' if self.completed else 'INCOMPLETE ⏳'
        format_todo = [generate_id(), todo, status]
        with open(self.filename, 'a') as filename:
            filename_writer = csv.writer(filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            filename_writer.writerow(format_todo)
            print('Todo created successfully')


    def view_all_todos(self):
        count = 0
        with open(self.filename) as filename:
            reader = csv.reader(filename)
            for todo in reader:
                print(f'ID: {todo[0]} - {todo[1]} - {todo[2]}')
    

    def complete_todo(self, id):
        with open(self.filename, 'r') as filename:
            # reader = csv.reader(filename)
            reader = list(csv.reader(filename))

            found = False
            for todo in reader:
                if todo[0].strip() == id.strip():
                    todo[-1] = 'COMPLETE ✅'
                    found = True
                    break
            
            if found:
                # Write the updated data back to the CSV file
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(reader)
                    print('Data updated successfully')
            else:
                print(f'Todo with ID {id} not found')
                


    def delete_all_todos(self):
        with open(self.filename) as file:
            reader = list(csv.reader(file))
            reader = []

        with open(self.filename, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(reader)
            print('Todos cleared')
            

    def update_todo(self,id):
        with open(self.filename, 'r') as file:
            reader = list(csv.reader(file))
            found = False
            for todo in reader:
                if todo[0].strip() == id.strip():
                    found = True
                    update = input('Update todo: ')
                    todo[1] = update
                    break

            if found:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(reader)
                    print('Data updated successfully')
            else:
                print(f'Todo with ID {id} not found')


    def delete_todo(self,id):
        updated_list = []
        with open(self.filename, newline="") as file:
            reader = csv.reader(file)
            for todo in reader:
                if todo[0] != id:
                    updated_list.append(todo)

        with open(self.filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_list)
            print('Todo has been deleted')


    def show_complete(self):
        with open(self.filename) as filename:
            reader = csv.reader(filename)
            for todo in reader:
                if todo[-1] == 'COMPLETE ✅':
                    print(f'ID: {todo[0]} - {todo[1]} - {todo[2]}')
            
    
    def show_incomplete(self):
        with open(self.filename) as filename:
            reader = csv.reader(filename)
            for todo in reader:
                if todo[-1] == 'INCOMPLETE ⏳':
                    print(f'ID: {todo[0]} - {todo[1]} - {todo[2]}')


todos = Todos()


while True:
    action = input('What do you wanna do? (create/view_all/complete/clear/update/delete/show_complete/show_incomplete): ')
    if action == 'create'.lower():
        todo = input('Create new todo item: ').capitalize()
        todos.add_todo(todo)


    elif action == 'view_all':
        todos.view_all_todos()


    elif action == 'complete':
        id = input('Enter todo ID you want to complete: ')
        todos.complete_todo(id)


    elif action == 'clear':
        todos.delete_all_todos()


    elif action == 'update':
        id = input('Enter todo ID you want to update: ')
        todos.update_todo(id)


    elif action == 'delete':
        id = input('Enter todo ID you want to delete: ')
        todos.delete_todo(id)


    elif action == 'show_complete':
        todos.show_complete()

    elif action == 'show_incomplete':
        todos.show_incomplete()