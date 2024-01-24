grade = int(input('Enter student marks: '))

if grade < 0:
    print('Invalid!')
elif grade < 40:
    print('fail')
elif grade < 50:
    print('grade: D')
elif grade < 60:
    print('grade: C')
elif grade < 70:
    print('grade: B')
elif grade < 100:
    print('grade: A')
else:
    print('marks beyond range.')
