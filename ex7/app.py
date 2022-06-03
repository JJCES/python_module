import math  # math 라이브러리를 불러옵니다.
'''
여기서 질문으로 예상되는 것은
왜?
왜 math라는 파일이 없는데 실행되는거죠?
라고 하실 수 있습니다.

math는 파이썬에서 기본으로 내장되어있는 라이브러리다 보니
따로 파일이 존재하지 않아도 파이썬 안에 있는 math라는 함수를 불러오게 됩니다.
'''

print('pi', math.pi)  # 원주율값을 반환
print("inf=", math.inf)  # infinity의 약자로 무한을 반환합니다.
print("ceil(90.9)", math.ceil(90.9))  # 올림을 의미하며 출력은 91이 됩니다.
print("floor(90.9)", math.floor(90.9))  # 버림을 의미하며 출력값은 90이 됩니다.
print("round(90.9)", math.round(90.9))  # 반올림을 의미하며 출력값은 91이 됩니다.
print("factorial(5)", math.factorial(5))  # 5의 펙토리얼값을 출력하라는 의미로 120이 나옵니다.
print("gcd(12,4)", math.gcd(12, 4))  # 12와 4의 최대공약수를 나타내라는 뜻으로 4가 나옵니다.
print("sqrt(144)", math.sqrt(144)) # 144의 제곱근을 나타내라는 뜻으로 12.0이 나옵니다.
# 주의할 사항은 sqrt는 float형식을 출력한다는 점입니다.
