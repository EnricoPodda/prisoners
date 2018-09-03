from random import randint

nPrisoners = int(input('How many prisoners do you have? '))
print('There are ' + str(nPrisoners) + ' prisoners. How many day will it take to rejoin freedom?')

dictPrisoners = {}

for n in range(nPrisoners):
    dictPrisoners[n] = False

light = False
counter = 0                                         # The n prisoner count
day = 0

while True:
    day += 1

    prisoner = randint(0, nPrisoners - 1)           # 0 <= prisoner <= nPrisoners - 1.

    if not(dictPrisoners.get(prisoner)) and not(light) and not(prisoner == nPrisoners-1):
        dictPrisoners[prisoner] = True
        light = True

    if prisoner == nPrisoners-1 and light:
        light = False
        counter += 1
        if counter == (nPrisoners-1):
            break


print('They did it! They are free now, after only ' + str(day) + ' days!')