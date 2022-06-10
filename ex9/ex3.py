from datetime import time
# datetime에 있는 time 모듈 호출

t = time() 
# 기본값 호출
# 00:00:00 으로 지정
t1 = time(hour=10, minute=20, second=30)
# 시간을 10시 20분 30초로 지정
# 출력값 : 10:20:30
t2 = time(hour=10, minute=20, second=50)
# 시간을 10시 25분 50초로 지정
# 출력값 : 10:25:50
print(t2.second - t1.second)
# t2의 초와 t1의 초를 비교할 때 사용
# 출력 : 20