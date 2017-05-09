
def getFirstLetter_Frequency(text):

    text = text.upper()
    text = " " + text
    chararacterFrequency_FirstLetter = {}

    for i in range(len(text)):
        if text[i] == " ":
            if text[i+1] not in chararacterFrequency_FirstLetter.keys():
                chararacterFrequency_FirstLetter[text[i+1]] = 0
                
            chararacterFrequency_FirstLetter[text[i+1]] += 1
            #print(chararacterFrequency_FirstLetter)

            
    return chararacterFrequency_FirstLetter

print(getFirstLetter_Frequency("The quick brown fox jumps over the lazy dog"))
