import sys
import string

in_put = sys.argv[1]
msg = input('What is the message?: ')
msg = msg.upper()
msg = msg.replace(' ','')
translate_msg = msg.translate(str.maketrans('','',string.punctuation))
ress = ' '
blocks = 0
shift = 0
n = 0
char = ''
for i in range(len(translate_msg)):
    char = translate_msg[i]
    n = ord(char)
    
    if (n + int(in_put)) > 90:
        shift = (n + int(in_put)) - 26
    else:
        shift = n + int(in_put)
    
    if (i % 5 == 0) and (i > 0):
        ress = ress + ' '
        blocks += 1
        
    if blocks == 10:
        #echo ress
        print (ress)
        blocks = 0
        ress = ' '
        
    ress += chr(shift)
    
#echo ress
print(ress)

