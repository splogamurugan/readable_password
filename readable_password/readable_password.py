from string import ascii_lowercase
from string import punctuation
from string import digits
from random import sample
from random import choice
from functools import partial
from math import ceil

def readable_string(n:int):
    vow = ['a', 'e', 'i', 'o', 'u']
    cons = list(set(ascii_lowercase).difference(set(vow)))
    s = [choice(cons) if _%2==0 else choice(vow) for _ in range(n)]
    return "".join(s)

def regulated_punc():
    return "".join([s for s in punctuation if s not in " \~<.,"])

def readable_password(length=10, *, incl_upper=True, incl_lower=True, incl_punc=True, incl_digit=True):
    config = {
        "min_length": 6,
        "punc_perc": .1,
        "digit_perc": .3
    }

    length = length if length>config['min_length'] else config['min_length']
    incl_punc_perc = config['punc_perc'] if incl_punc else 0
    incl_digit_perc = config['digit_perc'] if incl_digit else 0
    incl_lower_perc = 1 - (incl_punc_perc + incl_digit_perc)

    alp_perc   =  ceil(length * incl_lower_perc)
    punc_perc  = ceil(length * incl_punc_perc)
    digit_perc = ceil(length * incl_digit_perc)
    alp_perc   = alp_perc - ((alp_perc + punc_perc + digit_perc) - length)

    s = readable_string(alp_perc)
    s = s.title() if incl_upper else s
    s = s + "".join(sample(digits,  digit_perc))
    s = s + "".join(sample(regulated_punc(),  punc_perc))
    return s

eight_char_password = partial(readable_password, length=8)
standard_password = partial(readable_password, length=10)
twelve_char_password = partial(readable_password, length=12)