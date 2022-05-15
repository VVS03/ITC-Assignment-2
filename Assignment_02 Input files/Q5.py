#QUES5

    
print('Ans 5')


L1 = int(input('\nEnter the 1st length:\n'))
L2 = int(input('\nEnter the 2nd length:\n'))
L3 = int(input('\nEnter the 3rd length:\n'))

if L1>(L2+L3) or L2>(L1+L2) or L3>(L1+L2):
    print('\n No,entered three lengths can not form a triangle')
else:
    print('\n Yes,entered three lengths can form a triangle')
