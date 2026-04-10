from password_manager import add_login, change_password, encrypt_passwords_in_file

def main() -> None:
    archivo = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(archivo)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        opcion = input()
        if opcion == 1:
            user_input = input("Enter the website and the new password:\n")
            partes = user_input.split()
            if len(partes) < 2:
                print("Input is in the wrong format!")
                continue
            website = partes[0]
            password = partes[1]
            if len(password) < 12:
                print("Password is too short!")
                continue
            resultado = change_password(archivo, website, password)
            if resultado == False:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")
        elif opcion == 2:
            user_input = input("Enter the website, username, and password:\n")
            partes = user_input.split()
            if len(partes) < 3:
                print("Input is in the wrong format!")
                continue
            website = partes[0]
            username = partes[1]
            password = partes[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(archivo, website, username, password)
            print("Login added.")
        elif opcion == 3:
            break
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
