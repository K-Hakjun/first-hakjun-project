resident_number=input("주민번호를 입력해주세요(12자리, -포함): ")
birth_year=resident_number[0:2]
birth_month=resident_number[2:4]
birth_day=resident_number[4:6]
sex=resident_number[7]
birth_year=int(birth_year)
try:
    if 0<=birth_year<22:
        a=str(input('2000년 이후 출생자 입니까? 맞으면o, 아니면x: '))
        if a=='o':
            if sex == '3':
                sex="남자"
            if sex=='4':
                sex="여자"
            else:
                print('올바른 번호를 입력해주세요')
        if a=='x':
            print('올바른 번호를 입력해주세요')
    else:
        if sex == '1':
            sex='남자'
        if sex=='2':
            sex='여자'
except:
    print("올바른 주민등록번호를 입력해주세요.")
birth_year=str(birth_year)
birth_year=resident_number[0:2]
print("생년월일:{0}년 {1}월 {2}일".format(birth_year, birth_month, birth_day))
print("성별:{0}".format(sex))

