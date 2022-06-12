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
Affine()