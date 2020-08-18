'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    sub_str = 'th'
    n1 = len(word)
    n2 = 2

    # Base Case
    if (n1 == 0 or n1 < n2):
        return 0

    # Recursive case
    if (word[0:n2] == sub_str):
        return count_th(word[n2-1:]) + 1

    # Otherwise return count from remaining index
    return count_th(word[n2-1:])
