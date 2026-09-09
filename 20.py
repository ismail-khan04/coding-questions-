ch = input("enter a character : ")
if len(ch) != 1 :
    print ("enter only single character")
elif ch in 'aeiouAIEOU' :
    print("character is a vowel")
else :
    print ("character is a consonant")