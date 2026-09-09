marks=60
attendance=75
income=200000
mark = int(input("enter marks percentage : "))
att = int (input("enter attendance percentage : "))
fmly_incme = int (input("enter annual family income : "))
if mark >= marks and att >= attendance and fmly_incme <= income :
    print ("eligible for scholarship")
else :
    print("not eligible for scholarship")