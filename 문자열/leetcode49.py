import collections


def groupAnagrams1(strs):
    sorted_strs = []
    for s in strs:
        sorted_strs.append("".join(sorted(s)))

    anagramGroup = {}
    for i in range(len(strs)):
        if anagramGroup:
            if sorted_strs[i] in anagramGroup:
                anagramGroup[sorted_strs[i]].append(strs[i])
            else:
                anagramGroup[sorted_strs[i]] = [strs[i]]
        else:
            anagramGroup[sorted_strs[i]] = [strs[i]]

    return anagramGroup.values()


def groupAnagrams2(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


print(groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams1([""]))
print(groupAnagrams2(["a"]))
print(groupAnagrams2(["hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt"]))
