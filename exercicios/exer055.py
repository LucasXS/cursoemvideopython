bigger = 0
smaller = 0
for p in range(1, 6):
    weight = float(input(f'{p}º - Your weight: '))
    if p == 1: #li o peso da 1º pessoas
        bigger = weight #o maior peso, vai passar a ser o peso
        smaller = weight #o menor peso, vai passar a ser o peso
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print(f'The Highest weight read was {bigger}')
print(f'The Smaller weight read was {smaller}:')