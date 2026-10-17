class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos=[0,0]
        for i in moves:
            if i=='R':
                pos[0]+=1
            elif i=='L':
                pos[0]-=1
            elif i=='U':
                pos[1]+=1
            else: 
                pos[1]-=1
        
        return pos==[0, 0]
        