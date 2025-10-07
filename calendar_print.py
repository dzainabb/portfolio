print('hello')

print ('how many day are in this month?')
days_in_month = input()

print('what day of the week did this month start on? ' \
'Enter 1 for Sunday, 2 for Monday, 3 for Tuesday, 4 for Wednesday, 5 for Thursday, 6 for Friday, 7 for Saturday')
first_day_of_month = int(input())
print ('S   M   T   W   T   F   S')

if first_day_of_month == 1:
    print ("1   2   3   4   5   6  7 ")
    print ("8   9   10  11  12  13  14")
    print("15  16  17  18  19  20  21")
    print('22  23  24   25  26  27  28')
    print('29  30  31')