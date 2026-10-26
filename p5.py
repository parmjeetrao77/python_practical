import os
import sys

def main():
    directory = input("Enter directory path (blank for current): ")
    directory = directory or "."

    if not os.path.isdir(directory):
        print("Directory does not exist.")
        return

    print("\nCurrent directory:", os.path.abspath(directory))
    print("\nFiles and folders:")

    for item in os.listdir(directory):
        print(item)

    extension = input("\nEnter extension to search (e.g. .txt): ")

    if extension:
        print("\nMatching files:")
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isfile(path) and item.endswith(extension):
                print(item)

    folder = input("\nEnter new folder name (blank to skip): ")

    if folder:
        new_path = os.path.join(directory, folder)
        os.makedirs(new_path, exist_ok=True)
        print("Folder created:", new_path)

    log_name = input("\nEnter log filename (blank to skip): ")

    if log_name:
        with open(os.path.join(directory, log_name), "w") as file:
            file.write("File management utility log\n")
            file.write("Directory: " + os.path.abspath(directory))
        print("Log file created.")

if __name__ == "__main__":
    print("Command-line arguments:", sys.argv)
    main()