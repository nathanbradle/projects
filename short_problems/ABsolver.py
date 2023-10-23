'''
Removes "ABA" and "BBA" from a given string. Returns the minimum length of final solution after all removals.
Ensures it is the optimal solution.
Solved using Recursion
'''


def minimum_string(seq):
    return len(helper(seq, {}))

def helper(seq, memo):
    if seq in memo:
        return memo[seq]
    if "ABA" not in seq and "BBA" not in seq:
        return seq
    after_ABA = seq
    
    while "ABA" in after_ABA:
        after_ABA = after_ABA.replace("ABA", "", 1)
        after_ABA = helper(after_ABA, memo)
    after_BBA = seq
    while "BBA" in after_BBA:
        after_BBA = after_BBA.replace("BBA", "", 1)
        after_BBA = helper(after_BBA, memo)

    if after_ABA < after_BBA:
        memo[seq] = after_ABA
    else:
        memo[seq] = after_BBA
    return memo[seq]
    
def main():
    test_strings = ["ABBABBABAABABABABBBABBBABABB", "ABBBBBABABABBBBABABAAAA", "AABBBBABABABABABBBABABB", "BBABABABAB", "AAAA"]
    for s in test_strings:
        result = minimum_string(s)
        print(f"Original: {s}, Minimum: {result}")

if __name__ == "__main__":
    main()