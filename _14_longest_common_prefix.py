from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs or len(strs) == 0:
        return ""
    res=""
    l = list(zip(*strs))
    for c in l:
        if len(set(c)) == 1:
            res += c[0]
        else:
            break
    return res


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))