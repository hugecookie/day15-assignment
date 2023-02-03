# 시간복잡도란 어떤 일을 처리하는데 걸리는 최악의 시간을 계산한 것이다.
# 반복해서 더하는 n = n + 1의 경우 O(n)시간이 걸린다고 할 수 있다.
#
#
#


pokemons = []  # 빈 배열


def add_data(pokemon):
    pokemons.append(None)
    # pokemons[len(pokemons) - 1] = pokemon
    pokemons[-1] = pokemon

add_data('피카츄')
add_data('라이츄')
add_data('꼬부기')
add_data('어니부기')
add_data('거북왕')

print(pokemons)

