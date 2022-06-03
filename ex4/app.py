'''
from 모듈이름 import 모듈_내_함수
from ~ import ~문은 모듈에서 필요없는 함수가 너무 많거나
함수를 사용할 때 필요 이상으로 코드가 길어지는 점을 막고자 사용합니다.
위 문법을 사용할때는 아래와 같은 규칙을 적용합니다.

from [파일 이름] import [불러 올 파일 안에서 내가 사용하고자 하는 함수의 이름들]
위 문법을 random이라는 모듈을 예시로 하자면
아래와 같습니다.

from random import randint, choice

자 이제 한번 3번 예제코드를 배워본 내용으로 변형해봅시다.
'''
from module import getGrade

avg = 90.2 # 학생의 평균점수를 90.2점으로 선언
grade = getGrade(avg) # module.py에 있는 getGrade에 avg값을 인수로 넘겨준 뒤 이 함수를 실행하여 얻은 결과값을 grade에 저장
print(grade) # 위 grade에 저장된 값을 출력

# 별거 없죠?