hour, minute = map(int,input().split())

# hour = hour - 1
# minute = minute + 15

# if(minute > 59) :
#     hour = hour + 1
#     minute = minute - 60

# if( hour < 0 ) :
#     hour = hour + 24
# elif hour > 23 : 
#     hour = hour - 24
# print(hour, minute)

if minute < 45 :
    if hour == 0 :
        hour = 23
    else : 
        hour -= 1
    minute += 15
    print(hour, minute)
else : 
    print(hour, minute - 45)