ch = input("enter a character : ")
if len(ch) != 1 :
    print("enter a single character only ")
elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' :
    print("entered character is an alphabet ")
elif '0' <= ch <= '9' :
    print("entered character is a digit ")
else :
    print ("entered character is a special character ")
