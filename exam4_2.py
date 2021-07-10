def pyramid(size=8):
    for i in range(size):
        row = '*'*(2*i+1)
        print (row.center(2*size))