class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        A=moves[::2]
        B=moves[1::2]
        wins=[
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]

        for win in wins:
            if all(list(cell) in A for cell in win):
                return 'A'
            if all(list(cell) in B for cell in win):
                return 'B'

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'
