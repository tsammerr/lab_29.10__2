s = int(input('stroke -> '))
a = int(input('letter -> '))
from collections import Counter
my_str = "Mary had a little lamb"
counter = Counter(my_str)
print(counter['a'])