class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        state=0 #NESW-0123
        pos=[0,0]
        for i in instructions:
            if i=='L':
                state-=1
                if state<0:
                    state=3
            elif i=='R':
                state+=1
                if state>3:
                    state=0
            else:
                if state==0:
                    pos[1]+=1
                elif state==1:
                    pos[0]+=1
                elif state==2:
                    pos[1]-=1
                else:
                    pos[0]-=1
        return pos == [0, 0] or state != 0
