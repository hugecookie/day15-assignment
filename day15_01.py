def find_and_insert_data(pokemon, p_count):
    find_pos = -1
    for i in range(len(pokemons)):
        pair = pokemons[i]
        if p_count >= pair[1]:
            find_pos = i
            break
    if find_pos == -1:
        find_pos = len(pokemons)

    insert_data(find_pos, (pokemon, p_count))


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("Out of index")
        return
    pokemons.append(None)
    kLen = len(pokemons)

    for i in range(kLen - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon


dat = {'거북왕': 230, '라이츄': 190, '어니부기': 160, '피카츄': 120, '꼬부기': 95}
pokemons = list(dat.items())



if __name__ == "__main__":
    print(dat)
    while True:
        data = input("추가할 친구--> ")
        count = int(input("카톡 횟수--> "))
        find_and_insert_data(data, count)
        dat = dict(pokemons)
        print(dat)


# 교재 chap3 예제 문제
# 1. 선형리스트
#
# 2. 1
#
# 3. 4->2->3->1
#
# 4. katok.append(None)
#
# 5. katok.pop()
#
# 6. 4->2->1->3
#
# 7. 4
#
# 8. 1