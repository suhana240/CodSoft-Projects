from prettytable import PrettyTable
import random
import time

class PasswordGenerator:
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
        self.x = PrettyTable()
        self.password_dict = {}

    def generate_passwords(self, no_of_passwords, password_length):
        count = 1
        while count <= no_of_passwords:
            password = ""
            for _ in range(password_length):
                password += random.choice(self.characters)
            self.password_dict[count] = password
            count += 1

    def display_passwords(self):
        self.x.field_names = ["Generated Passwords"]
        for key, value in self.password_dict.items():
            self.x.add_row([f"{key} | {value}"])
        print(self.x)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            [file.write(f"{i}----{j}\n") for i, j in self.password_dict.items()]

def main():
    print("\n*** Password Generator App ***")
    
    no_of_passwords = int(input("\nHow many passwords do you want to generate? "))
    password_length = int(input("\nEnter the length of each password: "))
    
    password_generator = PasswordGenerator()
    
    print("\nGenerating passwords...")
    password_generator.generate_passwords(no_of_passwords, password_length)
    
    print("\nGenerating entire list...")
    time.sleep(2)
    
    password_generator.display_passwords()
    
    filename = "password.txt"
    password_generator.save_to_file(filename)
    print(f"\nGenerated passwords have been saved to {filename}")

if __name__ == "__main__":
    main()