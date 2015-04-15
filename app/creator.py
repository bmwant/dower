# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'
import os
import shutil
import subprocess
from subprocess import CREATE_NEW_CONSOLE, Popen


fj = os.path.join


class Creator(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def create(self):
        project_dir = fj('c:/projects', self.name)
        if os.path.exists(project_dir):
            raise 'Directory with this name already exists'
        yield 'Creating directories structure...'
        shutil.copytree(fj('factory', self.type), project_dir)
        os.chdir(project_dir)
        #Popen(['c:/python27/scripts/virtualenv', 'venv'], creationflags=CREATE_NEW_CONSOLE)
        yield 'Creating virtual environment...'
        subprocess.call(['c:/python27/scripts/virtualenv', 'venv'])
        yield 'Installing dependencies...'
        subprocess.call(['c:/python27/scripts/pip', 'install', '-r', 'requirements.txt'])
        python_exe = fj(project_dir, 'venv/scripts/python.exe')
        Popen(['cmd', '/K', python_exe, 'run.py'], creationflags=CREATE_NEW_CONSOLE)
