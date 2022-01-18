def average(a):
    return(sum(a))


a = []
while True:
    try:
        b = int(input())
        if b == 0:
            raise Exception('Programm is over')
        a.append(b)

    except Exception as e:
        print(e)
        break
print ('The sum is ' + str(average(a)))
