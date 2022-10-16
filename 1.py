def fill_array(array, size):
    for i in range(size):
        print("Элемент", i+1, "= ", end="")
        array[i] = float(input()) 

def find_index_of_maximum(array, size):
    index = 0
    for i in range(1, size):
        if (array[i] >= array[index]):
            index = i
    return index

# -------------------------------------------------

N = int(input("Размерность массива: "))
numberArray = [0] * N

fill_array(numberArray, N)

print("Входной массив: ", numberArray)
		  
maxElementIndex = find_index_of_maximum(numberArray, N)

for i in range (maxElementIndex + 1, N):
    numberArray[i] = 0

print("Результат: ", numberArray)