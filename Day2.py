print("Welcome to the Tip Calculator. ")
Tbill = float(input("What was the total Bill? "))
People = int(input("How many people do you want to split the bill in Between? "))
tip = int(input("What percentage would you like to tip?  10,12 or 15  "))
tip = tip/100
pay = (Tbill + (Tbill*tip))/People
print("Each person should pay: ",round(pay,2))

#age = input("What is your current age?")
# leftage = 90 - int(age)
# weeksperyear = 52
# leftagemonths = leftage*12
# leftageweeks = leftage*52
# leftdays = leftage*365
# print(f"your life in weeks is {leftdays} days left , {leftageweeks} weeks left , {leftagemonths} months left ")