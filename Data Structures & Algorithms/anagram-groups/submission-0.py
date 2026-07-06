class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=defaultdict(list)
        for i in strs:
            sorteds="".join(sorted(i))
            s[sorteds].append(i)
        return list(s.values())