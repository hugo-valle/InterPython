def find_rare():
    with open("challenge2_data.html", mode='rt', encoding='utf-8') as data:
        # Loop over file
        for rec in data:
            # Loop over line
            for c in rec:
                if c.isalpha():
                    print(c, end='')
        print()


if __name__ == '__main__':
    find_rare()