nb1 = None
while nb1 is None:
    nb1_str = input("Entrez le 1er nombre: ")
    if nb1_str.isdigit():
        nb1 = int(nb1_str)

nb2 = None
while nb2 is None:
    nb2_str = input("Entrez le 2e nombre: ")
    if nb2_str.isdigit():
        nb2 = int(nb2_str)

print()
print(f"=> {nb1} + {nb2}: {nb1 + nb2}")
