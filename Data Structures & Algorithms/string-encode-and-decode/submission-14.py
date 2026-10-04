class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.index("#",i)
            n = int(s[i:j])
            res.append(s[j+1 : j+1+n])
            i = j + 1 + n
        return res