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
    downalph=alph.lower()
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=newalph[a]
            if char==char2:
                decrypted+=alph[a]
            elif char.lower()==char2.lower():
                decrypted+=downalph[a]
    for i in range(len(alph)):
        newalph2 += alph[(i+shift)%len(alph)]
    for i in range(len(text)):
        char=text[i]
        for a in range(len(alph)):
            char2=newalph2[a]
            if char==char2:
                decrypted2+=alph[a]
            elif char.lower()==char2.lower():
                decrypted2+=downalph[a]
    print(f"Decrypted({-shift}): {decrypted2}")
    print(f"Decrypted({shift}): {decrypted}")