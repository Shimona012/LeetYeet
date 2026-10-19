class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x=coordinates[1][0]-coordinates[0][0]
        y=coordinates[1][1]-coordinates[0][1]
        for i in coordinates[2:]:
            if (i[0]-coordinates[0][0])*y!=(i[1]-coordinates[0][1])*x:
                return False
        return True