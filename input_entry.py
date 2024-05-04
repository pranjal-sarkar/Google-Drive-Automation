def input_entries():
    master_folder = input("Enter master folder name: ")
    file_folder = input("Enter file folder name: ")
    roll_no = input("Enter Roll Number of person: ")
    roll_no = roll_no[:2]

    return [master_folder, file_folder, roll_no]