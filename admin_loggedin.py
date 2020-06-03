import datetime
import TableIt


def admin_loggedin():
    while 1:
        n = int(input("\n1.Add new Train\n2.Cancel Train\n3.View All train\n4.Logout\n"))
        if n == 1:
            ntvalid = 0
            tname = input("\nEnter train name: ")
            tno = input("\nEnter train number: ")
            f = open("train", "r")
            for lines in f:
                avltrain = lines.split("|")
                if avltrain[1] == tno:
                    print("\nTrain Number Already exist")
                    input()
                    ntvalid = 1
            tdate = datetime.datetime(int(input("Enter year: ")), int(input("Enter Month: ")), int(input("Enter Day: "))).date()
            if ntvalid == 0:
                if tdate <= datetime.datetime.now().date():
                    print("Date Invalid")
                    input()
                    ntvalid = 1
            if ntvalid == 0:
                tdate = str(tdate)
                source = input("Enter the starting point: ").lower()
                dest = input("Enter the destination: ").lower()
                deptt = input("Enter Departure Time: ")
                reachtime = input("Enter Journey Time: ")
                totalseat = int(input("Enter the Total no of seats: "))
                price = str(int(input("Enter the price: ")))
                print("Train added Succesfully")
                f = open("train", "a")
                f.write(tname+"|"+tno+"|"+tdate+"|"+source+"|"+dest+"|"+deptt+"|"+reachtime+"|"+str(totalseat)+"|"+str(totalseat)+"|"+price+"$\n")
        elif n == 2:
            can = 0
            ctrainno = input("Enter the train no for which you want to cancel the train")
            f = open("train", "r")
            trains = f.readlines()
            f.close()
            if len(trains) > 0:
                f = open("train", "w")
                for t in trains:
                    ctr = t.split("|")[1]
                    if ctr != ctrainno:
                        f.write(t)
                    else:
                        can = 1
                if can == 1:
                    ctr = ""
                    f.close()
                    f = open("booking", "r")
                    book = f.readlines()
                    f.close()
                    f = open("booking", "w")
                    fp = open("messages", "a")
                    for b in book:
                        bs = b.split("|")
                        ctr = bs[2].strip("$\n")
                        if ctr != ctrainno:
                            f.write(b)
                        else:
                            fp.write(bs[0]+"|"+"Booking for train no "+ctr+" for "+bs[1]+" has been cancelled$\n")
                    f.close()
                    fp.close()
                    print("Train on ", ctr, " Cancelled")
                else:
                    print("No train with the given train no")
                    input()
            else:
                print("No train avaliable to cancel")
                input()
        elif n == 3:
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
                print("\nNo Trains Avaliable")
                input()
        else:
            print("Logged out")
            input()
            return