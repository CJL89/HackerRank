import re

n = 'Sorting1234'
results = []

lower = re.findall('[a-z]+', n)
results.append([''.join(sorted(x)) for x in lower])
upper = re.findall('[A-Z]+', n)
results.append([''.join(sorted(x)) for x in upper])
odd_numbers = re.findall('[13579]+', n)
results.append([''.join(sorted(x)) for x in odd_numbers])
even_numbers = re.findall('[24680]+', n)
results.append([''.join(sorted(x)) for x in even_numbers])

results = [''.join(x) for x in results]
print(*results, sep='')


# One liner:
sorted(re.findall('[a-z]', s)) + sorted(re.findall('[A-Z]', s)) + sorted(re.findall('[13579]', s)) + sorted(re.findall('[24680]', s))
print(''.join(results))
