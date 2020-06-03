def displaymsg(username):
    f = open("messages", "r")
    lines = f.readlines()
    f.close()
    mb = ["\nMessages"]
    for l in lines:
        cl = l.split("|")
        cl[1] = cl[1].strip("$\n")
        if cl[0] == username:
            mb.append(cl[1])
    if len(mb) > 1:
        for i in mb:
            print(i)
        f = open("messages", "w")
        for l in lines:
            cl = l.split("|")
            if cl[0] != username:
                f.write(l)
        f.close()
    else:
        print("\nNo messages")