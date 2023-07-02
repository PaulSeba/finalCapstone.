


def encrypt(txt, key):
    encrypted_txt = ""
    n = len(txt)
    key = key%26 #I decrease the key - when it is larger than the alphabet... .

    for i in range(n): #for each char in message...

        character = txt[i]
        ASCI_code = ord(character) #I change char to ASCI
        if ((ASCI_code>96) and (ASCI_code<123)):  # a-asci code=97, z-asci code = 123 - so when we have
            # between this values, we have small chars. I can use fun islower(), but I use my condition.
            #In this case - there are small letters.

            # ASCI code minus code of 'a' - this is position on alphabet - for small letters
            alphabet_index = ASCI_code - ord('a')

            #Here we change position - we add key - with modulo,
            # because after encrypt [Z] we back to begin of alphabet.... and we must add 'a' pos
            # - because we need to back for normall ASCI codee
            char_changed = (alphabet_index + key) % 26 + ord('a')

            #Here from ASCI we go out to normall txt
            encrypted_txt = encrypted_txt + chr(char_changed)


        #Here everything simillar like before - but for upper cases...
        elif  ((ASCI_code>64) and (ASCI_code<91)):
            alphabet_index = ASCI_code - ord('A')

            char_changed = (alphabet_index + key) % 26 + ord('A')
            encrypted_txt = encrypted_txt + chr(char_changed)
        else:
            encrypted_txt += character
    return encrypted_txt


def decrypt(txt, key):
    decrypted_txt = ""
    n = len(txt)
    key = key % 26

    for i in range(n):

        character = txt[i]
        ASCI_code = ord(character)

        #Everything like in encrypt - function, but we substract key.
        # In one place it is the other way round.
        if ((ASCI_code > 96) and (ASCI_code < 123)):
            alphabet_index = ASCI_code - ord('a')
            char_changed = (alphabet_index - key) % 26 + ord('a')
            decrypted_txt = decrypted_txt + chr(char_changed)

        elif ((ASCI_code > 64) and (ASCI_code < 91)):
            alphabet_index = ASCI_code - ord('A')
            char_changed = (alphabet_index - key) % 26 + ord('A')
            decrypted_txt = decrypted_txt + chr(char_changed)
        else:
            decrypted_txt += character
    return decrypted_txt

#This is a helper function to ensure that the key value is correctly entered by the user.
#I used it in my previous programs.
def InputNumberInt(num_str):

    # Input  and check int - param - information string - for example :" How many years......".
    # In this way we can use this functiom im many situations
    while True:
        try:
            num = int(input(num_str))
            return (num)

        except ValueError:
            print("Improperly value - only int..")


def Messages ():
    print("The program encrypts the text using the Caesar Cipher. "
          "Spaces, special chars will be not encrypted.")
    print("//////////////////////////////////////////////////////////////////////////////////////")
    print("\n")
    key = 15 #In homework task key is costans - 15... - but  - I added alternative improve.
    #When you remove comments on these next lines - you will input key and app will work on different keys

    # we can use it to input key value - alternative
    # st = "Input key value as integer, please:"
    # key = InputNumberInt(st)
    message = input("Print text to encrypt, please")
    print("\n")
    print("//////////////////////////////////////////////////////////////////////////////////////")

    s = encrypt(message, key)
    x = decrypt(s, key)
    print("Result:")
    st = 'Message before encryption:' + message
    print(st)
    print("\n")
    st = "Encrypted message:" + s
    print(st)
    print("\n")
    st = "Decrypted message:" + x
    print(st)


#-----------------------------------------------------------------------------------------------------------

Messages()


