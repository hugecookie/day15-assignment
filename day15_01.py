pokemons = ["피카츄", "라이츄", "꼬부기", "어니부기", "거북왕"]


def insert_data(position, pokemon):
    if position < 0 or position > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    """
    선형 리스트의 idx위치에 원소 제거
    :param idx: Index number
    :return:
    """
    if idx < 0 or idx >= len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, kLen):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[kLen - 1])


def add_data(pokemon):
    '''
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon: 삽입할 포켓몬 이름
    :return:
    '''
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


pokmons = []
select = -1

if __name__ == "__main__":
    while True:
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
        if select == 1:
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif select == 2:
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif select == 3:
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif select == 4:
            print(pokemons)
            # exit()
            break
        else:
            print("menu에서 고르세요")
            continue


    # print(pokemons)
    # insert_data(2, '가디')
    # delete_data(1)
    # print(pokemons)
    # insert_data(6, '피존투')
    # delete_data(3)
    # print(pokemons)
    # a = int(input('입력한 이후 삭제할 인덱스 값을 입력하세요.'))
    # for i in range(len(pokemons)-1, a, -1):
    #     delete_data(i)
    #     print(pokemons)
    # add_data('터컴니')
    # print(pokemons)


# pokemons = list()  # 빈 배열
# def add_data(pokemon):
#     pokemons.append(None)
#     # pokemons[len(pokemons) - 1] = pokemon
#     pokemons[-1] = pokemon
#
# add_data('피카츄')
# add_data('라이츄')
# add_data('꼬부기')
# add_data('어니부기')
# add_data('거북왕')
#
# print(pokemons)


