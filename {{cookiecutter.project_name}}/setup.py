#!/usr/bin/python
## script to setup local environment and install packages
## execute from ./setup.sh
## 1) Install python-pip
##      a)check for existing pip installation
## 2) configure linux environment for pip & ansible
## 3) install & configure pipenv

import os 
import os.path 
import subprocess 

home = os.getenv('HOME')
local_pip_bin = '/.local/bin/pip'
root_pip_bin = ['/usr/bin/pip','/usr/local/bin/pip']
user_pip_bin = home + local_pip_bin + "\n"

# discover whether pip is currently installed and where
def discover_pip():
    check_pip = subprocess.check_output('which pip; exit 0', shell=True, stderr=subprocess.STDOUT)

    if check_pip == user_pip_bin:
        print('pip is installed in the home directory')
        print(check_pip)
    elif check_pip in root_pip_bin:
        print('pip is enabled for users with sudo/root permissions')
        print(check_pip)
    else:   # i.e. if check_pip != user_bin_pip or root_pip_bin
        # declare global namespace 'pip' with value 'None' to pass to install_pip
        global pip; pip = None
    
def install_pip(*args, **kwds):
    if "pip" in args:
        pip=args["pip"]
        #install pip
    

def config_shell(*args, **kwds):
    if pip in args:
        print(pip)
    else:

        return 

def configure_pipenv():
    return

if __name__ == "__main__":
    discover_pip()