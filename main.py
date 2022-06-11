import encoder
import decoder
while True:
    print("Affine, Ceaser, Vigenère Cipher")
    print("""
1-Affine Cipher Encoder
2-Affine Cipher Decoder
3-Ceaser Cipher Encoder
4-Ceaser Cipher Decoder
5-Vigenère Cipher Encoder
6-Vigenère Cipher Decoder    
""")
    event = int(input("Select Event: "))

    if event==1:
        encoder.Affine()
    elif event==2:
        decoder.Affine()
    elif event==3:
        encoder.Ceaser()
    elif event==4:
        decoder.Ceaser()
    elif event==5:
        encoder.Vigenere()
    elif event==6:
        decoder.Vigenere()
    else:
        print("Invalid Number")