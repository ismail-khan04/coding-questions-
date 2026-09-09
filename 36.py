item = input("enter item : ")
cp = int(input(' Enter Cost Price : '))
sp = int(input(' Enter Selling Price : '))
if sp > cp :
    print ('profit of rs',sp-cp)
elif cp > sp:
    print('loss of rs',cp-sp)
else :
    print ("no profit and no loss ")




