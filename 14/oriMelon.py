K = int(input())
max_height,max_width = 0,0
max_width_index,max_height_index = 0,0
info = []  
for i in range(6):
    temp = list(map(int, input().split()))
    info.append(temp)
    if temp[0] == 1 or temp[0] == 2:  
        if max_width < temp[1]:  
            max_width,max_width_index = temp[1], i
    else:
        if max_height < temp[1]: 
            max_height,max_height_index = temp[1], i  
index_list = [info[max_height_index - 1], info[(max_height_index + 1) % 6], info[max_width_index - 1],
              info[(max_width_index + 1) % 6]]
product = 1  
for i in info:  
    if i not in index_list:  
        product *= i[1]  

result = (max_width * max_height - product) * K 
print(result)