from path_manager.folder_maker import FolderMaker
from path_manager.file_maker import FileMaker



if __name__ == '__main__':
    folder_maker = FolderMaker()
    # fl_wtr = FileWriter()
    file_maker = FileMaker()


    # make a folder
    folder_maker.mkdir(folder_name="my folder", subfolder_name="my tiny folder")

    # make a file
    file_maker.make_file()
