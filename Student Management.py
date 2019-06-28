StudentsData=[]
def GetStudentValue(value):
    index = 0
    for name in StudentsData:
        if name['Name'].lower() == value.lower():
            return index
        index += 1

while True:
    print('\n 1. Add new Student\'s data')
    print(' 2. Delete Student\'s data')
    print(' 3. Search Student\'s data')
    print(' 4. Edit Student\'s data')
    print(' 5. Show All Students data')
    print(' 6. Exit')

    value = input("\n Press 1-6 ")

    if value=='1':
        Student={}
        Student['Name']=input("Enter Student's Name ")
        Student['F_Name'] = input("Enter Father Name ")
        Student['Age'] = input("Enter Student's Age ")
        Student['ContactNo'] = input("Enter Student's Contact Number ")
        StudentsData.append(Student)

    elif value == '2':
        SName = input('Enter Student\'s Name ')
        DeleteValue =GetStudentValue(SName)
        del StudentsData[DeleteValue]
        input('Press any Key to Continue...')

    elif value == '3':
        SName = input('Enter Student\'s Name ')
        SearchValue =GetStudentValue(SName)
        print('\n'+"\n".join("{}: {}".format(k, v) for k, v in StudentsData[SearchValue].items())+'\n')
        input('Press any Key to Continue...')

    elif value == '4':
        SName = input('Enter Student\'s Name ')
        ValueForUpdate = GetStudentValue(SName)
        print('\n' + "\n".join("{}: {}".format(k, v) for k, v in StudentsData[ValueForUpdate].items()) + '\n')
        while True:
            Key = input('Enter Key ')
            value = input('Enter Value ')
            for keySearch in StudentsData[ValueForUpdate].keys():
                if keySearch == Key:
                    StudentsData[ValueForUpdate][keySearch] = value
            print('\n' + "\n".join("{}: {}".format(k, v) for k, v in StudentsData[ValueForUpdate].items()) + '\n')
            check=input('Do you want to Update more? Y/N ')
            if check=='N' or 'n':
                break
    elif value == '5':
        print(StudentsData)
        input('Press any Key to Continue...')
    elif value == '6':
        break