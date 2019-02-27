def permutations(string):
    if len(string) <= 1:
        return [string]

    all_perms = []

    for i, char in enumerate(string):
        remainder = string[:i] + string[i+1:]
        suffixes = permutations(remainder)
        all_perms += [ char + suffix for suffix in suffixes ] 

    return all_perms

# print(permutations("abc"))
