print ("Welcome to the vending machine change maker program")
print ("Change maker initialized.")
print ("Stock contains:")
print ("  25 nickels")
print ("  25 dimes")
print ("  25 quarters")
print ("  0 ones")
print ("  0 fives")

n = 25
d = 25
q = 25
o = 0
f = 0

price_str = input ("Enter the purchase price (xx.xx) or 'q' to quit:")
price_float = float (price_str)

while True:
    if price_float*100 % 5 != 0 or price_float < 0:
        print ("Illegal price: Must be a non-negative multiple of 5 cents.")
        
    else:
        print ("Menu for deposits:")
        print (" 'n' - deposit a nickel")
        print (" 'd' - deposit a dime")
        print (" 'q' - deposit a quarter")
        print (" 'o' - deposit a one dollar bill")
        print (" 'f' - deposit a five dollar bill")
        print (" 'c' - cancel the purchase")
        print (" ")    

        while price_float>0:
            print ("Payment due: ",int (price_float),"dollars and",round ((float (price_float) - int (price_float))*100),"cents")
            deposit = input ("Indicate your deposit: ")
            if deposit != 'n' and deposit != 'd' and deposit != 'q' and deposit != 'o' and deposit != 'f' and deposit != 'c':
                print ("Illegal selection: ")
            elif deposit == 'n':
                price_float = (price_float - 0.05)
                n = n + 1
            elif deposit == 'd':
                price_float = (price_float - 0.10)
                d = d + 1
            elif deposit == 'q':
                price_float = (price_float - 0.25)
                q = q + 1
            elif deposit == 'o':
                price_float = (price_float - 1.00)
                o = o + 1
            elif deposit == 'f':
                price_float = (price_float - 5.00)
                f = f + 1
            elif deposit == 'c':
                    print ("Cancel the purchase")

        change_o = 0
        change_q = 0
        change_d = 0
        change_n = 0

        while price_float < 0:
            if price_float <= -1.00 and o > 0:
                price_float = price_float + 1.00
                o = o - 1
                change_o = o + 1
            elif price_float <= -0.25 and q > 0:
                price_float = price_float + 0.25
                q = q - 1
                change_q = change_q + 1
            elif price_float <= -0.10 and d > 0:
                price_float = price_float + 0.10
                d = d - 1
                change_d = change_d + 1
            elif price_float <= -0.05 and n > 0:
                price_float = price_float + 0.05
                n = n - 1
                change_n = change_n +1
            else:
                break
                
        print ("Please take the change below.")
        if change_q > 0:
            print (change_q," quarters")
        elif change_d > 0:
            print (change_d," dimes")
        elif change_n > 0:
            print (change_n," nickels")
        elif change_q == 0 and change_d == 0 and change_n == 0:
            print ("No change due.")
        if price_float < 0:
            print ("See store manager for remaining refund.")
            print ("Amount due is: ",int (price_float)*-1,"dollars and",round ((float (price_float) - int (price_float))*-100),"cents")
        

        print ("Stock contains:")
        print (" ",n," nickels")
        print (" ",d," dimes")
        print (" ",q," quarters")
        print (" ",o," ones")
        print (" ",f," fives")
        
    price_str = input ("Enter the purchase price (xx.xx) or 'q' to quit:")
    price_float = float (price_str)
    
