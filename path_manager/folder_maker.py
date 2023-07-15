import os


class FolderMaker:
    def __init__(self):
        pass

    def mkdir(self, folder_name="new folder", subfolder_name=None):
        '''Check if the given file name exists.'''
        # to only make mainfolder
        if not os.path.isdir(folder_name) and subfolder_name is None:
            os.makedirs(folder_name)
            print(f"{folder_name} created successfully!")

        # to make mainfolder and subfolder
        elif os.path.isdir(folder_name) and subfolder_name is not None:
            # 子目录
            # print(os.path.join(os.getcwd(),folder_name, subfolder_name))
            try:
                os.makedirs(os.path.join(os.getcwd(), folder_name, subfolder_name))
                print(f"{folder_name}/{subfolder_name} created successfully!")
            except FileExistsError:
                print(f"{folder_name}/{subfolder_name} already exists.")

        elif not os.path.isdir(folder_name) and subfolder_name is not None:
            os.makedirs(folder_name)
            os.makedirs(os.path.join(os.getcwd(), folder_name, subfolder_name))
            print(f"{folder_name} created successfully!")
            print(f"{folder_name}/{subfolder_name} created successfully!")
        else:
            print(f"{folder_name} already exists.")