def solution(A):
    N = len(A)

    # Sort the array in ascending order
    A.sort()

    # Calculate the product of the three largest values
    product1 = A[N-1] * A[N-2] * A[N-3]

    # Two negative values can produce a positive product
    product2 = A[0] * A[1] * A[N-1]

    # Return the larger of the two products
    if product1 > product2:
        return product1
    else:
        return product2


#Test
print(solution([-3, 1, 2, -2, 5, 6]))

# Sources: Codility problem statement.
# AI assistance: ChatGPT provided pseudocode and Python solutions.
