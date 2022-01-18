import math


# #Begin35
# v = int(input())
# u = int(input())
# t = int(input())
# t2 = int(input())
# s=((v-u)*t2)+(v*t)
# print(s)

# #Begin36
# v1 = int(input())
# v2 = int(input())
# s = int(input())
# t = int(input())
# res = s + (v1*t) + (v2*t)
# print (res)

# #Integer27
# days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# k = int(input())
# jan_first = 6
# if 0<k<365:
#     k = (k+6) % 7
#     print (k)
#     print (days[k-2])
# else:
#     print('again')

# #Integer30
# year = int(input())
# century = (year+100) // 100
# print(century)

# #Boolean23
# num = int(input())
# s = str(num)
# try:
#     if len(s) != 4:
#         raise Exception('Не четырехзначное')
#     if s[0] == s[3] and s[1] == s[2]:
#         print ('Полиндром')
#     else:
#         print ('Нот полиндром')
# except Exception as e:
#     print (e)

# #Boolean25
# x = int(input('X = '))
# y = int(input('Y = '))
# dot = [x,y]
# booll = True
# if x < 0 and y > 0:
#     print (boll)
# else:
#     boll = False
#     print (booll)

# #If20
# A = int(input())
# B = int(input())
# C = int(input())
# AB = (A - B)
# AC = (A - C)
# if AB < 0:
#     AB *= -1
# if AC < 0:
#     AC *= -1
# if AB < AC:
#     print('AB is closer = ' + str(AB))
# elif AC < AB:
#     print('AC is closer = ' + str(AC))
# else:
#     print('AB and AC is equal = ' + str(AB))

# #If25
# x = int(input())
# if x > 0:
#     f = 2 * math.sin(x)
# else:
#     f = 6 - x
# print(f)

