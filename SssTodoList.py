from prettytable import PrettyTable

class ToDoListManager:
    def __init__(self):
        self.my_todo_list = []
        self.x = PrettyTable()
        self.x.field_names = ["Item Names"]

    def my_list(self):
        self.x.clear_rows()
        for i in self.my_todo_list:
            self.x.add_row([i])
        print(self.x.get_string(title="TO DO List"))

    def add_todo(self):
        new_todo = input("\nEnter your new TO DO: ").lower()
        print(f"\nYour current TO DO is {new_todo}.")
        self.my_todo_list.append(new_todo)

    def delete_todo(self):
        item_name = input("\nEnter the item you want to delete: ").lower()
        try:
            if item_name in self.my_todo_list:
                choice = input(f"Are you sure to delete {item_name} from your TODO list? (Y/N): ").lower()
                if choice == "y":
                    self.my_todo_list.remove(item_name)
                    print("Your updated TO-DO List:")
                    self.my_list()
                else:
                    print("Item not deleted.")
            else:
                print("Item not found.")
        except Exception:
            print("Something went wrong.")

    def update_todo(self):
        item_name = input("\nEnter the item you want to update: ").lower()
        try:
            if item_name in self.my_todo_list:
                choice = input(f"Are you sure to update {item_name} from your TODO list? (Y/N): ").lower()
                if choice == "y":
                    update_item = input(f"Enter a name you want to update {item_name} with: ").lower()
                    index = self.my_todo_list.index(item_name)
                    self.my_todo_list[index] = update_item
                    print("Your updated TO-DO List:")
                    self.my_list()
                else:
                    print("Item not updated.")
            else:
                print("Item not found.")
        except Exception:
            print("Something went wrong.")

    def exit_program(self):
        ask_user = input("\nAre you sure you want to exit? (Y/N): ").lower()
        if ask_user == "y":
            return True
        return False

    def process_input(self, user_input):
        switch = {
            "a": self.add_todo,
            "d": self.delete_todo,
            "u": self.update_todo,
            "e": self.exit_program,
            "l": self.my_list,
            "": lambda: print("Please enter something."),
        }
        return switch.get(user_input, lambda: print("Enter a valid value."))()

    def run(self):
        print("\n*** My TO-DO List. ***")
        instructions = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to check your TO-DO."
        print(instructions)

        running = True
        while running:
            user_input = input("\nWhat do you want to do? (A,D,U,E,L): ").lower()
            running = not self.process_input(user_input)

if __name__ == "__main__":
    todo_manager = ToDoListManager()
    todo_manager.run()