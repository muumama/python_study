def king(korea, chosun):
    king_dict = dict() # 왕 이름을 담을 dict
    
    korea = korea.split(",") # 문자열을 ,기준으로 list 변경 
    chosun = chosun.split(",") # 문자열을 ,기준으로 list 변경
    
    # 고려의 왕 이름 저장 후 값을 1로 설정
    for kor in korea:
        king_dict[kor] = 1
    
    # 조선의 왕 탐색
    for cho in chosun:
        if king_dict.get(cho, 0) >= 1: # 왕 이름이 존재 여부 있으면 1이상의 값이 나옴
            king_dict[cho] = king_dict[cho] + 1 # 존재하면 +1
        else:
            continue # 없으면 건너 뜀
#    리스트 컴프리헨션을 사용하면 아래 코드
#    repeated_king = [ k for (k, v) in king_dict.items() if v >= 2 ]
    
    repeated_king = [] # 중복된 왕 이름을 담는 리스트
    for (k,v) in king_dict.items():
        if v >= 2: # 왕 이름이 2이상이면 중복된 것
            repeated_king.append(k)
    
    count = 0 # 카운트 변수
    for king in repeated_king:
        print(f"조선과 고려에 모두 있는 왕 이름 : {king}")
        count = count + 1 # 존재하면 +1
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")