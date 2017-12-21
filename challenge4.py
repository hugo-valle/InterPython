from urllib.request import urlopen


def main():
    address_base = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    number = "12345"
    address = address_base + number
    while(number):
        with urlopen(address) as f:
            for line in f:
                next_rec = line.decode('utf-8').split(" ")
            if next_rec[-1].isdigit():
                number = next_rec[-1]
                print("Now processing {}".format((address)))
            elif next_rec[-1] == "going.":
                number = str(int(number)//2)
            else:
                number = 0
                print(next_rec)
                break
        address = address_base + number
    print("Done")

if __name__ == '__main__':
    main()