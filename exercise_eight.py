def prepareList(attempts, attempt):
    list = []
    while(attempt <= attempts):
        print()
        number = float(input(f'Informando número {attempt} de {attempts} : '))
        list.append(number)
        attempt += 1
    return list

attempts = int(input('Deseja informar quantos números? : '))
attempt = 1
list = prepareList(attempts, attempt)
sum_numbers = sum(list)
media = sum_numbers / len(list)


print(f'Média dos números informados: {media}')