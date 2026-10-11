list = [62, 19, 26, 4, 21, 9, 19, 48, 21, 99]

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp
    return list 

print(selection_sort(list))
print(bubble_sort(list))
