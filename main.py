# str = 'this is really string'

def rep():
    try:
        t = input('text -> ')
        w = input('word to change -> ')
        c = input('change to -> ')

        print(t.replace(f'{w}',f'{c}'))
    except Exception as ex:
        print(f'Error: {ex}')


rep()
