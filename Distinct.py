def solution(A):
    # Create an empty set to store distinct values
    distinct = set()

    # Add each element to the set, which removes duplicates
    for element in A:
        distinct.add(element)

    # Return the number of distinct values
    return len(distinct)

#Test
print(solution([2, 1, 1, 2, 3, 1]))

# Sources: Codility problem statement.
# AI assistance: ChatGPT provided pseudocode and Python solutions.
