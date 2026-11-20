class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_string = ""
        shorter = None
        len1 = len(word1)
        len2 = len(word2)
        if len1 < len2:
            shorter = len1
            for i in range(0, shorter):
                final_string += word1[i]
                final_string += word2[i]
            # Add leftovers
            final_string += word2[shorter:]
            return final_string
        elif len2 < len1:
            shorter = len2
            for i in range(0, shorter):
                final_string += word1[i]
                final_string += word2[i]
            # Add leftovers
            final_string += word1[shorter:]
            return final_string
        elif len1 == len2:
            # doesnt matter which one we choose, they are same length
            for i in range(0, len1):
                final_string += word1[i]
                final_string += word2[i]
            return final_string