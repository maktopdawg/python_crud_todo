import csv
from GenerateID import generate_id

# ADD method to change status to incomplete too

class Todos:
    def __init__(self) -> None:
        self.todos = []
        self.filename = './todo/todos.csv'
        self.completed = False
        self.lines = '='*100

    def menu(self):
        '''
            This function prints the menu option
        '''

        print(f"""
{self.lines}
    OPTIONS\n
    - To Show Menu - (show_menu)
    - Create New Task - (create)
    - View Existing Tasks - (view_all)
    - Complete A Task - (complete)
    - To Change Completed Task Status Back To Incomplete - (incomplete)
    - Clear All Exisiting Tasks - (clear)
    - Delete A Task - (delete)
    - Show All Completed Tasks - (show_complete)
    - Show All Incomplete Tasks - (show_incomplete)
    - To Quit Game - (quit)
{self.lines}
""")

    def update_csv(self, reader, message: str):
        '''
            This function updates the csv file storing our data.
            It writes what is parsed in the reader parameter to the file, updating it's contents.
            Thereafter it prints the a message which is enter by the user on the terminal
        '''

        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
            print(f"{self.lines}\n\n    {message}\n\n{self.lines}")


    def add_todo(self, todo: str):
        '''
            This function takes an argument of a parameter and appends it to the file.
        '''

        status = 'COMPLETE ✅' if self.completed else 'INCOMPLETE ⏳'
        format_todo = [generate_id(), todo, status]
        with open(self.filename, 'a') as filename:
            filename_writer = csv.writer(filename, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            filename_writer.writerow(format_todo)
            print(f"\n{self.lines}\n\n    Todo created successfully\n\n{self.lines}")


    def view_all_todos(self):
        '''
            This function first counts the items in the file name and stores the count in a variable called count.
            And if the count is not equal to zero it will open the files and print everything out in the specified format.
        '''

        count = 0
        with open(self.filename) as file:
            reader = csv.reader(file)
            for todo in reader:
                count += 1

        if count != 0:
            with open(self.filename) as filename:
                reader = csv.reader(filename)
                print(f"\n{self.lines}\n    You have {count} task/s:\n")
                for todo in reader:
                    print(f"    -> ID: {todo[0]} - {todo[1]} - {todo[2]}")
                print(f"\n{self.lines}")
        else:
            print(f"\n{self.lines}\n    You have no tasks scheduled\n    (Run 'create' to add new task)\n{self.lines}\n")
    

    def complete_todo(self, id):
        '''
            This function takes an id as a paramter.
            Proceeds to read the file and look for an task with the same id as the one specified.
            And if found it'll will change the status to COMPLETE ✅
        '''

        with open(self.filename, 'r') as filename:
            reader = list(csv.reader(filename))

            found = False
            for todo in reader:
                if todo[0].strip() == id.strip():
                    todo[-1] = 'COMPLETE ✅'
                    found = True
                    break
            
            if found:
                self.update_csv(reader,'Todo completed!')
            else:
                print(f"{self.lines}\n    Todo with ID '{id}' not found\n{self.lines}")


    def incomplete_todo(self, id):
        '''
            This function takes an id as a paramter.
            Proceeds to read the file and look for an task with the same id as the one specified.
            And if found it'll will change the status to INCOMPLETE ⏳
        '''

        with open(self.filename, 'r') as filename:
            reader = list(csv.reader(filename))

            found = False
            for todo in reader:
                if todo[0].strip() == id.strip():
                    todo[-1] = 'INCOMPLETE ⏳'
                    found = True
                    break
            
            if found:
                self.update_csv(reader,'Todo status changed back to incompleted!')
            else:
                print(f"{self.lines}\n    Todo with ID '{id}' not found\n{self.lines}")
                

    def delete_all_todos(self):
        with open(self.filename) as file:
            reader = list(csv.reader(file))
            reader = []

        self.update_csv(reader, 'All todos cleared')
            

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
                self.update_csv(reader, 'Todo updated successfully')
            else:
                print(f"{self.lines}\n    Todo with ID {id} not found\n{self.lines}")


    def delete_todo(self,id):
        updated_list = []
        with open(self.filename, newline="") as file:
            reader = csv.reader(file)
            for todo in reader:
                if todo[0] != id:
                    updated_list.append(todo)

        self.update_csv(updated_list, 'Todo has been removed successfully!')


    def show_complete(self):
        count = 0
        status = 'COMPLETE ✅'

        with open(self.filename) as file:
            reader = csv.reader(file)
            for todo in reader:
                if todo[-1] == status:
                    count += 1

        with open(self.filename) as filename:
            reader = csv.reader(filename)
            print(f"\n{self.lines}\n    You have {count} completed task/s:\n")
            for todo in reader:
                if todo[-1] == status:
                    print(f"    -> ID: {todo[0]} - {todo[1]} - {todo[2]}")
            print(f"\n{self.lines}")
            
    
    def show_incomplete(self):
        count = 0
        status = 'INCOMPLETE ⏳'

        with open(self.filename) as file:
            reader = csv.reader(file)
            for todo in reader:
                if todo[-1] == status:
                    count += 1

        with open(self.filename) as filename:
            reader = csv.reader(filename)
            print(f"\n{self.lines}\n    You have {count} incompleted task/s:\n")
            for todo in reader:
                if todo[-1] == status:
                    print(f"    -> ID: {todo[0]} - {todo[1]} - {todo[2]}")
            print(f"\n{self.lines}")


    def run_program(self):
        action = input('\nWhat Do You Wish To Do: ')
        while True:
            match action:
                case 'show_menu':
                    self.menu()
                    self.run_program()

                case 'create':
                    task = input('Create New Todo: ')
                    self.add_todo(task)
                    self.run_program()

                case 'view_all':
                    self.view_all_todos()
                    self.run_program()

                case 'complete':
                    id = input('Enter task ID you wish to complete: ')
                    self.complete_todo(id)
                    self.run_program()

                case 'incomplete':
                    id = input('Enter task ID you wish to change to incomplete: ')
                    self.incomplete_todo(id)
                    self.run_program()

                case 'clear':
                    self.delete_all_todos()
                    self.run_program()

                case 'update':
                    id = input(f"{self.lines}\n    Enter task ID you wish to update: ")
                    self.update_todo(id)
                    self.run_program()

                case 'delete':
                    id = input('Enter task ID you wish to remove: ')
                    self.delete_todo(id)
                    self.run_program()

                case 'show_complete':
                    self.show_complete()
                    self.run_program()

                case 'show_incomplete':
                    self.show_incomplete()
                    self.run_program()

                case 'quit':
                    break
                
                case _ :
                    print(f"{self.lines}\n    Invalid Command\n{self.lines}")
                    self.run_program()