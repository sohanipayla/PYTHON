def countSpecialElements(A):
    count = 0
    n = len(A)
    for i in range(n):
        temp = A[:i] + A[i+1:] 
        even_sum = sum(temp[j] for j in range(0, len(temp), 2))
        odd_sum = sum(temp[j] for j in range(1, len(temp), 2))

        if even_sum == odd_sum:
            count += 1
    return count
print(countSpecialElements([2, 1, 6, 4]))     
print(countSpecialElements([5, 5, 2, 5, 8]))  
