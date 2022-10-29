def print_count():
    try:
        t = input('text -> ')
        w = input('word -> ')

        print(f'Number of particular symbol in text: {t.count(w)}')
    except Exception as ex:
        print(f'Error: {ex}')

print_count()