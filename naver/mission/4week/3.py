guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def wrong_guest_book(guest_book):
    #파일 저장
    file_guest_book = open('boostcourse.txt','w')
    file_guest_book.write(guest_book)
    file_guest_book.close()
    #방명록 인원 별 정보 분리
    guest_book = guest_book.split('\n')
    #이름 전화번호 분리
    for i in range(len(guest_book)):
        guest_book[i] = guest_book[i].split(',')
    #잘못된 방명록 검사
    for i in range(len(guest_book)):
        first_condition = (guest_book[i][1][:3] != '010')
        second_condition = (guest_book[i][1][3] != '-' and guest_book[i][1][8] != '-')
        third_condition = (len(guest_book[i][1]) != 13)
        if first_condition or second_condition or third_condition:
            print('잘못 쓴 사람: '+guest_book[i][0])
            print('잘못 쓴 번호: '+guest_book[i][1])
            print()


wrong_guest_book(guest_book)
