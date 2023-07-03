import random
import string
import sys


def gen_pass(length):
    return "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                                 length))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            print(gen_pass(int(sys.argv[1])))
        except Exception as e:
            print("ERROR:\t" + e + "\nEnter the number of character for the password")
    else:
        print(gen_pass(random.randint(12, 16)))
