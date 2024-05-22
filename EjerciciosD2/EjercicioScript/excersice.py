def read_collaborators(file):
    try:
        with open(file, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def print_collaborators(collaborators, num=5):
    if not collaborators:
        print("No collaborators found.")
    else:
        for i, collaborator in enumerate(collaborators[:num]):
            print(f"{i+1}. {collaborator}")


def add_collaborator(file, new_collaborator):
    collaborators = read_collaborators(file)
    if len(collaborators) >= 15:
        print("Cannot add more collaborators, the list is full.")
    else:
        with open(file, 'a') as f:
            f.write(new_collaborator + '\n')
        print(f"Collaborator {new_collaborator} added successfully.")


def main():
    file = 'collaborators.txt'

    while True:
        print("\nOptions:")
        print("1. View collaborators")
        print("2. Add collaborator")
        print("3. Exit")
        choice = input("Select an option (1, 2, 3): ")

        if choice == '1':
            num = input("Listar Colaboradores: ")
            num = int(num) if num.isdigit() else 5
            collaborators = read_collaborators(file)
            print_collaborators(collaborators, num)
        elif choice == '2':
            new_collaborator = input("Enter the name of the new collaborator: ")
            add_collaborator(file, new_collaborator)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
