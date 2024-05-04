#Imani Hollie 02/14/2024
#Revised 6-Side Dice Roll Code

#IMPORT RANDOM (random is a library function)
import random
#Define a FUNCTION (a special-type of module)
def d6Roll():
    roll = random.randrange(1,6)
    return roll

#Call diceRoll() function
D1 = d6Roll()
D2 = d6Roll()

#Calculations/Output
print(f'D1 = {D1}')
print(f'D2 = {D2}')
print(f'Sum: {D1 + D2}')