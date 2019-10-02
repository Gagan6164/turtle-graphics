from sys import argv
import os
import sys
import threading
import time
import getpass

from detection import func

if not os.path.exists(os.environ['HOME']+"/3y3/face/known"):
    print("No user registered!")
    sys.exit()

username = os.environ.get('SUDO_USER')
print(username)

num_args = len(argv[1:])
print(num_args)
args = argv[1:]

print(args)

while True :

    user = func()

    if user != 'unknown':
        if num_args:
            if args[0] == "detect":
                str = "echo -e '[greeter]\nlast-user={}' > /var/lib/lightdm/.cache/unity-greeter/state"
                os.system(str.format(user))
                sys.exit()
        elif user != username:
            str = "dm-tool switch-to-user {}"
            os.system(str.format(user))
            sys.exit()
           
    else:
        if not num_args:
            os.system('./dummy.sh')
            #os.system("dm-tool switch-to-greeter")
            sys.exit()

    time.sleep(5)
        
    
