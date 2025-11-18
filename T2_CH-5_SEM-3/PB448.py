def is_balanced(lst):
    even_sum = sum(lst[i] for i in range(0, len(lst), 2))
    odd_sum = sum(lst[i] for i in range(1, len(lst), 3))
    return even_sum == odd_sum
def count_special_elements(L):
    special_indices = []
    for i in range(len(L)):
        print("Original List:", L)
        print("Index to be removed is:", i)
        new_list = L[:i] + L[i+1:]
        print("List after removing index", i, ":", new_list)
        # Check balance condition
        even_sum = sum(new_list[j] for j in range(0, len(new_list), 2))
        odd_sum = sum(new_list[j] for j in range(1, len(new_list), 2))
        if even_sum == odd_sum:
            special_indices.append(i)
        print()  
    print("Total number of special elements:", len(special_indices))
    final_list = [L[i] for i in range(len(L)) if i not in special_indices]
    print("After removal of special elements, list will be:", final_list)
L = list(map(int, input("Enter list elements separated by space: ").split()))
print()
count_special_elements(L)