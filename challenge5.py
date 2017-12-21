import pickle


def main():
    pdata = "banner.p"
    with open(pdata, mode='rb') as pickle_in:
        data = pickle.load(pickle_in)
        for l in data:      # list 1D
            for t in l:     # tuple 2D
                print(t[0]*int(t[1]), end='')
            print()
        print("Done")

if __name__ == '__main__':
    main()