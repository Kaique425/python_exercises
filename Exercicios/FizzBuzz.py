def fizz_buzz(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FizzBuzz'
    elif n1 % 5 == 0:
        return 'Buzz'
    elif n1 % 3 == 0:
        return 'Fizz'
    else:
        return n1

while True:
    try:
        fizzbuzz_number = int(input('Enter a number: '))
        print(fizz_buzz(fizzbuzz_number))
        break
    except:
        print('Only numbers are accepted')
