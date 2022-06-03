import random  # random 라이브러리를 불러옵니다.

print("randint", random.randint(1, 100))  # 1~100 사이의 랜덤한 정수를 출력합니다.
'''
위 내용 외에 사용법이 많아 다룹니다.
random.randrange(10) # 0부터 10까지의 랜덤한 정수를 출력합니다.
random.range(1, 100, 3) # 1~100 사이의 정수중 랜덤한 3의 배수를 출력합니다.

randint와 randrange의 차이점은 시작 지점을 정할 수 있느냐 없느냐 로 보시면 됩니다!
'''

print("choice", random.choice(["짜장면", "짬뽕", "탕수육", "먹고싶다"]))
'''
위 choice는 리스트 값 내에 있는 값들중 랜덤한 한 값을 뽑은 예제로
짜장면, 짬뽕, 탕수육, 먹고싶다 중 딱 하나만 반환합니다.

만약 여러개를 반환하시려면

random.choices(["짜장면", "짬뽕", "탕수육", "먹고싶다"],k=2)
와 같이 작성시 2개의 값을 반환합니다.
'''

print("shuffle", random.shuffle([1,2,3,4,5,6])) # 말 그대로 셔플입니다. 리스트 배열을 섞습니다.
print("sample", random.sample([1,2,3,4,5]), k=2) # 이는 위의 choices와 같이 생각하면 되오나
# choices와는 다르게 뽑은 값은 변수에서 삭제됩니다.

print("random()", random.random()) # 0.00~1.00사이의 실수를 반환합니다.
print("uniform", random.uniform(1, 100)) # 1과 100사이의 실수를 반환합니다.

random.seed() # 이는 반환값이 없으나 랜덤 모듈에 대한 실행 값이 일정하지 않도록 변경해주는 역할을 합니다.