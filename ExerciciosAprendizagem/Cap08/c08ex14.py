agrupMutavel = {"A", "B", 1, 2, 3}
for i, j in enumerate(agrupMutavel):
    print(i, " - ", j)

agrupImutavel = frozenset({1, 2, 3, "A", "B"})
for i, j in enumerate(agrupImutavel):
    print(i, " - ", j)

enter = input("\nPressione <Enter> para encerrar... ")
