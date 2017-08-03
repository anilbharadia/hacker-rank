squares = [i*i for i in range(1, 11)]
print squares

double_of_squares = [j + j for j in [ i * i for i in range(1,11) ]]
print double_of_squares

multiples_of_three = [i for i in range(1, 11) if i % 3 == 0]
print multiples_of_three

num_square_qube = [[n, n**2, n**3] for n in range(1, 5)]
print num_square_qube

possibilities = [[a, n] for a in ['a', 'b', 'c'] for n in range(1,4)]
print possibilities