from main import PasswordCracker
  
obj = PasswordCracker()

obj.show_menu()
while True:
    choice = input('Make a choice: ')

    if choice == '1':
        obj.set_password()
        obj.show_menu()

    elif choice == '2':
        if obj.password is None:
            print('First set a password, please type 1')
        else:
            difficulty = input('Weak char set or stronger? (w/s) ')
            obj.brute_force_password() if difficulty == 'w' else obj.brute_force_password(difficulty=True)

    elif choice == '3':
        if obj.password is None:
            print('First set a password, please type 1')
        else:
            path = input('Enter the path to the common password file: ')
            obj.brute_force_with_common_passwords(path)

    elif choice == '4':
        if obj.password is None:
            print('First set a password, please type 1')
        else:
            print(obj.check_password_strength())

    elif choice == '5':
        obj.delete_password()
        

    elif choice.lower() == 'q':
        break

    elif choice.lower() == 'm':
        obj.show_menu()

    else:
        print('Choose a correct command')

