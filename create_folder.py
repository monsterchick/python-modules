'''
自动创建文件夹或文件 Automatically create folders or files.
'''
import os


class Create:
    def __init__(self):
        pass

    def mkdir(self, folder_name, subfolder_name=None):
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
                os.makedirs(os.path.join(os.getcwd(),folder_name, subfolder_name))
                print(f"{folder_name}/{subfolder_name} created successfully!")
            except FileExistsError:
                print(f"{folder_name}/{subfolder_name} already exists.")

        elif not os.path.isdir(folder_name) and subfolder_name is not None:
            os.makedirs(folder_name)
            os.makedirs(os.path.join(os.getcwd(),folder_name, subfolder_name))
            print(f"{folder_name} created successfully!")
            print(f"{folder_name}/{subfolder_name} created successfully!")
        else:
            print(f"{folder_name} already exists.")

    def mkfile(self, filename, folder=None, content=None):
        # 当前路径+文件名
        # print(os.path.join(os.getcwd(),filename))
        # 当前路径+文件夹+文件名
        # print(os.path.join(os.getcwd(), folder, filename))

        path_without_folder = os.path.join(os.getcwd(),filename)
        path_with_folder = os.path.join(os.getcwd(),folder,filename)

        # 默认当前路径创建 | 文件在当前路径不存在 | 没有数据写入
        if not os.path.exists(path_without_folder) and folder is None and content is None:
            content = ''
            with open(path_without_folder, 'w') as f:
                f.write(content)
                print(f"{filename} created successfully!")

        # 默认当前路径创建 | 文件在当前路径不存在 | 有数据写入
        elif not os.path.exists(path_without_folder) and folder is None and content is not None:
            print(content)
            with open(path_without_folder, 'w') as f:
                f.write(content)
                print(f"{filename} created successfully! Data has been written.")

        # 指定文件夹路径创建 | 指定文件夹路径不存在 | 没有数据写入
        elif not os.path.exists(path_with_folder) and folder is not None and content is None:
            content = ''
            # 反复尝试打开文件夹
            while True:
                try:
                    with open(path_with_folder, 'w') as f:
                        f.write(content)
                        break
                except FileExistsError and FileNotFoundError:
                    # 创建文件夹
                    self.mkdir(folder_name=folder)
            print(f"{folder}/{filename} created successfully!")

        # 指定文件夹路径创建 | 指定文件夹路径不存在 | 有数据写入
        elif not os.path.exists(path_with_folder) and folder is not None and content is not None:
            # 反复尝试打开文件夹
            while True:
                try:
                    with open(path_with_folder, 'w') as f:
                        f.write(content)
                        break
                except FileExistsError and FileNotFoundError:
                    # 创建文件夹
                    self.mkdir(folder_name=folder)
            print(f"{folder}/{filename} created successfully! Data has been written.")
        # 其它情况
        # 文件已经存在 | 有子文件夹存在的情况
        elif os.path.exists(path_without_folder) and folder is None and content is None:
            print('111')
        else:
            pass
            # with open(path_with_folder, 'w') as f:
            #     f.write(content)
        # # 文件已经存在 | 没有子文件夹存在的情况
        # elif os.path.exists(path_without_folder) and content is not None:
        #     with open(path_without_folder, 'w') as f:
        #         f.write(content)
        # else:
        #     pass
        # print(f"{folder}/{filename} already exists. Data has been written.")


# 创建文件夹/子文件夹
# Create().mkdir(folder_name='download',subfolder_name='video')

tem_data = 'data to be tested'
# 创建文件
Create().mkfile(filename='my_file.json')