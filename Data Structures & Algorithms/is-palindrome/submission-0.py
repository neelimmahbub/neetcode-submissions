class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join([char.lower() for char in s if char.isalnum()])
        reverse_sentence = sentence[::-1]
        return sentence == reverse_sentence        