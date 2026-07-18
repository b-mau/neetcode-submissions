class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            letters = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                letters[index] += 1
            key = tuple(letters)
            if key not in dic:
                dic[key] = []
            dic[key].append(word)

        return(list(dic.values()))


        