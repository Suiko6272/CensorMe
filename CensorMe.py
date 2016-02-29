#! python3.3


    #####################
    #   Censor Me       #
    #       V1.0        #
    #   By Suiko6272    #
    #####################

    #Nick was here

#Returns (str)censoredText
def censorDocument(OUTPUT=1, docFileName="secretdoc.txt", keyFileName="keys.txt"):
    import sys, re, string

    DEV = 0 #Enables print outs for debugging

    # Read in files
    with open(keyFileName, "rt") as in_file:    #TODO: error handling
        keys = in_file.read()

    with open(docFileName, "rt") as in_file:
        text = in_file.read()


    A = re.compile(r'"(.*?)"') #gets "*"        #TODO: combine A & B to make 1 regex findall
    B = re.compile(r"'(.*?)'") #gets '*'
    W = re.compile(r"([^,\W]+)") #gets all words
    

    p1 = A.findall(keys)
    p2 = B.findall(keys)
    censoedPhrases = []
    #Could instead use a string to create a regex of r"phrase(?={conditions})|phrase(?={conditions})|ect"
    for phrase in p1:
        censoedPhrases.append(phrase)
    for phrase in p2:
        censoedPhrases.append(phrase)

    #Remove phrases from keys so only keyWords remain, else keyWords would contain phrases
    keyWords = re.sub(A, '', keys)
    keyWords = re.sub(B, '', keyWords)
    censoredWords = W.findall(keyWords)


    if DEV:
        print("Phrases: {p}\nKey-Words: {w}"
            .format(p=censoedPhrases, w=censoredWords))

    censor = 'XXXX';
    censoredText = text;
    exactMatch = 1;
    if exactMatch:
        for phrase in censoedPhrases:
            regexStr = r'((?<=\s|\W)' + phrase + r'(?=\s|\W|\Z))'
            #regexStr: check for leading & trailing symbol or white space or EOF
            A = re.compile(regexStr, re.IGNORECASE)
            censoredText = re.sub(A, censor, censoredText)
        for word in censoredWords:
            regexStr = r'((?<=\s|\W)' + word + r'(?=\s|\W|\Z))' 
            A = re.compile(regexStr, re.IGNORECASE)
            censoredText = re.sub(A, censor, censoredText)
    else: #below would make key 'teen' hit and sub 'teenager' into 'XXXXager'
        for phrase in censoedPhrases:
            censoredText = re.sub(phrase, censor, censoredText)
        for word in censoredWords:
            censoredText = re.sub(word, censor, censoredText)

    if DEV:        
        print("-------------------------------")
        print(censoredText)
        print("-------------------------------")

    if OUTPUT:
        # Write out censored File
        censoredFile = "Censored_" + docFileName
        with open(censoredFile, "wt") as out_file:
            out_file.write(censoredText)
        return censoredText
    else:
        return censoredText



def run():
    if censorDocument():
        print("Document Censored")
    else:
        print("Unkown Error")
