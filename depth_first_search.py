from queue import LifoQueue


class DFS:
    def __init__(self):
        self.frontier = LifoQueue()

    def operate(self):
        if not self.frontier.empty():
            node = self.frontier.get()
            return node
        else:
            return None

    def append(self, node):
        self.frontier.put(node)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
