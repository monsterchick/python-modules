import os


class FileMaker:
    def __init__(self):
        self.default = 'new file.txt'

    def make_file(self, filename='', content=''):
        '''
            | 文件是否存在 | 提供文件夹名称 | 提供数据 |
         c1 |     否     |      没有    |   没有   |
         c2 |     否     |      没有    |     有   |
         c3 |     否     |       有    |    没有   |
         c4 |     否     |       有    |     有   |
         c5 |     是     |      没有    |   没有   |
         c6 |     是     |      没有    |    有   |
         c7 |     是     |       有    |    没有   |
         c8 |     是     |       有    |     有   |
        '''

        message = ''

        if filename == '':
            filename = self.default
        else:
            pass
        path = os.path.join(os.getcwd(), filename)
        # print(path)

        # | filename given | content given | path exists |
        if filename != '' and content != '' and os.path.exists(path):
            message = f'The file {filename} already exists.'
        elif filename != '' and content == '' and os.path.exists(path):
            message = f'The file {filename} already exists.'
        elif filename == '' and content != '' and os.path.exists(path):
            message = f'The file {filename} already exists.'
        elif filename == '' and content == '' and os.path.exists(path):
            message = f'The file {filename} already exists.'
        else:
            with open(path, 'w') as f:
                f.write(content)
            message = f'{filename} created successfully and content has been added!'

        print(message)
