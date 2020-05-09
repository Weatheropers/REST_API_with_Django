# models.py 에서 받아온 DB 필드 이름을, JSON으로 변환하기 위해 serializer의 필드로 넣어줘야 되는데,
# 이 과정에서 필드개수가 너무 많다 보니까 파이썬 코드로 문자들을 자동으로 처리해 주려고 함.

print("DB table의 필드 코드를 복붙해서 입력하세요 :")
while True:
    data = input().strip()
    if data == '':
        break
#    print('\n' + data.split(' ')[0], end='')    # 한줄씩 하나의 필드 이름만 출력
    print("'" + data.split(' ')[0] + "', ", end='')     # 필드 이름들을 튜플 요소들로 출력