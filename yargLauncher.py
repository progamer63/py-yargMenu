import os
import sys
cd = os.path.realpath(os.path.dirname(__file__))
#find dir or make it
docs = os.path.expanduser('~\Documents')
os.chdir(docs)
path = (docs+'\YARG')
exists = os.path.exists(path)
if (exists == True):
    print(f'{path} exists')
if (exists == False):
    print(f"relaunching to run the updater to install into {path}")
    input('press any key to continue')
    os.system('cls')
    with open(f'{cd}\main.py') as f:
        exec(f.read())
print()

#find all yargs
root = path
fnames = []
for f in os.scandir(root):
    if f.is_dir():
        if len(os.listdir(f)) == 0:
            print(str(f.name)+ " is empty, ignoring")
        if not len(os.listdir(f)) == 0:
            #print(str(f.name)+ " is not empty")
            fnames.append(f.name)
print()
yargs = []
for f in fnames:
    if f.startswith("YARG"):
        yargs.append(f) 
#print(yargs)
        
#get all version numbers
vers = []
for item in yargs:
    item = item.split("-")[0]
    item = item.split("v")[1]
    vers.append(item)
    #print(item)

#find the most up to date version you have
newestlocalver = max(vers)
print(newestlocalver+ " is the newest version of the game you have & is the one that will be opened")
path = f'{root}\YARG_v{newestlocalver}-Windows-x64'
if os.path.exists(path):
    os.chdir(path)
    if os.path.isfile(f'YARG.exe'):
        print('YARG.exe is real, running it')
        os.system('YARG.exe')
    sys.exit()

