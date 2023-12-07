from getpass import getpass
import itertools
from tools import time_to_execute



class PasswordCracker:
    def __init__(self):
        """
        Initialize a PasswordCracker object.

        Attributes:
        - password: The target password to be cracked.
        - weak_character_set: A set of characters for weak passwords.
        - character_set: A set of characters for strong passwords.
        - password_length: The length of the password.
        """
        self.password = None
        self.weak_character_set = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.character_set = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!$#@- "
        self.password_length = None


    def set_password(self):
        password = getpass("Enter a password: ")
        check_password = getpass("Enter the password again: ")

        if password != check_password:
            print("Passwords do not match. Please try again.")
            return

        self.password = password
        self.password_length = len(password)
        print("Password set successfully.")
    

    @time_to_execute
    def brute_force_password(self, difficulty=False):
        char_set = self.character_set if difficulty else self.weak_character_set

        for i, attempt in enumerate(itertools.product(char_set, repeat=self.password_length)):
            current_attempt = "".join(attempt)
            print(f"{i})=> {current_attempt}")

            if current_attempt == self.password:
                print(f"Password found: {current_attempt}")
                return

        print("Password not found.")


    @time_to_execute
    def brute_force_with_common_passwords(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                passwords = f.read().splitlines()
        except FileNotFoundError:
            print("File path is not correct")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return

        for i, password in enumerate(passwords):
            print(f"{i})=> {password}")
            if password == self.password:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found.")


    def check_password_strength(self):
        strength = 0

        # Length bonus
        length_bonus = min(len(self.password) // 2, 3)
        strength += length_bonus

        # Case sensitivity bonus
        if any(c.isupper() for c in self.password) and any(c.islower() for c in self.password):
            strength += 2

        # Digit presence bonus
        if any(c.isdigit() for c in self.password):
            strength += 2

        # Special character presence bonus
        if any(c in "!$#@-" for c in self.password):
            strength += 2

        # Strength classification
        if strength >= 7:
            return "Strong"
        elif 4 <= strength < 7:
            return "Medium"
        else:
            return "Weak"


    def delete_password(self):
        self.password = None
        print("Password deleted succesfully")


    def show_menu(self):
        print("""
        ╔══════════════════════════════╗
        ║    Welcome to PassCracker    ║
        ╚══════════════════════════════╝

        Please choose an option:

        1. Set a New Password
        2. Brute Force Attack
        3. Brute Force with Common Passwords
        4. Check Password Strength
        5. Delete the Password
        m. Show the menu
        q. Quit

        Enter the corresponding number or 'q' to quit:

        """)