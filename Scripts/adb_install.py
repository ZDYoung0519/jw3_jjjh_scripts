import os
from shutil import copy


def MoveFiles(path1, path2):
    file_lst = os.listdir(path1)
    for file in file_lst:
        copy(path1 + '/' + file, path2 + file)


def AddToPath(path2):
    os.system('path=%path%;'+path2)


def ADBTest():
    return os.popen('adb version').read()


def ConnectTest():
    return os.popen('adb devices').read()