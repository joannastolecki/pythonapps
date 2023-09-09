import string
import random

def gen():
    s1=string.ascii_uppercase  # generates: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(s1)
    s2=string.ascii_lowercase  # generates: abcdefghijklmnopqrstuvwxyz
    print(s2)
    s3=string.digits            #generates: 0123456789
    print(s3)
    s4 = string.punctuation     #generates: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    print(s4)
    
    passLen = int(input(('Enter the passwd length')))
    
    s = [] # create blank list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print(s)
    """all is in list: 
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
 """
    random.shuffle(s)
    print(s)
    pas = ("".join(s[0:passLen]))      # laczy znaki
    print(pas)
    
gen()