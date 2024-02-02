from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        print(sorted_word)
        if sorted_word not in d:
            d[sorted_word] = [word]
        else:
            d[sorted_word].append(word)

    result = []

    for item in d.values():
        result.append(item)
    return result 

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))