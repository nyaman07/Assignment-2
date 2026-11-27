def solution(A):
    N = len(A)

    # Sort the array in ascending order
    A.sort()

    # Initialize pointers at both ends of the array
    left = 0
    right = N-1

    # Initialize the minimum absolute sum
    minimum = abs(A[left] + A[right])

    # Allow both pointers to refer to the same element
    while left <= right:
        total = A[left] + A[right]

        # Update the minimum if a smaller value is found
        if abs(total) < minimum:
            minimum = abs(total)

        # Move the left pointer to increase a negative sum
        if total < 0:
            left = left + 1

        # Move the right pointer to decrease a positive sum
        elif total > 0:
            right = right - 1

        # Zero is the smallest possible absolute sum
        else:
            return 0

    return minimum

#Test
print(solution([1, 4, -3]))

# Sources: Codility problem statement.
# AI assistance: ChatGPT provided pseudocode and Python solutions.
