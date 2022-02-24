import os,re,shutil

os.chdir('C:\\Users\\ahmed\\Downloads') #optional for manual input of working directory.
current_dir = os.getcwd()
des_dir = 'R:\\new arrival' # change this to your location where you want to have the new folders..
print('working on: ' , current_dir)

def analyzer():
    files = 0
    folders = 0
    dir_lst = os.listdir()
    if dir_lst:
        for x in dir_lst:
            if os.path.isfile(x):
                files += 1
            elif os.path.isdir(x):
                folders += 1
            else:
                pass
        print('you have {} folder(s) and {} file(s) here...'.format(folders,files))
    else:
        pass
def file_analyzer(file):
    print('working with file..',file)
    try:
        extension = re.search(r'\.[a-zA-Z]+$',file)
        if (extension.group().lower() == '.txt'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'txt')
            if os.path.isdir(dest):
                shutil.move(original,dest)
                print(file, 'moved successfully...')
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
                print(file, 'moved successfully...')
        elif (extension.group().lower() == '.pdf'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'pdf')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.exe'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'exe')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.apk'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'apk')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.jpg') or (extension.group().lower() == '.jpeg'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'jpg')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.ppt') or (extension.group().lower() == '.pptx'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'pptx')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.doc') or (extension.group().lower() == '.docx'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'doc')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.mp4') or (extension.group().lower() == '.mkv'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'mp4')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.rar') or (extension.group().lower() == '.zip'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'zip')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
        elif (extension.group().lower() == '.png') or (extension.group().lower() == '.tif') or (extension.group().lower() == '.svg') or (extension.group().lower() == '.gif'):
            original = os.path.join(os.getcwd(),file)
            dest = os.path.join(des_dir,'png')
            if os.path.isdir(dest):
                shutil.move(original,dest)
            else:
                os.mkdir(dest)
                shutil.move(original,dest)
    except:
        print('An Error occured...')

def folder_parser(folder):
    curr_dir = os.getcwd()
    os.chdir(os.path.join(curr_dir,folder))
    print('directory changed to folder "{}"'.format(folder))
    print('new current directory is {}'.format(os.getcwd()))
    analyzer()
    lst = os.listdir()
    for item in lst:
        if os.path.isdir(item):
            print('entering nested folder..')
            folder_parser(item)
        elif os.path.isfile(item):
            file_analyzer(item)
        else:
            None
    os.chdir('../')




if __name__ == '__main__':
    lst = os.listdir() #lst is a list containg dir list,files and folders.
    if lst:
        analyzer()
        for item in lst:
            if os.path.isdir(item):
                folder_parser(item)
            elif os.path.isfile(item):
                file_analyzer(item)
            else:
                None
    else:
        print('invalid path')
