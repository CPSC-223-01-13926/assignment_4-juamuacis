##Author:       Juan Cisneros
##Assignment:   Lab 4

from weather import *
import calendar
file = "w.dat"

flag = True

while(flag):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data Filename")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Data")
    print("9. Exit the Program")

    mychoice = int(input("Enter Menu choice: "))
    print()

    if mychoice == 1:
        myfile = input("Enter data filename: ")
        weather = read_data(myfile)
    elif mychoice == 2:
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter Humidity: "))
        r = float(input("Enter rainfall: "))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        write_data(weather, filename = myfile)
    elif mychoice == 3:
        d = input("Enter Date: ")
        display = report_daily(weather, d)        
        print(display)
    elif mychoice == 4:
        display = report_historical(data = weather)
        print(display)
    elif mychoice == 9:
        flag = False
        break

print("Goodbye!")