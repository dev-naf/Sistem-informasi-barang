from hashlib import sha256

class Encrypt():
    def process(plainText):
        plainText = plainText
        plainTextEncode = plainText.encode()
        return sha256(plainTextEncode)

saklar = True
i =0
while(saklar):
    if i ==2 :
        saklar = False
    print("Putaran ke ", i)
    i +=1