def days_in_month(month) :
    match month :
       case 1 | 3 | 5 | 7 | 8 | 10 | 12  :
        return " 31 days "
       case 4 | 6 | 9 | 11  :
          return " 30 days "
       case _ :
          return 'Invalid Input'

month = int(input("enter the month number to find its days : "))
print(days_in_month(month))
        
    

        