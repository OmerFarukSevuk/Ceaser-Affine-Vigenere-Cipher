def Ceaser():
    cipher=""
    shift=int(input("Shift: "))
    alph=input("Alphabet: ").upper()
    text=input("Text: ")
    newalph=""
    for i in range(len(alph)):
        newalph += alph[(i+shift)%len(alph)]
    newlowalph=newalph.lower()    
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=alph[a]
            if char==char2:
                cipher+=newalph[a]
            elif char.lower()==char2.lower():
                cipher+=newlowalph[a]
    print(f"Encrypted: {cipher}")
def Affine():
    cipher=""
    key_a=int(input("Key A: "))
    key_b=int(input("Key B: "))
    alph=input("Alphabet: ").upper()
    text=input("Text: ")
    lowalph=alph.lower()
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=alph[a]
            if char==char2:
                cipher+=alph[((a*key_a)+key_b)%len(alph)]
            elif char.lower()==char2.lower():
                cipher+=lowalph[((a*key_a)+key_b)%len(alph)]
    print(f"Encrypted: {cipher}")
def Vigenere():
    cipher=""
    alph=input("Alphabet: ").upper()
    key=input("Key: ")
    text=input("Text: ")
    lowalph=alph.lower()
    while not len(text)==len(key):
        key+=key
        if len(key)>len(text):
            z=len(key)-len(text)
            key=key[:(len(key)-z)]
    for i in range(len(text)):
        char=text[i]
        char2=key[i]
        for a in range(len(alph)):
            char3=alph[a]
            if char==char3:
                for b in range(len(alph)):
                    char4=alph[b]
                    if char4==char2:
                        cipher+=alph[(a+b)%len(alph)]
            elif char.lower()==char3.lower():
                for b in range(len(alph)):
                    char4=alph[b]
                    if char4.lower()==char2.lower():
                        cipher+=lowalph[(a+b)%len(alph)]
    print(f"Encrypted: {cipher}")