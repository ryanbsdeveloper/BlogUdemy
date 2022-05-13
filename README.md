```python
initial = 24362700
end = 24362799

for n in range(initial, end+1):
  n, end, initial = str(n), str(end), str(initial)

  if n[-2:] == n[-2] + '9':
    n = n[:-1]
    print(n)

  if n == end and end[-1] not in '9':
    _continue = [x for x in end]

    if initial < end:
      _continue[-1] = initial[-1]
      _continue = ''.join(_continue)

    else:
      _continue = '0'

    for c in range(int(_continue), int(end)+1):
      print(c)
```

