'''
student = ['a', 'b', 'c', 'd']
school = ['a School', 'b School', 'b School', 'b School']
SS_ID = ['SS001', 'SS002', 'SS003', 'SS004' ]
Attendance = [(True, True, True, False), (False, False, True, True), (True, True, True, False),
              (True, False, True, True)]
for testing use
'''
student = []
school = []
SS_ID = []
Attendance = []
population = 4
for i in range(population):
    student.append(input('input student\'s name:'))
    school.append(input('input school name:'))
    while True:
        ID = input('input %s\'s SS ID:' % student[i])
        try:
            int(ID[2:])
        except ValueError:
            print('invalid input')
            continue
        if len(ID) != 5 or ID[:2] != 'SS':
            print('invalid input')
            continue
        else:
            SS_ID.append(ID)
            break
    for j in range(1, 5):
        att = []
        while True:
            result = input('does %s absent at day %d?(y/n)' % (student[i], j))
            if result == 'y':
                att.append(False)
                break
            elif result == 'n':
                att.append(True)
                break
            else:
                print('invalid input')
    Attendance.append(tuple(att))
print('{0:<20} {1:<30} {2:<20} {3:<20}'.format('student name', 'school name', 'SS_ID', 'Attendance'))
for i in range(population):
    print('{0:<20} {1:<30} {2:<20} {3:<20}'.format(student[i], school[i], SS_ID[i], str(Attendance[i])))
while True:
    choice = input('type something to search:')
    count = 0
    count_att = 0
    print('{0:<20} {1:<30} {2:<20} {3:<20}'.format('student name', 'school name', 'SS_ID', 'Attendance'))
    if 'School' in choice or 'College' in choice:
        for i in range(population):
            if choice == school[i]:
                print('{0:<20} {1:<30} {2:<20} {3:<20}'.format(student[i], school[i], SS_ID[i], str(Attendance[i])))
                count_att += sum(Attendance[i])
                count += 4
        print('Attendance rate of %s = %s' % (choice, str(count_att / count * 100) + '%'))
    elif 'SS' in choice:
        for i in range(population):
            if choice == SS_ID[i]:
                print('{0:<20} {1:<30} {2:<20} {3:<20}'.format(student[i], school[i], SS_ID[i], str(Attendance[i])))
                print('Attendance rate of %s = %s' % (choice, str(sum(Attendance[i]) / 4 * 100) + '%'))
                break
    else:
        for i in range(population):
            if choice == student[i]:
                print('{0:<20} {1:<30} {2:<20} {3:<20}'.format(student[i], school[i], SS_ID[i], str(Attendance[i])))
                print('Attendance rate of %s = %s' % (choice, str(sum(Attendance[i]) / 4 * 100) + '%'))
                break
