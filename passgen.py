import random
import string 


def gen_pw(length=12):
    char = string.ascii_letters + string.digits + string.punctuation


    pw = "".join(random.choice(char) for _ in range(length) )
    return pw 


def cus_cs(length = 16, dig = True, sym = True):
    cg = string.ascii_letters


    if dig:
        cg += string.digits

    if sym:
        cg += string.punctuation

    pw = "".join(random.choice(cg) for _ in range(length) )
    return pw

my_pass = cus_cs(length = 16, dig = True, sym = False)
print("my pass", my_pass)