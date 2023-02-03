## 전역 변수 선언 부분 ##
px = [7, -4, 0, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 함수 선언 부분 ##
def printPoly(px):
    """
    다항식을 포멧에 맞게 출력하는 함수
    :param px: 각 원소의 계수 모음
    :return:
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_Str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if coef > 0:
            if i == 0:
                poly_Str = poly_Str + " "
                poly_Str = poly_Str + f'{str(coef)}x^{str(term)} '
                term = term - 1
                continue
            poly_Str = poly_Str + "+"
        elif coef == 0:
            term = term - 1
            continue

        poly_Str = poly_Str + f'{str(coef)}x^{str(term)} '
        term = term - 1






    return poly_Str


def calcPoly(x_val, px):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param x_val:  x값 integer
    :param px:  계수를 원소로 가지고 있는 list
    :return: 계산 결과 값 integer
    """
    return_val = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        return_val = return_val+ coef * x_val ** term
        term = term - 1

    return return_val


## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값:"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)


