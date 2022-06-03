# 이 함수는 따로 설명하지 않겠습니다.

def getGrade(score): 
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"