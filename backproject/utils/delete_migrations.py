import os

for root, dirs, files in os.walk("..", topdown = False):
    if 'migrations' in root:
        for file in files:
            if not file.startswith('__init__'): 
                if not file.startswith('db'):
                    print (root+'\\'+ file)
                    ## os.remove(root+'\\'+file)