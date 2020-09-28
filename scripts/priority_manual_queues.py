q = []

q.append((2, 'code'))
q.append((1, 'eat'))
q.append((3, 'sleep'))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)