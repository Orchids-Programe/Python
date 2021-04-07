import os
def makedir(path):
    #kiểm tra xem path đã tồn tại chưa
    if os.path.exists(path):
        print(path, 'is exists')
    else:
        os.mkdir(path)
        print(path, ' has been created')

def makefile(path):
    f = open(path, 'x')
    f.close()
    print(path, ' has been created')

def ls(path):
    if os.path.exists(path):
        #listdir trả về một danh sách với tên các file trong thư mục path
        return os.listdir(path)
    else:
        print(path, 'is exists')
def cd(path):
    if os.path.exists(path):
        global currentpath
        #abspath() trả về đường dẫn
        currentpath = os.path.abspath(path)
        #chdir() chuyển sang đường dẫn của file cần tới
        os.chdir(path)
        print('Chang working to ',os.getcwd()) #getcwd() kiểm tra trả về thư mục đang làm việc hiện tại
    else:
        print('path is not exists')
while True:
    s = input()
    if not s:
        break
    s = s.strip() #xoa bo ky tu thua
    tokens = s.split(' ')
    print('parsing command >>>',tokens)
    #statswith() trả về True nếu bắt đầu đúng bằng chuỗi đó, ngươc lại False
    if s.startswith('mkdir'):
        makedir(tokens[1])
    elif s.startswith('mkfile'):
        makefile(tokens[1])
    elif s.startswith('ls'):
        if(len(tokens) > 1):
            l = (ls(tokens[1]))
        else:
            l = (ls(os.getcwd()))

        for i in l:
            print(i)
    elif s.startswith('cd'):
        cd(tokens[1])
    else:
        print('Unknow command : ',s)