a = int(input())
if a == 0:
    print("зеленый")
elif 0<a and a <=36:
    if (a%2==0) and ((1<=a and a<= 10) or (19<=a and a<= 28)):
        print("черный")
    elif (a%2!=0) and ((11<=a and a<= 18)or(29<=a and a<= 36)):
        print("черный")
    else:
        print("красный")
else:
    print("ошибка ввода")
