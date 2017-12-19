
def translate_c_way(message):
    asc_dict={}
    # build map
    for i in range(97,123):
        if i == 121:  # map 'y' to 'a'
            asc_dict[chr(i)] = chr(97)
        elif i == 122:  # map 'z' to 'b'
            asc_dict[chr(i)] = chr(98)
        else:
            asc_dict[chr(i)] = chr(i+2)
    # translate
    for c in message:
        if c in asc_dict:
            print(asc_dict[c], end='')
        else:
            print(c, end='')
    print()


def translate_python_way(message, offset):
    #s1 = "abcdefghijklmnopqrstuvwxyz"
    # Create a srt or ascii values from a-z
    # loop over ascii range from a-z
    # cast it to ascii, in a list comprehension
    # create a string of the list
    s1 = ''.join([chr(i) for i in range(97, 123)])
    s2 = s1[offset:] + s1[:offset]
    t = str.maketrans(s1, s2)
    print(message.translate(t))


if __name__ == '__main__':
    s = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
    rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw
    fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr
    gq qm jmle. sqgle qrpgle.kyicrpylq()
    gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    #translate_c_way(s)
    translate_python_way(s, offset=2)
    translate_python_way("map", offset=2)
