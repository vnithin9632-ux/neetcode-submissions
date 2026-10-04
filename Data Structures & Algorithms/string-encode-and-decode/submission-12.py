class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: 
            s = '😏'
            return s
        else:
            s = "😁".join(strs)
            return s
    def decode(self, s: str) -> List[str]:
        if s == '😏':
            s = [] 
            return s
        else:
            decoded = s.split("😁")
            return decoded