def incavail(trainno):
    f = open("train", "r")
    lines = f.readlines()
    f.close()
    f = open("train", "w")
    for l in lines:
        cl = l.split("|")
        if cl[1] == trainno:
            cl[8] = str(int(cl[8])+1)
            l = cl[0]+"|"+cl[1]+"|"+cl[2]+"|"+cl[3]+"|"+cl[4]+"|"+cl[5]+"|"+cl[6]+"|"+cl[7]+"|"+cl[8]+"|"+cl[9]
            f.write(l)
        f.write(l)
    f.close()