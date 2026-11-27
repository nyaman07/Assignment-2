def solution(A):
    N = len(A)

    # At least three elements are needed to form a triangle
    if N < 3:
        return 0

    # Sort the array in ascending order
    A.sort()

    # Check each group of three consecutive elements
    for i in range(N-2):
        # Check if the sum of the two smaller sides
        # is greater than the largest side
        if A[i] + A[i+1] > A[i+2]:
            return 1

    # No triangular triplet was found
    return 0

#Test
print(solution([10, 2, 5, 1, 8, 20]))

# Sources: Codility problem statement.
# AI assistance: ChatGPT provided pseudocode and Python solutions.
