import re

def find_message():
    pattern = re.compile(r"[A-Z]{3}")
    with open("challenge3_data.hmtl", mode='rt', encoding='utf-8') as data:
        # Loop over file
        for rec in data:
            hit = re.search(pattern, rec)
            print(hit)

if __name__ == '__main__':
    find_message()
