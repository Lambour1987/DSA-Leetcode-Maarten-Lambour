#2d Matrices of nd Matrices

twodimensial_list = [[1,2,3],[4,5,6],[7,8,9]]

print(twodimensial_list [0][0],"\n")

print(twodimensial_list[1][2],"\n")

twodimensial_tuple = ((1,2,3),(4,5,6),(7,8,9))

print(twodimensial_tuple[0][0],"\n")
print(twodimensial_tuple[1][2],"\n")

multidimensial_list = [[[1,2],[3,4]], [[5,6], [7,8]]]

print(multidimensial_list[0][0][0],"\n")
print(multidimensial_list[1][1][1])

print(multidimensial_list[0][0], "\n")
print(multidimensial_list[0])

klanten = [('Pim', 'Pershad', 'Hilversum'),('Jamil', 'Hermsen', 'Amsterdam'),('Susan', 'Kleijn', 'Maarssen')]
print(klanten)

for regel in klanten:
    for kolom in regel:
        print(kolom)
    print()

for regel in klanten:
    for kolom in regel:
        print(f"{kolom:<10}", end='')
    print()

