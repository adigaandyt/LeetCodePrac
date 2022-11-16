# Map each character of each word to each other
# and check if the character is already mapped return false
# need 2 maps because Isomorphic goes both ways

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            # go through each character in each word
            c1, c2 = s[i], t[i]

            # Check if character is already mapped
            if ((c1 in mapST and mapST[c1] != c2) or
                    (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # map each character to each other
            mapST[c1] = c2
            mapTS[c2] = c1
        return True
