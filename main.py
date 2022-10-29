def con():
    try:
        text = input('enter text -> ')
        counter = 0
        counter_2 = 0
        for i in text:
            if i.isalpha():
                counter += 1
            if i.isnumeric():
                counter_2 += 1
        print(f'Number of letters: {counter}\nNumber of digits: {counter_2}')
    except Exception as ex:
        print(f'Error:{ex}')


con()
