def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    arr=[None]*n
    for i in range(n):
        arr[i]=[None]*n
    return arr


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count=0
    for i in arr:
        if i is not None:
            count+=1
        else:
            break
    return count

def divide_chunks(arr: list[int], chunk_size: int) -> list[list[int]]:
    """
    A fruitful function that takes an array and chunk size as arguments and divides the array into chunks of size k.
    """
    number_of_chunks=int((length(arr)+chunk_size-1)/chunk_size)
    single_chunk=[None]*chunk_size 
    chunks=[None]*number_of_chunks
    current_i=0
    count=0
    for i in range(length(arr)):
        single_chunk[count]=arr[i]
        count+=1
        if i==length(arr)-1 or count==chunk_size: #until the chunk_size is reached to create a new chunk
            n_chunk=[None]*count
            for j in range(count): 
                n_chunk[j]=single_chunk[j]
            chunks[current_i]=n_chunk
            count=0
            current_i+=1
            single_chunk=[None]*chunk_size
    return chunks

def selection_sort(arr: list[int]) -> None:
    """
    A void function that takes an array and sorts it in descending order using the selection sort algorithm.
    This is an in-place function, meaning the original array that was passed as a reference will be updated with the
    sorted values.

    The function should not return anything.
    """
    for i in range(length(arr)):
        maximum=i
        for j in range(i+1,length(arr)):
            if arr[j]>arr[maximum]:
                maximum=j
        arr[i],arr[maximum]=arr[maximum],arr[i]
        print(arr)

def consolidate(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    A fruitful function that combines two sorted arrays into one sorted array using a two-pointer approach,
    in a descending order.

    The function returns the updated, sorted array
    """
    sorted_array=[None]*(length(arr1)+length(arr2))
    pointer1=0
    pointer2=0
    for i in range(length(arr1)+length(arr2)):
        if pointer1>=length(arr1): #for any remaining element
            sorted_array[i]=arr2[pointer2]
            pointer2+=1
        elif pointer2>=length(arr2): #for any remaining element
            sorted_array[i]=arr1[pointer1]
            pointer1+=1
        elif arr1[pointer1]>=arr2[pointer2]:
            sorted_array[i]=arr1[pointer1]
            pointer1+=1
        else:
            sorted_array[i]=arr2[pointer2]
            pointer2+=1
    return sorted_array

def fusion_sort(arr: list[int]) -> list[int]:
    """
    A fruitful function that implements the “Fusion Sort” algorithm described above to sort the valid data items
    in a descending order, while preserving the positions of invalid items.

    The function returns the updated, sorted array
    """
    n=1
    for num in arr:
        if num is not None:
            n=0
            break  
    if n==1:
        return arr 
    chunk_size=int(length(arr)**0.5)
    chunks=divide_chunks(arr,chunk_size)
    for a_chunk in chunks:  #sort each chunk 
        selection_sort(a_chunk)

    array_sorted=chunks[0]
    for i in range(1,length(chunks)):
        array_sorted=consolidate(array_sorted,chunks[i])
    descending_array=[None]*len(arr)
    sorted_index=0
    for i in range(len(arr)):
        if arr[i] is None:
            descending_array[i]=None
        else:
            descending_array[i]=array_sorted[sorted_index]
            sorted_index+=1
    return descending_array

def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply fusion sorting algorithm to get the sorted arrays and returns the output, sorted array.
    """
    with open(filename) as f:  
        lines = f.read().strip()
    array=[]  
    str=""  
    for i in range(len(lines)):  
        if lines[i].isdigit():  
            str+=lines[i]
        elif lines[i]==',' or i==len(lines) - 1:  #if we have reached the end of file or the comma
            if str: 
                array+=[int(str)] 
                str=''
            else:
                array+=[None] 
    count=0
    for num in array:
        if num is not None:
            count+=1
    if count==0:
        return array
    return fusion_sort(array)

if __name__ == "__main__":
    print(main("sorting\\Inputs\\sorting01.txt"))
