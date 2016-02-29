#! python3.3
#simple click to run app
import CensorMe

#CensorMe.censorDocument('OUTPUT', 'docFileName', 'keyFileName')
#Defaults to 1, keys.txt, secrectdoc.txt
#Always returns censoredText
censoredText = CensorMe.censorDocument(0)
# Write out censored File
if not censoredText == None:
    with open('appCensor.txt', "wt") as out_file:
        out_file.write(censoredText)
else:
    print("Error: No text returned")    #Should not occur

#weeeeeeeeeeeeee fuckytou]

