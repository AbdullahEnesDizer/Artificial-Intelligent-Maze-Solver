from A_star_search import A_StarSearch
from depth_first_search import DFS
from greedy_best_first_search import GreedyBestFirstSearch
from iterative_deepening_search import IterativeDeepeningSearch
from queue import LifoQueue


class GraphSearch:
    def __init__(self, strategy, grid, startState, goalNodes, cost=0, exploredSet=None, lastNode=None,
                 maxDepth=0, currentDepth=0, IDS_exploredSet=None, maxLenOfExploredSet=0, expandedNodesList=None):
        self.strategy = strategy
        self.grid = grid
        self.startState = startState
        self.goalNodes = goalNodes
        self.cost = cost
        self.exploredSet = exploredSet if exploredSet is not None else []
        self.lastNode = lastNode
        self.maxDepth = maxDepth
        self.currentDepth = currentDepth
        self.IDS_exploredSet = IDS_exploredSet if IDS_exploredSet is not None else []
        self.maxLenOfExploredSet = maxLenOfExploredSet

        self.expandedNodesList = expandedNodesList if expandedNodesList is not None else []

    def expandNode(self, curr_node):
        expandedNodes = []
        # east
        if not curr_node.eastWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex][curr_node.horizontalIndex + 1])
        # west
        if not curr_node.westWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex][curr_node.horizontalIndex - 1])
        # north
        if not curr_node.northWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex - 1][curr_node.horizontalIndex])
        # south
        if not curr_node.southWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex + 1][curr_node.horizontalIndex])

        return expandedNodes

    def checkInNotFrontierOrExploredSet(self, nextNode):
        return nextNode not in self.exploredSet and nextNode not in self.strategy.getAllFrontier()

    def search(self):
        if isinstance(self.strategy, (A_StarSearch, GreedyBestFirstSearch)):
            self.strategy.calculateHeuristicValues(self.grid, self.goalNodes)

        self.strategy.append(self.grid[self.startState[0]][self.startState[1]])

        while self.strategy.getLengthOfFrontier() > 0:
            curr_node = self.strategy.operate()

            if curr_node.status.startswith("G"):
                print(f"Founded goal state: {curr_node.status}")
                self.IDS_exploredSet.append(curr_node)
                self.cost = curr_node.cost
                self.lastNode = curr_node
                return "Goal"

            self.exploredSet.append(curr_node)
            self.maxLenOfExploredSet = max(self.maxLenOfExploredSet, len(self.exploredSet))



            # expand the node and add resulting nodes to the frontier
            expandedNodes = self.expandNode(curr_node)
            self.expandedNodesList += expandedNodes  # Genişletilen düğümleri kaydet

            IDS = isinstance(self.strategy, IterativeDeepeningSearch)
            if not IDS or (IDS and self.currentDepth <= self.maxDepth):
                if isinstance(self.strategy, DFS) or IDS:
                    expandedNodes.reverse()
                for nextNode in expandedNodes:
                    if self.checkInNotFrontierOrExploredSet(nextNode):
                        if nextNode.status == "T":
                            nextNode.cost = curr_node.cost + 7
                        else:
                            nextNode.cost = curr_node.cost + 1
                        nextNode.successor = curr_node
                        self.strategy.append(nextNode)
                self.currentDepth += 1
            else:
                self.IDS_exploredSet = self.IDS_exploredSet + self.exploredSet
                self.strategy.frontier = LifoQueue()
                self.cost = 0
                for row in self.grid:
                    for node in row:
                        node.successor = None
                self.exploredSet = []
                self.lastNode = None

                self.currentDepth = 0
                self.maxDepth += 1
                return self.search()

    def getExpandedNodesList(self):
        return self.expandedNodesList
    def printPath(self, node):
        if node is None:
            return
        self.printPath(node.successor)
        print(f"-({node.horizontalIndex + 1},{node.verticalIndex + 1})", end="")

    def printExploredSet(self):
        explored_coordinates = [f"({node.horizontalIndex + 1},{node.verticalIndex + 1})" for node in self.exploredSet]
        print(" ".join(explored_coordinates))

    def printIterativeDeepeningExploredSet(self):
        ids_explored_coordinates = [f"({node.horizontalIndex + 1},{node.verticalIndex + 1})" for node in
                                    self.IDS_exploredSet]
        print(" ".join(ids_explored_coordinates))