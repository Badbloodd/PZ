def reverse_elements_between(A, K, L):
    if 1 < K < L < len(A):
        sublist_to_reverse = A[K-1:L]
        A[K-1:L] = sublist_to_reverse[::-1]
    else:
        print("Условие 1 < K < L < N не выполняется")

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 3
L = 7
reverse_elements_between(input_list, K, L)
print(input_list)
