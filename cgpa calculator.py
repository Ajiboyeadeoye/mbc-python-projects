# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 03:10:53 2023

@author: PC
"""

print('Hi computer science Uite!, I am a cgpa calculator, I can calculate your first year cgpa, just follow my instructions! ')
name = input('Enter your name ')
matricNo = int(input('Enter your matric no ')) #UI matric number does not contain letter
listOfCourses = {'CSC 101 ':3, 'MAT 111 ':4, 'MAT121 ':4, 'MAT 141 ':4, 'STA 112 ':4, 'STA 121 ':4, 'PHY 112 ':3, 'PHY 113 ':3, 'PHY 114 ':3, 'PHY 115 ':3, 'PHY 118 ':3, 'GES 101 ':2, 'GES 102 ':2
                 }

courseUnits = listOfCourses.values() # This gets the unit for each of the courses
totalUnit = 0
totalUnitObtained = 0
result = 0
scoreList = []
unitObtainedList = []
for unit in courseUnits:
    totalUnit = totalUnit + unit
    unit += 1
    
print('you registered courses of total unit :', totalUnit ) #The sudent resgistered all courses
def enter_scores(): 
    course = listOfCourses.keys()
    for course in course:
        scoreObtain = int(input('Enter score for ' + course ))
        if scoreObtain >= 70 and scoreObtain <= 100:
              unitObtainedList.append(4)
        elif scoreObtain >= 60 and scoreObtain <= 69:
              unitObtainedList.append(3)
        elif (scoreObtain >= 50 and scoreObtain <= 59):
              unitObtainedList.append(2)
        elif scoreObtain >= 45 and scoreObtain <= 49:
              unitObtainedList.append(1)
        else: 
            unitObtainedList.append(0)
            
enter_scores()
print('please, verify all the entries accordingly ' +  str(scoreList))
print('please, start again for wrong input or continue for correct input')
print(unitObtainedList)
for unit in unitObtainedList:
    totalUnitObtained = totalUnitObtained + unit
    unit += 1

result = totalUnit/totalUnitObtained
print(result)

if result >= 3.4 and result <= 4:
    print('first class')
elif result >= 3.0 and result <= 3.49:
    print('second class upper')
elif result >= 2.0 and result <= 2.99:
    print('second class lower')
else:
    print('third class')
    
    