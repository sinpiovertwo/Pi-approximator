print("="*70)
print("학교 수행평가 용도로 제작한 원주율 근사기 프로그램입니다.")
print("아르키메데스가 정96각형을 이용하여 원주율을 근사한 원리를 이용하였으며,")
print("근삿값과 함께 근사 과정을 시각화하여 제공합니다.")
print("n값을 입력하시면 정n각형으로 근사합니다.\n0을 입력하시면 프로그램을 종료합니다.")
print("="*70)
import math as m
import turtle as t

def mypi(n):
    theta = (360/n)/2
    inner = m.sin(m.radians(theta)) * n  # 내접다각형 둘레/원의지름
    outer = m.tan(m.radians(theta)) * n  # 외접다각형 둘레/원의지름
    newpi = (inner + outer) / 2  # 두 값의 평균값으로 원주율 근사
    error = newpi - m.pi  # 오차 계산

    print(inner, "< 원주율 <", outer)  # 계산한 값을 출력
    print(n, "각형으로 근사한 원주율:", newpi)
    print("오차:", error)
    print("="*70)

    t.clearscreen()
    t.shape("turtle")  # 그림으로 표현
    t.color("black")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(200)  # 원 그리기
   
    t.color("blue")  # 내접다각형 그리기5
    t.penup()
    t.goto(200, 0)  
    t.pendown()
    for i in range(n):
        x = 200 * m.cos(m.radians(i * 360/n))
        y = 200 * m.sin(m.radians(i * 360/n))  
        t.goto(x, y)  
    t.goto(200, 0)
       #t.circle(100, steps=n)도 가능하지만 좌표계산법에 비해 시간이 더 오래 걸리기 때문에 쓰지 않았습니다.
   
    t.color("red") #외접다각형 그리기
    k = 200 / m.cos(m.radians(theta))  #외접다각형의 시작점 x좌표
    t.penup()
    t.goto(k, 0)  
    t.pendown()
    for i in range(n):
        x = k * m.cos(m.radians(i * 360/n))
        y = k * m.sin(m.radians(i * 360/n))  
        t.goto(x, y)
          #외접다각형은 step같은게 따로 없는 것 같아서 좌표를 썼습니다.
          #cos,sin은 단위원 위의 x,y 좌표를 의미하므로 삼각함수를 이용하여 좌표를 작성했습니다.
          #단, 여기서는 단위원이 아닌 외접다각형의 외접원의 반지름을 생각해야하므로 k배 해주었습니다.
    t.goto(k, 0)
    t.done

while True:
    try:
        n = int(input("n="))
        if n == 0:
           print("프로그램을 종료합니다.\n원주율 근사기를 이용해주셔서 감사합니다.")
           break
        if n == 1 or n == 2:
           print("3 이상의 정수를 입력해주세요.")
           print("="*70)
           continue
    except ValueError:   
        print("3 이상의 정수를 입력하세요.")
        print("="*70)
        continue
    mypi(n) 