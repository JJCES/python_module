from Module.calc import *
'''
Module 폴더에 있는 calc.py 모듈에 있는 모든 함수를 app.py에 종속
calc.py에는 
add와 remove함수가 있는데
이를 사용할때는 그냥 함수명만을 이용하여 함수를 호출합니다.
ex) add(1, 2) # result : 3
'''


result = 0 # result변수를 0으로 선언

result = add(result, 100) # result는 add함수의 매개변수인 x와 y에 대해 인수 result(0)와 100을 순차적으로 대입하여 연산한 결과값을 다시 정의합니다.
print(result) # 100 출력
result = remove(result, 10) # 여기서 다시 result를 remove함수의 매개변수 x와 y에 대해 인수 result(100)와 10을 순차 대입하여 연산한 결과값을 다시 정의합니다.
print(result) # 90 출력