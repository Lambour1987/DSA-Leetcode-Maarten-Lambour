# filenames = ['a.txt', 'b.txt', 'c.txt']
#
# for filename in filenames:
#     file = open(f"files/{filenames}")


# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)

file = open("data.txt", 'w')

file.write("100.12\n")
file.write("111.23\n")



file.close()