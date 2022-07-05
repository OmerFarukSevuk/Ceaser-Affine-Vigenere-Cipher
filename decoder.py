def Ceaser():
    decrypted=""
    decrypted2=""
    shift=int(input("Shift: "))
    alph=input("Alphabet: ").upper()
    text=input("Text: ")
    newalph=""
    newalph2=""
    for i in range(len(alph)):
        newalph += alph[(i-shift)%len(alph)]
    lowalph=alph.lower()
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=newalph[a]
            if char==char2:
                decrypted+=alph[a]
            elif char.lower()==char2.lower():
                decrypted+=lowalph[a]
    for i in range(len(alph)):
        newalph2 += alph[(i+shift)%len(alph)]
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=newalph2[a]
            if char==char2:
                decrypted2+=alph[a]
            elif char.lower()==char2.lower():
                decrypted2+=lowalph[a]
    print(f"Decrypted({-shift}): {decrypted2}")
    print(f"Decrypted({shift}): {decrypted}")
def Affine():
    cipher=""
    key_a=int(input("Key A: "))
    key_b=int(input("Key B: "))
    alph=input("Alphabet: ").upper()
    text=input("Text: ")
    lowalph=alph.lower()
    z=0
    while not((key_a*z)%len(alph)==1):
        z+=1
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=alph[a]
            if char==char2:
                cipher+=alph[(z*(a-key_b))%len(alph)]
            elif char.lower()==char2.lower():
                cipher+=lowalph[(z*(a-key_b))%len(alph)]
    print(f"Decrypted: {cipher}")
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
                        cipher+=alph[((a-b)+26)%len(alph)]
            elif char.lower()==char3.lower():
                for b in range(len(alph)):
                    char4=alph[b]
                    if char4.lower()==char2.lower():
                        cipher+=lowalph[((a-b)+26)%len(alph)]
    print(f"Encrypted: {cipher}")