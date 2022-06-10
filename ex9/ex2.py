from datetime import date
# datetime에 있는 date 모듈 호출

today = date.today() 
# 오늘 날짜에 대한 데이터를 받아옵니다.
print(today) 
# year-month-day hour:minute:second.milliseconds
# 형식으로 출력됩니다.
print(today.year) # 몇년도인지 출력합니다.
print(today.month) # 몇월인지 출력합니다.
print(today.day) # 몇일인지 출력합니다.
print(today.weekday()) # 요일을 출력해줍니다.
# 요일은 int 형식으로 출력되는데
# ["월", "화", "수", "목", "금", "토", "일"]
# 의 배열 위치 규칙으로 되어있습니다.