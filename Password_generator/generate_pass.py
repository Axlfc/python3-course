import random
import string


def gen_pass(length):
    return "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                                 length))


if __name__ == '__main__':
    print(gen_pass(16))
