fname = raw_input('Enter your first name: ')
lname = raw_input('Enter your last name: ')
print 'Enter your date of birth: '
A = raw_input('Month from (1-12) Mar=1, Apr=2...Jan=11 and so on? ')
A = int(A)
if A < 1 or A > 12:
    print'Month should be from 1 to 12'
    exit()

B = raw_input('Day? from 1-31')
B = int(B)

if B < 1 or B > 31:
    print'Day should be between  to 1-31'
    exit()
yr = raw_input('Year? ')


if A == 11 or A == 12:
   yr = int(yr)-1
   yr = str(yr)
   C = yr[2:]
   D = yr[:2]
   
else :
    C = yr[2:]
    D = yr[:2]
   

    
W = (13*A-1)/5
X = int(C)/4
Y = int(D)/4
Z = W + X + Y + B + int(C) - 2*int(D)
R = Z%7

if R < 0:
    R = R + 7
    
else :
    R=R

if R == 0:
    day = 'Sunday'
elif R == 1:
    day = 'Monday'
elif R == 2:
    day = 'Tuesday'
elif R == 3:
    day = 'Wednesday'
elif R == 4:
    day = 'Thursday'
elif R == 5:
    day = 'Friday'
elif R == 6:
    day = 'Saturday'
    

print fname,lname,'was born on a',day  
  
