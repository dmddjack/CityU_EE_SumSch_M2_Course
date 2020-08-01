dict0 = {}
while True:
    student_name = input('input student\'s name:')
    school_name = input('input school name:')
    while True:
        SS_ID = input('input %s\'s SS ID:' % student_name)
        try:
            int(SS_ID[2:])
        except ValueError:
            print('invalid input')
            continue
        if len(SS_ID) != 5 or SS_ID[:2] is not  'SS':
            print('invalid input')
            continue
        else:
            break
    while True:
        Attendance = input('does %s absent today?(y/n)')
        if Attendance == 'y':
            Attendance = False
            break
        elif Attendance == 'x':
            Attendance = True
            break
        else:
            print('invalid input')
    dict0.get(student_name, {'school_name': school_name, 'SS_ID': tuple(SS_ID), 'Attendance': tuple(Attendance)})
    print(dict0)