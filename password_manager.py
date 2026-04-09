import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, 'r') as file:
        password = file.readline().strip() 
    encrypted_password = caesar_encrypt(password)
    with open(filename, 'w') as file:
        file.write(encrypted_password)
    
def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = []
        for row in reader:
            if row:
                rows.append(row)
    for i in range(1, len(rows)):
        rows[i][2] = caesar_encrypt(rows[i][2])
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
