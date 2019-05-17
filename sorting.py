#bubble sort
def bubbleSort(array):
	#go left to right, switch values if left is < right
	#do repeatedly until no swaps made on 1 runthrough
	swapped = True
	while swapped == True:
		swaps = 0
		for i in range(len(array)):
			if i+1 < len(array):
				if array[i] > array[i+1]:
					swap(i,i+1,array)
					swaps += 1
		if swaps > 0:
			swapped = True
		else:
			swapped = False
	return array

#insertion sort
def insertionSort(array):
	#for every element after first element, push it left if it is greater than current element
	for i in range(1,len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			swap(j,j-1,array)
			j -= 1	
	return array

#selection sort
def selectionSort(array):
	currentIdx = 0
	while currentIdx < len(array):
		minIdx = currentIdx
		for i in range(currentIdx,len(array)):
			if array[i] < array[minIdx]:
				minIdx = i
		swap(minIdx,currentIdx,array)
		currentIdx += 1
	return array

def swap(x,y,arr):
	arr[x],arr[y] = arr[y],arr[x]


def main():
	og = [8,5,2,9,5,6,3]
	unsort = [8,5,2,9,5,6,3]
	print(og, "-> bubble sort ->", bubbleSort(unsort)) 
	print(og, "-> insertion sort ->", insertionSort(unsort))
	print(og, "-> selection sort ->", selectionSort(unsort))


main()