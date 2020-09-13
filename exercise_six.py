number_max_sequences = int(input('Quantas sequências Fibonacci deseja visualizar?: \n'))

previous = 0
next = 0

while(next < number_max_sequences):
    print(next)
    next = next + previous
    previous = next - previous
    if next == 0:
        next = next + 1