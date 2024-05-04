def check_name(file_name, roll_number):
    roll_number_file_name = ""

    roll_number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    i = 0
    while(i < len(file_name)):
        if(file_name[i] in roll_number_list):
            roll_number_file_name = roll_number_file_name + file_name[i]
        else:
            break
        
        i = i + 1

    if (int(roll_number_file_name) == int(roll_number)):
        return 1
    else:
        return 0