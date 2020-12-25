class Crypting:
    """ Encrypts or Decrypts the given string.
        Methods : (1) Encrypt (2) Decrypt
        Key Arguments for methods : word -- String
    """
    def Encrypt(word):
        temp=""
        for letter in word:
            temp = temp + chr(ord(letter) + 5)
        return(temp)
    
    def Decrypt(word):
        temp=""
        for letter in word:
            temp = temp + chr(ord(letter) - 5)
        return(temp)

if __name__ == "__main__":
    # username = input("Enter the username word : ")
    # password = input("Enter the password word : ")
    username = "admin"
    password = "{nxmfpm"
    
    print("ENCRYPTING") # encrypting admin and password
    print(username, ":", Crypting.Encrypt(username))
    print(password, ":", Crypting.Encrypt(password))
    
    print("DECRYPTING") # Decrypting back to admin and password
    # print(username, ":", Crypting.Decrypt("firns"))
    # print(password, ":", Crypting.Decrypt("ufxx|twi"))
    print("firns", ":", Crypting.Decrypt("firns"))
    print("ufxx|twi", ":", Crypting.Decrypt("xfi"))
    # print(Crypting.Decrypt(password))
    