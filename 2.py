from random import randint

def create_array():
	N = int(input("Размерность нового массива: "))
	array = [0] * N
	for i in range(N):
		array[i] = randint(-5, 5)
	return array

# ------------------------------------------------------

array1 = create_array()
array2 = create_array()

print("Первый массив: ", array1)
print("Второй массив: ", array2)

resultArray = []

for i in array1:
    if i in array2:
      resultArray.append(i), array2.remove(i)

print(resultArray)