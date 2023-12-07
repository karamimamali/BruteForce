## Password Cracker Documentation:

Overview
The Password Cracker is a Python program designed to demonstrate various password-cracking techniques. It includes functionality to set, delete, and check the strength of a password. Additionally, it implements two brute-force methods to attempt to crack a given password.



# The design and implementation details of your code.
The project consists of three parts. In main.py, it uses the PasswordCracker class to encapsulate all the methods, making our project modular. run.py is where our GUI logic is implemented, and user inputs are checked here. In tools.py, we store additional tools; in our case, the time_to_execute decorator is defined here.


# 1 main.py Methods

# 1.1 __init__()
*   Initialize a PasswordCracker object.

    Attributes:
    - password: The target password to be cracked.
    - weak_character_set: A set of characters for weak passwords.
    - character_set: A set of characters for strong passwords.
    - password_length: The length of the password.

# 1.2 set_password()
*   Set a new password after prompting the user for input.

# 1.3 brute_force_password()
*   Attempt to brute force the password using the specified character set.

    Parameters:
    - difficulty (bool): If True, use the strong character set; otherwise, use the weak character set.

# 1.4 brute_force_with_common_passwords()
*   Attempt to brute force the password using a list of common passwords from a file.

    Parameters:
    - path (str): The path to the file containing common passwords.

# 1.5 check_password_strength()
*   Check the strength of the set password based on various criteria.

    Returns:
    - str: The strength classification of the password ('Weak', 'Medium', or 'Strong').

# 1.6 delete_password()
*   Delete the currently set password.

# 1.7 show_menu()
*   Display the main menu for the password cracker application.


# tools.py 
# time_to_execute()
*   A decorator that measures the execution time of a function.

    Parameters:
    - func (callable): The function to be measured.

    Returns:
    - callable: The wrapped function.



# 2. Time Complexity Analysis
* brute_force_password:
    The time complexity of this function is O(N^M), where N is the size of the character set and M is the length of the password.
    itertools.product generates all possible combinations of characters from the character set with repetition allowed, resulting in N^M combinations.

* brute_force_with_common_passwords:
    The time complexity of this function is O(N * M), where N is the number of passwords in the file, and M is the length of the password.
    It iterates through each password in the file, and for each password, it performs a comparison operation with the target password of length M.


# 3- Results of testing with different types of passwords.

For brute force methods without a common.txt file, the runtime depends on the speed of your computer and the strongness of your password. With a common.txt file, it is easier to identify common passwords compared to a normal brute force. However, for more complex passwords, there is no alternative but to resort to a straightforward brute force approach.


password => 11111111 , time = 0.0326 seconds

password => 12345678 , time = 0.0000 seconds

password => hello123 , time = 0.2605 seconds

password => 10101010 , time = 0.4515 seconds

password => 12112005 , time = 0.7194 seconds
 



# 4- Discussion on password strength and security considerations.

 # 4.1 Password Strength Criteria
Length: The password should be at least 8 characters long.
Character Types: A mix of uppercase, lowercase, digits, and special characters enhances strength.
Diversity: Using a diverse set of characters improves password strength.
* 4.2 Code's Password Strength Evaluation
The check_password_strength() method provides a strength classification based on length and character types.
The classification includes "Strong," "Medium," and "Weak" categories.
* 4.3 Security Considerations
Brute-force attacks are inherently insecure and inefficient for longer passwords or strong password policies.
Users are encouraged to follow password best practices, including using complex and unique passwords.

