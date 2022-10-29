def print_count():
    try:
        t = input('text -> ')
        s = input('symbol -> ')

        print(f'Number of particular symbol in text: {t.count(s)}')
    except Exception as ex:
        print(f'Error: {ex}')

print_count()