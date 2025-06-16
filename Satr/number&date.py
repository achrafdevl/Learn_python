 #! ****************************
 #! from negative to positive

# number = -999
# print(abs(number))

#! ****************************
#! In this lesson, we will learn how to round a number using the round function in Python

# number = 3.537
# print(round(number))

#! ****************************
#! n°²

# number = 3 
# print(pow(number, 2))

#! ****************************
#! min & max

# numbers = 300,600,786,1000,276
# print(min(numbers))
# print(max(numbers))

#! ****************************
#! sum function

# numbers = 300,600,786,1000,276
# print(sum(numbers))

#! ****************************
#! we will learn how to find the square root of a number using the sqrt function

# import math
# number = 144
# print(math.sqrt(number))

#! ****************************
#! remainder

import math
print(math.remainder(26, 5))

#! ****************************
#! randim number
# import random
# print(random.randint(1,100))

#! ****************************
#! create Date

# import datetime
# date= datetime.date(2020, 2, 13)
# print(date)
# print(date.year)

#! ****************************
#! create Time

# import datetime
# time= datetime.time(14,33, 15)
# print(time)
# print(time.second)

#! ****************************
#! know the date & time of today

# import datetime
# now = datetime.datetime.today()
# print(now)
# print(now.hour)
# print(now.day)

#! ****************************
#! who to change  date  & time to text

# import datetime
# date = datetime.date(2020, 2 ,13)
# time = datetime.time(14,5,17)

# print(date)
# print(time)

# print(date.strftime('%A %B %Y'))
# print(time.strftime("%I %M %S"))
