def find_rare():
    with open("challenge2_data.html") as data:
        for rec in data:
            print(rec)


if __name__ == '__main__':
    find_rare()