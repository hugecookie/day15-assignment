
def insert_data(position, pokemon):
    if position < 0 or position > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon  # 지정한 위치에 친구 추가

if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "어니부기", "거북왕"]
    print(pokemons)
    insert_data(2, '가디')
    print(pokemons)
    insert_data(6, '피존투')
    print(pokemons)

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
