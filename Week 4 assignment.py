import os

def modify_file():
    try:
        filename = input("Enter the filename to read: ").strip()  # Remove leading/trailing whitespace
        if not filename:
            print("Error: Filename cannot be empty.")
            return

        # Split the filename into directory and base components
        dir_name = os.path.dirname(filename)
        base_name = os.path.basename(filename)
        new_base_name = "modified_" + base_name
        new_filename = os.path.join(dir_name, new_base_name)

        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_file()
