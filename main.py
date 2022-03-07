while True:
    va = input('to converter celsius to fahrenheit type it 1 and fahrenheit to celsius type it 2: ')
    if va == '1':
        
        var = int(input('write the degrees in celsius: '))
        var2 = 9/5 * var + 32
        print(f'{var} converted to fahrenheit is {var2}')
    elif va == '2':
        varr = int(input('write the degrees in fahrenheit: '))
        varr2 = varr - 32 
        varr3 = varr2 /1.8
        print(f'{varr} converted in celsius is {varr3}')
    

    v1 = input('Do you want to convert again? (y/n) ')
    if v1 == 'y':
        continue
    else:
        break
