import os
# if os.path.exists('demo.txt'):
#     os.remove('demo.txt')
# else:
#     print('The file is not exist')

if os.path.exists('demofolder'):
    os.rmdir('demofolder')
else:
    print('the folder is not exist')