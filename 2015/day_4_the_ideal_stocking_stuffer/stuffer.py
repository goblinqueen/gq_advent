import hashlib


def hash_fits(in_i):
    b_string = (INPUT + str(in_i)).encode()
    return hashlib.md5(b_string).hexdigest()[:6] == "000000"


if __name__ == '__main__':
    INPUT = "bgvyzdsv"
    # INPUT = "abcdef"
    i = 0
    fits = hash_fits(i)
    while not fits:
        i += 1
        fits = hash_fits(i)
    print(i)
