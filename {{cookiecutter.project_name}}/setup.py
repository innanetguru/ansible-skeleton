#!/usr/bin/python3
## script to setup local environment and install packages
## execute from ./setup.sh
## 1) Install python-pip
##      a)check for existing pip installation
## 2) configure linux environment for pip & ansible
## 3) install & configure pipenv

import os 
import os.path 
import subprocess 


def configure_pipenv():
    return

def config_shell(*args, **kwds):
    # configure bash $PATH variable to include "/$HOME/.local/bin"

    return 

def install_pip():
        #install pip
    
    return config_shell()

# discover whether pip is currently installed and where
def discover_pip(*args):

    check_pip = subprocess.check_output('which pip; exit 0', shell=True, stderr=subprocess.STDOUT)

    if check_pip == user_pip_bin:
        print('pip is installed in the home directory')
        print(check_pip)
        return config_shell()
    elif check_pip in root_pip_bin:
        print('pip is enabled for users with sudo/root permissions')
        print(check_pip)
    else:   # i.e. if check_pip != user_bin_pip or root_pip_bin
        # declare global namespace 'pip' with value 'None' to pass to install_pip
        #global pip; 
        return install_pip()
    

home = os.getenv('HOME')
local_pip_bin = '/.local/bin/pip'
root_pip_bin = ['/usr/bin/pip','/usr/local/bin/pip']
user_pip_bin = home + local_pip_bin + "\n"

def main():
    discover_pip(root_pip_bin, user_pip_bin, home, local_pip_bin)

if __name__ == "__main__":
    main()