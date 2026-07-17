class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join([char.lower() for char in s if char.isalnum()])
        return sentence == sentence[::-1]        