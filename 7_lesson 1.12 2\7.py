
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞)(−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии (полуинтервал, промежуток).

Sample Input 1:

20

Sample Output 1:

True

Sample Input 2:

-20

Sample Output 2:

False

X = int(input())
if X<=12 and X>-15:
    print('True')
elif X>14 and X<17:
    print('True')
elif X>=19:
    print('True')
else:
    print('False')
