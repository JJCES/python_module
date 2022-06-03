import module #모듈 파일을 불러와 app.py에 종속

avg = 90.2 # 학생의 평균점수를 90.2점으로 선언
grade = module.getGrade(avg) # module.py에 있는 getGrade에 avg값을 인수로 넘겨준 뒤 이 함수를 실행하여 얻은 결과값을 grade에 저장
print(grade) # 위 grade에 저장된 값을 출력