def lassoLetter(ltr, shftAmt):
   
   #coverting letter into lowercase and then
   #fetching their ascii value
   ltrCode = ord(ltr.lower())
   
   #storing ascii value of 'a' in Ascii
   Ascii = 97
   #alphabet size i.e. 26
   alphabetSize = 26
   
   # Since we've to take into account the looping around the alphabets
   trueCode = Ascii + (((ltrCode - Ascii) + shftAmt) % alphabetSize)
   
   # Converting the ASCII number to the character or letter
   decodedLtr = chr(trueCode)
   return decodedLtr

def lassoWord(word, shft):
    
    # To update this variable each time a new word is passed
    decodedWord = ""
    
    #looping through each word
    for ltr in word:
        #invoking lassoletter to get updated value of each letter
        decodedLtr = lassoLetter(ltr, shft)

        #adding into decodedWord string
        decodedWord += decodedLtr

    return decodedWord

decryptedStr = lassoWord('Hello', 2)
print(decryptedStr)
