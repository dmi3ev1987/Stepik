def is_subfolder(folder_dict, subfolder, folder):
    while True:
        for current_folder, subfolder_list in folder_dict.items():
            if subfolder in subfolder_list:
                if current_folder == folder:
                    return True
                else:
                    subfolder = current_folder
                    break
        else:
            return False
