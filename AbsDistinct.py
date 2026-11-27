def solution(A):
    # Create an empty set to store distinct absolute values
    distinct = set()

    for element in A:
        # Find the absolute value of the current element
        value = abs(element)

        # Add the value to the set without duplicates
        distinct.add(value)

    # Return the number of distinct absolute values
    return len(distinct)

#Test
print(solution([-5, -3, -1, 0, 3, 6]))

# Sources: Codility problem statement.
# AI assistance: ChatGPT provided pseudocode and Python solutions.
