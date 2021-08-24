# import here
import subprocess
import platform
import socket
import time
import os


# end import
# define here


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    commandPing = ['ping', param, pingTimes, host]
    return subprocess.call(commandPing)


def error(type):
    if type == 1 or type == 'dirNotFound':
        print('ERROR: No such file or directory.')
    elif type == 2 or type == 'pathExists':
        print('ERROR: File exists. Try a different command.')


# end define

path = '/'

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
print('Welcome to the PyTerminal Prototype v0.1!')
print('Created Aug 24th, 2021')
while True:
    command = input(path + ' >>>')
    dir_list = os.listdir(path)
    if command == 'ping':
        host = input('http domain: ')
        pingTimes = input('Ping amount: ')
        print(ping(host))

    if command == 'local':
        print('Local IPS: ' + hostIP)
        print('Machine Name:' + hostName)
    if command == 'date':
        print('Local Date: ' + time.strftime('%m/%d/%y'))
    if command == 'list':
        dir_list = os.listdir(path)
        print("Local files and directories in '" + path + "':")
        print(dir_list)
    if command == 'list -a':
        file = input('Path: ')
        dir_list2 = os.listdir(file)
        print(dir_list2)
    if command == 'echo' or command == 'echo me':
        echo = input()
        print(echo)
    if command == 'cd':
        path = input("Please type in the directory you would like to go to: ")
        if path == 'BASE^PT':
            os.chdir('/')
        else:
            path = '/' + path
            os.chdir(path)
    if command == 'replace file':
        newFile = input('Filename: ')
        open(newFile, 'w')
    if command == 'mkfile' or command == 'make file':
        newFile = input('Filename: ')
        if newFile in dir_list:
            error(2)
        else:
            open(newFile, 'x')
