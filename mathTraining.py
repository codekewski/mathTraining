import time
timestamp = time.ctime()
def storCmd():
    if isinstance(result, (int,float,complex)):
        storCmd = str(input('Do you want to save this result y/n? ')) #Saves stuff to files
        if storCmd == 'y':
            with open('results.txt','a') as saveData:
                saveData.write(f"\n on {timestamp} you calculated: {numberOne} {opSymbol} {NummerZwei} with a result of {result}")
                print('Result successfully saved!')
        else:
            print("your result is forever lost in the aether")

numberOne = int(input('Give meh numbah one: '))
opSymbol = input('Give operator: ')
NummerZwei = int(input('Second numbah two: '))


if  opSymbol == '+':
    result = (numberOne+NummerZwei)
    print(result)
elif opSymbol == '-':
    result = (numberOne-NummerZwei)
    print(result)
elif opSymbol == '*':
    result = (numberOne*NummerZwei)
    print(result)
elif opSymbol == '/':
    result = (numberOne/NummerZwei)
    print(result)
else:
    result = ('That\'s not one of them operatorz')
    print(result)

storCmd()
print('change')
