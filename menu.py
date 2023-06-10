import os
import sys
cd = os.path.realpath(os.path.dirname(__file__))
os.system('cls')
print('''                                           __  __                  
                                          |  \/  |                 
  _ __  _   _ ______ _   _  __ _ _ __ __ _| \  / | ___ _ __  _   _ 
 | '_ \| | | |______| | | |/ _` | '__/ _` | |\/| |/ _ \ '_ \| | | |
 | |_) | |_| |      | |_| | (_| | | | (_| | |  | |  __/ | | | |_| |
 | .__/ \__, |       \__, |\__,_|_|  \__, |_|  |_|\___|_| |_|\__,_|
 | |     __/ |        __/ |           __/ |                        
 |_|    |___/        |___/           |___/          ''')
print()
print('created by progamer63')
print('©2023')
print()
print('options:')
print('1: launch yarg | 2: update yarg | 4: quit')
opt = input('what would you like to do? ')
print()
print()
if (opt == '1'):
    os.system('cls')
    #with open(f'{cd}\yargLauncher.py') as f:
        #exec(f.read())
    import yargLauncher
if (opt == '2'):
    os.system('cls')
    #with open(f'{cd}\yargUpdater.py') as f:
        #exec(f.read())
    import yargUpdater
if (opt == '4'):
    print('bye')
    sys.exit()