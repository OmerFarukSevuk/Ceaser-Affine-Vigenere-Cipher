def Ceaser():
    cipher=""
    shift=int(input("Shift: "))
    alph=input("Alphabet: ").upper()
    text=input("Text: ")
    newalph=""
    for i in range(len(alph)):
        newalph += alph[(i+shift)%len(alph)]
    newdownalph=newalph.lower()    
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=alph[a]
            if char==char2:
                cipher+=newalph[a]
            elif char.lower()==char2.lower():
                cipher+=newdownalph[a]
    print(f"Encrypted: {cipher}")

