

def main():
    dfile = "challenge6Files/"
    bname = "90052"
    fext = ".txt"
    fname = dfile + bname + fext
    while(bname):
        with open(fname, mode="rt", encoding='utf-8') as f:
            for rec in f:
                next_rec = rec.split()
                if next_rec[-1].isdigit():
                    bname = next_rec[-1]
                    print("Now processing {}".format((fname)))
                else:
                    bname = 0
                    print(next_rec)
                    break
        fname = dfile + bname + fext
    print("Done")


if __name__ == '__main__':
    main()