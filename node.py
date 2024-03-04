import math


class Node:
    def __init__(self, status, eastWall, westWall, northWall, southWall, verticalIndex, horizontalIndex):
        self.status = status
        self.eastWall = eastWall
        self.westWall = westWall
        self.northWall = northWall
        self.southWall = southWall
        self.verticalIndex = verticalIndex
        self.horizontalIndex = horizontalIndex
        self.cost = 0
        self.successor = None
        self.heuristicCost = math.inf

    def __gt__(self, other):
        if self.cost > other.cost:
            True
        else:
            False
