RANGE = 500

for i in range(1, RANGE+1):
    length = len(str(i))
    i_arr = str(i)
    narcis_array = [int(x)**length for x in i_arr]
    narcis_num = sum(narcis_array)
    if narcis_num == i:
        print(i)



