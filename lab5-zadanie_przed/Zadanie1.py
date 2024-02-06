def sum_of_subsequence(numbers, length):
    max_subsequence = []
    if (length > len(numbers)):
        raise ValueError(
            "len of subseq cannot be bigger than len of initial seq")
    for i in range(len(numbers)-length+1):
        current_numbers = []
        for j in range(length):
            current_numbers.append(numbers[i+j])
        if (sum(current_numbers) > sum(max_subsequence)):
            max_subsequence = current_numbers
    return max_subsequence
