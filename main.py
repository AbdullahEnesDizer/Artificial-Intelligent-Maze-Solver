from A_star_search import A_StarSearch
from breadth_first_search import BFS
from greedy_best_first_search import GreedyBestFirstSearch
from uniform_cost_search import UniformCostSearch
from depth_first_search import DFS
from graph_search import GraphSearch
from IO import IO
from iterative_deepening_search import IterativeDeepeningSearch

#dfs23
#bfs23
#ucs18
#a*18
#ıds23
#greedy23

def printOutputsOfGivenInput(filename):
    grid, goalNodes, startState = IO().readTheMazeInput(filename)

    print(" ")
    print("--DFS--")
    strategy1 = DFS()
    graphSearch1 = GraphSearch(strategy1, grid.copy(), startState, goalNodes)
    graphSearch1.search()
    print("Cost of the founded solution: " + str(graphSearch1.cost))
    print("The number of expanded nodes: " + str(len(graphSearch1.exploredSet)))
    print("Solution path: ")
    graphSearch1.printPath(graphSearch1.lastNode)
    print()

    print(" ")
    print("--BFS--")
    strategy2 = BFS()
    graphSearch2 = GraphSearch(strategy2, grid.copy(), startState, goalNodes)
    graphSearch2.search()
    print("Cost of the founded solution: " + str(graphSearch2.cost))
    print("The number of expanded nodes: " + str(len(graphSearch2.exploredSet)))
    print("Solution path: ")
    graphSearch2.printPath(graphSearch2.lastNode)
    print()

    print(" ")
    print("--IDS--")
    strategy3 = IterativeDeepeningSearch()
    graphSearch3 = GraphSearch(strategy3, grid.copy(), startState, goalNodes)
    graphSearch3.search()
    print("Cost of the founded solution: " + str(graphSearch3.cost))
    print("The number of expanded nodes: " + str(len(graphSearch3.IDS_exploredSet)))
    print("Solution path: ")
    graphSearch3.printPath(graphSearch3.lastNode)
    print()

    print(" ")
    print("--Uniform Cost--")
    strategy4 = UniformCostSearch()
    graphSearch4 = GraphSearch(strategy4, grid.copy(), startState, goalNodes)
    graphSearch4.search()
    print("Cost of the founded solution: " + str(graphSearch4.cost))
    print("The number of expanded nodes: " + str(len(graphSearch4.exploredSet)))
    print("Solution path: ")
    graphSearch4.printPath(graphSearch4.lastNode)
    print()

    print(" ")
    print("--Greedy Best--")
    strategy5 = GreedyBestFirstSearch()
    graphSearch5 = GraphSearch(strategy5, grid.copy(), startState, goalNodes)
    graphSearch5.search()
    print("Cost of the founded solution: " + str(graphSearch5.cost))
    print("The number of expanded nodes: " + str(len(graphSearch5.exploredSet)))
    print("Solution path: ")
    graphSearch5.printPath(graphSearch5.lastNode)
    print()

    print(" ")
    print("--A*--")
    strategy6 = A_StarSearch()
    graphSearch6 = GraphSearch(strategy6, grid.copy(), startState, goalNodes)
    graphSearch6.search()
    print("Cost of the founded solution: " + str(graphSearch6.cost))
    print("The number of expanded nodes: " + str(len(graphSearch6.exploredSet)))
    print("Solution path: ")
    graphSearch6.printPath(graphSearch6.lastNode)
    print()


if __name__ == "__main__":
    print("GIVEN MAZE OUTPUTS")
    printOutputsOfGivenInput('given_input.json')
