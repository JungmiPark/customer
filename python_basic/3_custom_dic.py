li = []
info = dict()
a=''
print('='*55)
print('='*19, '고객 관리 시스템', '='*18)
print('='*18, '메뉴를 선택하세요.', '='*17)
print('='*55)
while True:
    print('='*5, '정보 입력 : I, 정보 개수 출력 : C, 종료 : Q', '='*5)
    menu=input('메뉴를 입력하세요:')
    if menu == 'I':
        info = dict()
        info['name']=input('이름을 입력해주세요.:')
        while True:
            a=input('여성이면 F, 남성이면 M을 입력해주세요.:')
            if a =='F' or a =='M':
                info['sex']=a  
                break    
            else:
                print('다시 입력해주세요.')
                continue
        info['email']=input('메일을 입력해주세요.:')
        info['year']=int(input('생년을 입력해주세요.:'))
        li.append(info)
    elif menu == 'C':
        print('등록된 고객 정보의 개수: ', len(li))
        # print(li)
    elif menu == 'Q':
        break
    else:
        print('다시 입력해주세요.')
        continue
        