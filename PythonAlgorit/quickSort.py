def quick_sort(aray, low, high):
    if low < high:
        pi = partition(aray, low, high)
        quick_sort(aray, low, pi - 1)
        quick_sort(aray, pi + 1, high)

def partition(aray, low, high):
    
    pivot = aray[high]
    i = low - 1
    
    for j in range(low, high):
        if aray[j] < pivot:
            i += 1
            aray[i], aray[j] = aray[j], aray[i]
    aray[i + 1], aray[high] = aray[high], aray[i + 1]
    return i + 1     

aray = [10, 7, 8, 9, 1, 5]
n = len(aray)
quick_sort(aray, 0, n - 1)  
print("Sorted array is:", aray)