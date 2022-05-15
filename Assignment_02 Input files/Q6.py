#QUES6

print('Ans6')


def countFlips(a, b):
     
                                                #initially flips is equal to 0
    flips = 0
     


                                              
    while(a > 0 or b > 0):                        # & each bits of a && b with 1
      t1 = (a & 1)                                 # and store them if t1 and t2
      t2 = (b & 1)                                     
    
      if(t1 != t2):                             # if t1 != t2 then we will flip that bit          
            flips += 1
             
      a>>=1                                 # right shifting a and b
      b>>=1
     
    return flips



a = int(input('enter value of a:\n'))

b = int(input('enter value of b:\n'))

print(countFlips(a, b))