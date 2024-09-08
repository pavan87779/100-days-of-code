
def caser(orginal_txt,shift_num,direction):
    output_txt = ""
    for i in orginal_txt:
        if direction=='decode':
            shift_num *= -1
        shifted_position = alphabet.index(i) + shift_num
        shifted_position %= len(alphabet)
        output_txt += alphabet[shifted_position]
    print(f"The generated text is {output_txt}")
e_r_d=input("Type 'encode' to encrypt. Type 'decode' to decrypt:").lower()
word=input("Type your message: ").lower()
shift=int(input("Type shift number: "))

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



caser(orginal_txt=word,shift_num=shift,direction=e_r_d)

