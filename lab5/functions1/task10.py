def unique(array):
    ans = list()
    for e in array:
        if e not in ans: ans.append(e)
    return ans