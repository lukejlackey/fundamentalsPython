
def main():
    Basic()
    multiplesOfFive()
    countingDojoWay()
    whoaTSH()
    countdownByFours()
    flexibleCntr()

def Basic():
    for i in range(151):
        print(i)
    return

def multiplesOfFive():
    for i in range(5, 1001, 5):
        print(i)
    return

def countingDojoWay():
    for i in range(1,101):
        if (i % 5) == 0:
            print('Coding Dojo')
        else:
            print(i)
    return

def whoaTSH():
    print(sum(i for i in range(500000) if (i % 2) != 0))
    return

def countdownByFours():
    for i in range(2018, 0, -4):
        print(i)
    return

def flexibleCntr():
    lowNum = 2
    highNum = 9
    mult = 3
    for i in [num for num in range(lowNum, highNum + 1) if (num % mult) == 0]:
        print(i)
    return

main()