points_vicory = 3
points_draw = 1
points_defeat = 0

victorys = int(input('Qual o número de vitórias que seu time teve durante o campeonato? : '))
draws = int(input('Qual o número de empates que seu time teve durante o campeonato? : '))
defeats = int(input('Qual o número de derrotas que seu time teve durante o campeonato? '))

winning_score = victorys * points_vicory
tie_score = draws * points_draw
sum_score = winning_score + tie_score + (defeats*points_defeat)
print(f'Seu time finalizou o campeonate com {sum_score} pontos !!')