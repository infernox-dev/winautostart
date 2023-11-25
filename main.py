import sys

sys.dont_write_bytecode = True

from os import system

from winautostart import Autostart

autostart = Autostart()


print("Welcome to WinAutostart Terminal version V-1.0.")
print("Easily manage your autostarts in the Windows registry.")


while True:
    system("cls")

    print("Available commands:")
    print("1. Add autostart")
    print("2. Remove autostart")
    print("3. Update autostart")
    print("4. Get autostart command by index")
    print("5. List all autostarts")
    print("6. Exit")

    choice = input("Enter the number of the option: ")
    print()

    if choice == "1":
        name = input("Enter the name of the autostart: ")
        command = input("Enter the command: ")
        autostart.add(name=name, command=command)
        print("New autostart is successfully added.")

    elif choice == "2":
        name = input("Enter the autostart name: ")
        autostart.remove(name=name)
        print("Autostart is successfully removed.")

    elif choice == "3":
        name = input("Enter the autostart name: ")
        new_command = input("Enter the new command: ")
        autostart.update(name=name, new_command=new_command)
        print("Autostart is successfully updated.")

    elif choice == "4":
        name = input("Enter the name of autostart: ")
        print(autostart.get_command(name=name) or "This autostart is not found")

    elif choice == "5":
        for name in autostart.list_all():
            print("Name: %s | Command: %s" % (name, autostart.get_command(name=name)))

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6")

    input("[Enter]: ")
