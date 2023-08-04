#define a function for this task:
def multiple_duplicates_check(arr):

    #initialize a dictionary to store each integer and it's count:
    counts = {}

    #initialize a list to store numbers having multiple duplicates:
    duplicates = []

    #Run a for loop to check th input array and append to the dictionary, it's respective count:
    for num in arr:

        #checking if the number exists in the dictionary:
        if num in counts:
            counts[num] +=1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if counts[num] > 2:
            duplicates.append(num)

    return duplicates

arr = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9]
results = multiple_duplicates_check(arr)
for j in results:
    print(j)
