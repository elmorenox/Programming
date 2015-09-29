currentYear = 2015
currentPop = 321386917

birthPerSec = 7
deathPerSec = (1/13.00)
secInYear = 31556952

inputYear = int(raw_input("Enter a future year: "))

numberOfYears = (inputYear - currentYear)
numOfSecs = numberOfYears * secInYear

futurePop = (birthPerSec * numOfSecs) - (deathPerSec * numOfSecs)

print int(futurePop)



