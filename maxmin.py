#Maxima Minima

# For finding the maxima if available from the Array
def findMaxima(arr, low, high):
    if high == low + 1:
        return False
    else:
        mid = (low + high)//2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return 'maxima ' + str(arr[mid])
        elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            low = mid
            return findMaxima(arr, low, high)
        else:
            high = mid
            return findMaxima(arr, low, high)

#For finding the minima if available from the Array
def findMinima(arr, low, high):
    if high == low + 1:
        return False
    else:
        mid = (low + high)//2
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return 'minima ' + str(arr[mid])
        elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            high = mid
            return findMinima(arr, low, high)
        else:
            low = mid
            return findMinima(arr, low, high)

#For finding if array is strictly increasing or strictly decreasing
def findSorted(arr, low, high):
    if low == high:
        return True
    if (high - low) == 1:
        return arr[high] >= arr[low]
    mid = (high + low) // 2
    return findSorted(arr, low, mid) and findSorted(arr, mid, high)


# Main
if __name__ == "__main__":
    with open('outputPS14.txt', 'w') as fileOut:
        with open('inputPS10.txt') as f:
          for line in f:
            inputArray = list(map(int, line.split(' ')))
            result = False
            result = findMinima(inputArray, 0, len(inputArray)-1)
            if(result):
                fileOut.write(result + '\n')
            else:
                result = findMaxima(inputArray, 0, len(inputArray)-1)
                if(result):
                    fileOut.write(findMaxima(
                        inputArray, 0, len(inputArray)-1) + '\n')
                else:
                    result = findSorted(inputArray, 0, len(inputArray)-1)
                    if(result):
                        fileOut.write('increasing ' +
                                      str(inputArray[0]) + '\n')
                    else:
                        fileOut.write('decreasing ' +
                                      str(inputArray[-1]) + '\n')
        f.close()
    fileOut.close()
