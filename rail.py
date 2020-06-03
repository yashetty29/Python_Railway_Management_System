import user_loggedin
import admin_loggedin
while True:
    mode = int(input("\n1.User\n2.Admin\n3.Exit: "))
    if mode == 1:
        user = int(input("\n1.Login\n2.Register:\n3.Exit: "))
        if user == 1:
            valid = 0
            username = input("\nEnter you username: ")
            password = input("\nEnter your password: ") + "$\n"
            f = open("user", "r")
            for lines in f:
                usn = lines.split("|")
                if usn[0] == username and usn[2] == password:
                    valid = 1
            f.close()
            if valid == 0:
                print("\nUsername or password wrong", end="")
                input()
            elif valid == 1:
                user_loggedin.user_loggedin(username)
        if user == 2:
            valid = 0
            name = input("\nEnter your name: ")
            username = input("\nEnter your user name: ")
            password = input("\nEnter your password: ")
            f = open("user", "r")
            for lines in f:
                usn = lines.split("|")
                if usn[0] == username:
                    print("\nUser name already Taken please use new one")
                    input()
                    valid = 1
            if valid == 0:
                f = open("user", "a")
                f.write(username + "|" + name + "|" + password + "$\n")
                f.close()
                print("\nRegistered Successfully")
                input()
                user_loggedin.user_loggedin(username)
    elif mode == 2:
        ausername = input("Enter the admin username")
        apassword = input("Enter the admin password")
        if ausername == 'admin' and apassword == 'admin':
            admin_loggedin.admin_loggedin()
        else:
            print("\nWrong Credentials\n")
            input()
    else:
        exit(0)
