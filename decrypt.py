def lassoletter(ltr, shftAmt):
    #converting letter to lower case and
    #fetching it's ascii value
    letterCode = ord(ltr.lower())
    
    #adding the shift to ascii value
    decodedLetter = letterCode + shftAmt

    return decodedLetter

