users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
    { "id": 10, "name": "Jen" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

amigos = {user['id']: [] for user in users}
for i,j in friendships:
    amigos[i].append(j) if j not in amigos[i] else None
    amigos[j].append(i) if i not in amigos[j] else None

# Qual o número médio de conexões?
ignore = set()
counter = 0
for k in amigos.keys():
    if k not in ignore:
        counter += len(amigos[k])
        ignore.add(k)
media = counter / len(amigos)
