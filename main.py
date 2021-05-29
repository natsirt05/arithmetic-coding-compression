#!/usr/bin/python3
from collections import Counter
def bin2float (b):
    s, f = b.find('.')+1, int(b.replace('.',''), 2)
    return f/2.**(len(b)-s) if s else f


def test():
    f = open('my_file', 'wb')
    bi = [0b10001000, 0b01000100]

    by = bytes(bi)
    f.write(by)
    f.close()

    f = open('my_file', 'rb')
# fr = f.read()
def genbits():
    # This returns each bit individually from all the bytes of the file
    for c in fr:
        # Go into each bytes
        for i in range(8):
            # (0x80 >> i) Simulate a byte that in binary is 0b1, 0b01, 0b001 where
            # the 1 is each time in one spot

            # (c & (0x80>>i)) != 0 This checks c has a 1 in the spot where 0x80>>i has 
            # a one. If it has a one in that spot it will return the number, which has a 
            # one, therefore, is not 0. Then you convert the bool into an int. with 0 = false and 
            # true = 1
            yield int((c & (0x80>>i)) != 0)
    f.close()

# outputs = genbits()

# Make a encoder, you'll need a batch size

f = open("my_file", "r").read()
# f = f[:2]
l = len(f)

def write():
    return

def get_table():
    table = {}
    table = Counter(list(f))

    last = 0
    l = len(f)
    for key in table:
        table[key] /= l
        table[key] += last
        temp = table[key]
        table[key] = (last, temp) # Keep a range of (start, end)
        last = temp
    return table

def new_point(s, e, p):
    # n = 
    r = (e - s) * p + s
    return r

def encode(f):
    print("encoded: ", f)
    SCALE = 1
    table = get_table()
    l = len(f)
    start = 0
    end = 1
    i = 1
    ranges = table.items()
    print(len(f))
    for c in f:
        c = table[c]
        start = new_point(start, end, c[0])
        end = new_point(start, end, c[1])
        # Not working yet
        start, end, SCALE = normalize(start, end, SCALE)

    print("f: ", start)
    return start, SCALE

def reverse_table(table):
    new_table = {}
    for key in table:
        new_table[table[key]] = key
    return new_table

def normalize(start, end, SCALE):
    current = 0
    equal = True
    decimal_i = 1
    result = [start, end]

    while True:
        v1 = str(start)
        v2 = str(end)

        i1 = v1.find(".")
        i2 = v2.find(".")

        try:
            c1 = v1[i1 + decimal_i]
            c2 = v2[i2 + decimal_i]
        except IndexError:
            break

        if c1 != c2:
            break
        print("v1: ", v1)
        print("v2: ", v2)
        if c1 != "0":
            break

        common = int(c1) / pow(10, decimal_i)

        result[0] = (start - common) * 10
        result[1] = (end - common) * 10
        SCALE *= 10
        decimal_i += 1
        print("normalized")
        #FIXME: this works but it doesn't yet integrate with the encoder nor the decoder

    return result[0], result[1], SCALE



def new_point2(s, e, p):
    w = e - s
    return w * p + s


def decode(encoded, l, SCALE):
    print("SCALE: ", SCALE)
    table = get_table()
    start = 0
    end = 1 * SCALE
    i = 0
    decoded = ""

    while i < l:
        for key in table.keys():
            r = table[key]
            s, e = r[0], r[1]
            if encoded >= new_point2(start, end, s) and encoded < new_point2(start, end, e):
                decoded += key
                start = new_point(start, end, s)
                end = new_point(start, end, e)
                break

        i += 1
    return decoded


def get_decimals(n):
    s = str(n)
    return s[::-1].find('.')


# Decoding theory
# Check each iteration
# --> Take number and check where it fits in the ranges
# --> then update ranges
# --> check again

a, SCALE = encode(f)
print("decoded: ", decode(a, l, SCALE))




# To work with long types
