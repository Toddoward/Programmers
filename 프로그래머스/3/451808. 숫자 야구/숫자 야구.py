def solution(n, submit):
    # 1. 3024개 전체 경우 생성 (1~9 사이의 서로 다른 4자리 수)
    candidate_list = []
    
    ### 중첩 루프를 이용한 전체 경우 생성
    for a in range(1, 10):
        for b in range(1, 10):
            if a == b: continue
            for c in range(1, 10):
                if a == c or b == c: continue
                for d in range(1, 10):
                    if a == d or b == d or c == d: continue
                    candidate_list.append(str(a * 1000 + b * 100 + c * 10 + d))

    # 2. 필터링 루프 시작
    cnt = 0
    while len(candidate_list) > 1:
        # 리스트의 첫 번째 요소를 시도해봅니다.
        num_str = candidate_list[0]
        cnt += 1
        result = submit(int(num_str))
        
        # 만약 정답을 맞혔다면 즉시 반환
        if result == "4S 0B":
            return int(num_str)
        
        # 결과 파싱 "xS yB" -> x, y
        strike = int(result[0])
        ball = int(result[3])
        
        ### 리스트 컴프리헨션으로 filterList 구현
        new_list = []
        num_set = set(num_str) # 중복 확인용 셋
        
        for ele_str in candidate_list:
            s_cnt = 0
            b_cnt = 0
            
            for i in range(4):
                if num_str[i] == ele_str[i]:
                    s_cnt += 1
                elif ele_str[i] in num_set:
                    b_cnt += 1
            
            # 현재 답변(strike, ball)과 모순되지 않는 숫자만 유지
            if s_cnt == strike and b_cnt == ball:
                new_list.append(ele_str)
        
        candidate_list = new_list

    # 리스트에 하나만 남았다면 그것이 정답
    return int(candidate_list[0]) if candidate_list else 0