def lassoletter(ltr, shftAmt):
   
   ltrCode = ord(ltr.lower())
   
   Ascii = 97

   alphabetSize = 26

   trueCode = Ascii + (((ltrCode - Ascii) + shftAmt) % alphabetSize)
   
   decodedLtr = chr(trueCode)
   return decodedLtr
