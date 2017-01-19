import datetime

firstDate = input("Enter the start date in the format dd/mm/YYYY: ")
lastDate = input("Enter the end date")

firstDate = datetime.datetime.strptime(firstDate, "%d/%m/%Y")
lastDate = datetime.datetime.strptime(lastDate, "%d/%m/%Y")

#Friday is day 4 because computer
currentDate = firstDate + datetime.timedelta((4-firstDate.weekday()) % 7)
occurrences = 0
while currentDate <= lastDate:
    if currentDate.day == 13:
        occurrences += 1
        print(currentDate)
    currentDate += datetime.timedelta(7)
print(occurrences)



