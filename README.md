# Readable Password
This password generator generates a easy-to-remember readable pronounceable passwords with password standards considerations

## Installation
```
pip install readable_password
```

## Usage
```
from readable_password import readable_password as rpwd
print(rpwd.readable_password(length=10))
print(rpwd.readable_password(length=8))
print(rpwd.readable_password(length=8, incl_digit=False))
print(rpwd.readable_password(length=8, incl_digit=False, incl_punc=False))
print(rpwd.readable_password(length=8, incl_upper=False, incl_digit=False, incl_punc=False))

```

## Sample output
```
Diwegu718@
Lihu604!
Hejuros?
Jegibeni
mutemoxo
```
## Password tips
```
Passwords must include at least three of the four following types of characters
English uppercase letters (A through Z).
English lower case letters (a through z).
Numbers (0 through 9).
Special characters and punctuation symbols (Example: _, -. +, =,!, @, %, *, &, ”, :, ., or /).
Do not use the following characters \ , ~  or < .
Do not use a space or tab.
```
