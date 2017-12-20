import re

def find_message():
    pattern = re.compile(r"[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")
    with open("challenge3_data.hmtl", mode='rt', encoding='utf-8') as data:
        # Loop over file
        count = 1
        for rec in data:
            # See re.math(), re.search(), re.findall()
            hit = re.findall(pattern, rec)
            for h in hit:
                print(h[4], end='')
                count += 1
        print()
        print("Found {} hits".format(count))

if __name__ == '__main__':
    find_message()
