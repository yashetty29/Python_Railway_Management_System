import datetime
import TableIt
import incavail
import redavail
import displaymsg


def user_loggedin(username):
    displaymsg.displaymsg(username)
    while 1:
        n = int(input("\n1.Book Ticket\n2.Cancel Ticket\n3.View All booked Ticket\n4.All Train Details\n5.Logout\nEnter you choice: "))
        if n == 1:
            bookmeth = int(input("\n1.Train no\n2.Journey Details\n3.Exit\nEnter you choice: "))
            if bookmeth == 1:
                ta = 0
                trainno = input("Enter Train No: ")
                f = open("train", "r")
                lines = f.readlines()
                f.close()
                for l in lines:
                    ct = l.split("|")
                    if trainno == ct[1] and int(ct[8]) > 0:
                        ta = 1
                if ta == 1:
                    name = input("Enter the passenger name: ")
                    f = open("booking", "a")
                    f.write(username + "|" + name + "|"+trainno+"$\n")
                    f.close()
                    redavail.redavail(trainno)
                    print("\nBooked Successfully")
                    input()
                else:
                    print("\nTrain not available or ticket not available")
                    input()
            elif bookmeth == 2:
                jdate = str(datetime.datetime(int(input("Enter journey year: ")), int(input("Enter journey Month: ")), int(input("Enter jouney Day: "))).date())
                jsour = input("Enter Journey Source: ")
                jdest = input("Enter the journey Destination: ")
                f = open("train", "r")
                ta = 0
                tl = []
                for l in f:
                    l = l.split("|")
                    if l[2] == jdate and l[3] == jsour and l[4] == jdest and int(l[8].strip("$\n")) > 0:
                        tl.append(l)
                        ta = 1
                f.close()
                if ta == 0:
                    print("\nTrain Not Available")
                    input()
                else:
                    i = 0
                    for i in range(len(tl)):
                        print(i, ".", tl[i])
                    print(i+1, ".", "Exit")
                    trainselected = int(input("\nEnter Which Train you want to book Ticket: "))
                    if trainselected < len(tl):
                        name = input("Enter passenger name the you want to book the ticket for: ")
                        f = open("booking", "a")
                        f.write(username+"|"+name+"|"+tl[trainselected][1]+"$\n")
                        f.close()
                        redavail.redavail(tl[trainselected][1])
                        print("\nBooked Successfully")
                        input()
        elif n == 2:
            f = open("booking", "r")
            bk = [["NO", "Username", "Passenger", "Train no"]]
            tc = 0
            for l in f:
                a = l.split("|")
                if a[0] == username:
                    a.insert(0, str(tc))
                    a[len(a)-1] = a[len(a)-1].strip("$\n")
                    tc += 1
                    bk.append(a)
            f.close()
            if len(bk) > 1:
                print("\nEnter which ticket you want to cancel: ")
                print(bk)
                TableIt.printTable(bk, useFieldNames=True)
                clist = int(input())
                if clist < len(bk):
                    ctno = bk[clist+1][3].strip("$\n")
                    cname = bk[clist+1][2]
                    f = open("booking", "r")
                    lines = f.readlines()
                    f.close()
                    f = open("booking", "w")
                    for l in lines:
                        wl = l.split("|")
                        wl[2] = wl[2].strip("$\n")
                        if wl[1] != cname or wl[2] != ctno:
                            f.write(l)
                    f.close()
                    incavail.incavail(ctno)
                    print("\nTicket Cancelled Successfully")
                    input()
            else:
                print("\nYou have no booking", end="")
                input("")
        elif n == 3:
            tktlist = [["Username", "Passenger", "Train No"]]
            f = open("booking", "r")
            lines = f.readlines()
            f.close()
            for l in lines:
                tktl = l.split("|")
                tktl[len(tktl) - 1] = tktl[len(tktl) - 1].strip("$\n")
                if tktl[0] == username:
                    tktlist.append(tktl)
            if len(tktlist) != 1:
                TableIt.printTable(tktlist, useFieldNames=True)
            else:
                print("\nYou have no booking", end="")
                input("")
        elif n == 4:
            trlist = [["Name", "Train Number", "Date", "SRC", "DST", "Departure", "Time", "Avail Seats", "Price"]]
            f = open("train", "r")
            lines = f.readlines()
            f.close()
            if len(lines) != 0:
                for l in lines:
                    tl = l.split("|")
                    tl[len(tl) - 1] = tl[len(tl) - 1].strip("$\n")
                    tl.pop(7)
                    trlist.append(tl)
                TableIt.printTable(trlist, useFieldNames=True)
            else:
                print("\nNo Trains Available")
                input()
        else:
            print("\nLogged out")
            return