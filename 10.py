ch = input('Enter a character :')
if len(ch) != 1 :
    print (" enter a single character only ")
elif 'A' <= ch <='Z' :
    print ("Entered character is UPPERCASE ")
elif 'a' <= ch <= 'z':
    print ("Entered character is LOWERCASE ")
elif '0' <= ch <= '9' :
    print ("Entered character is DIGIT ")
else :
    print ("Entered character is SPECIAL CHARACTER ")