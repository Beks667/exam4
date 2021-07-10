def summa(numbers):
    result = 0
    while numbers> 0:
        result += numbers % 10
        numbers //= 10
    return result
 
print(summa(1234567895))
































# print(sum(map(int, list(input('insert numbers and  i  sum it:')))))