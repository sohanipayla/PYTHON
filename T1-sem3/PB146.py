year=int(input('enter year:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,'year is Leap Year')
        else:
            print(year,'year is not Leap Year')
    else:
        print(year,'year is Leap Year')
else:
    print(year,'year is not Leap Year')