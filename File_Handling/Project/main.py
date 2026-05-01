from pathlib import Path

def readFileAndFolder():
    path = Path(__file__).parent.parent
    items = list(path.glob("*"))
    for i, item in enumerate(items):
        print(f"{i+1} : {item.name}")


def createFile():
    try:
        base_path = Path(__file__).parent.parent
        readFileAndFolder()
        name = input("Enter you file name: ")
        p = base_path / name
        if not p.exists() and p.is_file():
            with open(p, "w") as fs:
                data = input("What you want to write: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as err:
        print("Error: ", err)


def readFile():
    try:
        readFileAndFolder()
        name = input("Whcih file you want to read: ")
        base_path = Path(__file__).parent.parent
        p = base_path / name
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
    
    except Exception as err:
        print("Error: ", err)


def updateFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to update: ")
        base = Path(__file__).parent.parent
        p = base / name

        if p.exists() and p.is_file():
            print("Press 1 for changing the file name")
            print("Press 2 for overwriting the file")
            print("Press 3 for appending content to the file")

            res = int(input("Enter your choice: "))

            if res == 1:
                new_name = input("Enter new file name: ")
                new_path = base / new_name
                if not new_path.exists():
                    p.rename(new_path)
                    print("File name changed successfully")
                else:
                    print("File with this name already exists")

            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Enter new content: ")
                    fs.write(data)
                print("File overwritten successfully")

            elif res == 3:
                with open(p, "a") as fs:
                    data = input("Enter new content: ")
                    fs.write(data)
                print("File appended successfully")

            else:
                print("Invalid choice")

        else:
            print("File not found")
    
    except Exception as err:
        print("Error: ", err)


def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete: ")
        base = Path(__file__).parent.parent
        p = base / name

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("File not found")

    except Exception as err:
        print("Error: ", {err})



print("1 for creating a file !!")
print("2 for reading a file !!")
print("3 for updating a file !!")
print("4 for deleting a file !!")


check = int(input("Enter your choice : "))


if check == 1:
    createFile()

if check == 2:
    readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()
