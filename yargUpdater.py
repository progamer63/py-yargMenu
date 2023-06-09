import os
import requests
import shutil
import wget
cd = os.path.realpath(os.path.dirname(__file__))
#find dir or make it
docs = os.path.expanduser('~\Documents')
os.chdir(docs)
path = (docs+'\YARG')
exists = os.path.exists(path)
if (exists == True):
    print(f'{path} exists')
if (exists == False):
    os.mkdir(path)
    exists = os.path.exists(path)
    print(f"made {path}")
print()
temp = (path+'\Temp')
exists = os.path.exists(temp)
if (exists == True):
    print(f'{temp} exists')
if (exists == False):
    os.mkdir(temp)
    exists = os.path.exists(temp)
    print(f"made {temp}")
print()

#find all yargs
root = path
fnames = []
for f in os.scandir(root):
    if f.is_dir():
        if len(os.listdir(f)) == 0:
            print(str(f.name)+ " is empty")
        if not len(os.listdir(f)) == 0:
            print(str(f.name)+ " is not empty")
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
    
#make request finally
print("fetching latest version from github")
latest = requests.get('https://github.com/YARC-Official/YARG/releases/latest')
resp = latest.url
lver = resp.split("v")[1]
print("latest from github is "+lver)

#find the most up to date version you have
newestlocalver = max(vers)
print(newestlocalver+ " is the newest version of the game you have")
if (newestlocalver > lver):
    print("you have a newer version: "+item+" vs "+lver)
    print("how though?")
    needToUpdate = False
elif (newestlocalver == lver):
    print("you have the latest: "+item)
    needToUpdate = False
elif (newestlocalver < lver):
    print ("you have an older version: "+item+" vs "+lver)
    needToUpdate = True

#use vers dict now
os.chdir(temp)
print('downloading versions dictionary')
dictUrl='https://raw.githubusercontent.com/progamer63/py-yargMenu/main/acceptedVers.py'
wget.download(dictUrl)
os.system('cls')
from acceptedVers import versList
lookingVer = lver
for ver in versList:
    #print(f'got ver {ver}')
    if ver not in versList:
        print('found a version not in my dict')
if lookingVer in versList:
    url = versList[f'{lookingVer}']

#if need to update, do that stuff lol
if (needToUpdate == True):
    print()
    os.chdir(root)
    print("updating from "+newestlocalver+" to "+lver)
    print("downloading from "+url)
    print("this can take a while")
    if (os.path.exists(f'YARG_v{lver}-Windows-x64.zip') == False):
        wget.download(url)
        print("downloaded")
    if (os.path.exists(f'YARG_v{lver}-Windows-x64.zip') == True):
        print("already downloaed")
    print("unzipping")
    shutil.unpack_archive(f'{root}/YARG_v{lver}-Windows-x64.zip', f'YARG_v{lver}-Windows-x64')
    print("unzipped")
    print("deleting source .zip")
    if os.path.exists(f'{root}/YARG_v{lver}-Windows-x64.zip'):
        os.remove(f'{root}/YARG_v{lver}-Windows-x64.zip')
if (needToUpdate == False):
    print("no need to update :)")

#clear temp folder
print('clearing temp folder')
os.chdir(temp)
for i in os.listdir(temp):
    if i.endswith('.py'):
        os.remove(i)
input("press any key to go to main menu")
import menu
