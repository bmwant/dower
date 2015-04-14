import subprocess
import os
from subprocess import Popen, CREATE_NEW_CONSOLE


#Popen(["cmd"], creationflags=CREATE_NEW_CONSOLE)

#Start nginx in the background
os.chdir('installers/nginx-1.6.3/nginx-1.6.3/')
nginx_pid = Popen(['nginx.exe']).pid
print(nginx_pid)