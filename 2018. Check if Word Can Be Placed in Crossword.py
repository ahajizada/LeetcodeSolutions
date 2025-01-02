class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def can_fit(segment,word):
            if len(segment) != len(word):
                return False
            
            for s_char, w_char in zip(segment,word):
                if s_char != ' ' and s_char != w_char:
                    return False
            
            return True
        

        for row in board:
            segments = ''.join(row).split('#')
            for segment in segments:
                if can_fit(segment, word) or can_fit(segment, word[::-1]):
                    return True

        
        for col in zip(*board):  
            segments = ''.join(col).split('#')
            for segment in segments:
                if can_fit(segment, word) or can_fit(segment, word[::-1]):
                    return True

        return False
