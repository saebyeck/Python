def weeklyPay( rate, hour ): 
    money = 0
    if(hour > 30): 
        money = rate*30+ 1.5*rate*(hour-30)
    else: 
        money = rate*hour
    return money

rate = int(input("시급을입력하시오:"))
hour = int(input("근무시간을입력하시오:"))
print("주급은"+ str(weeklyPay(rate, hour)))
