#Missionaries and Cannibals game
#Problem Statement:
# The missionaries and cannabels problem is usually stated as follows (see the figure given below). 
# Three missionaries and three cannibals are on one side of a river, along with a boat that can hold one or two people. 
# Find a way to get everyone to the other side without ever leaving a group of missionaries in one place outnumbered by the cannibals in that place. 
# This problem is famous in AI because it was the subject of the first paper that approached problem formulation from an analytical viewpoint.



class Problem:
    def __init__(self):
        pass
    def isValid(self, aside):
        if aside[0]<aside[1] and aside[0]>0:
            return False
        if aside[0]>3 or aside[1]>3 or aside[0]<0 or aside[1]<0:
            return False
        if (3-aside[0])<(3-aside[1]) and (3-aside[0])>0:
            return False
        if (3-aside[0])>3 or (3-aside[1])>3 or (3-aside[0])<0 or (3-aside[1])<0:
            return False
        return True
    def isfinal(self, aside):
        if aside[0]==0 and aside[1]==0 and aside[2]==1:
            return True
        return False
    def print(self, path):
        path.reverse()
        print(f" [Missionaries, Cannable, Boat]")
        for x,y in enumerate(path):
            z = "0" if x<10 else ""
            print(f"Iteration {z}{x}: {y}")
        print()

class BFS:
    def __init__(self):
        self.states = [[0,1],[1,0],[1,1],[0,2],[2,0]]
        self.visited = set()
        self.q = [[3,3,0]]
        self.start = [3, 3, 0]
        self.check = Problem()
        self.parent = {}

    def bfs(self):
        for cur in self.q:
            scur = str(cur)

            if self.check.isfinal(cur):
                ans = []
                temp = scur
                while temp != str(self.start):
                    ans.append(temp)
                    temp = self.parent.get(temp)
                ans.append(self.start)
                return ans

            for state in self.states:
                if cur[2] == 0:
                    nex = [cur[0] - state[0], cur[1] - state[1], 1]
                    if self.check.isValid(nex):
                        if str(nex) not in self.visited:
                            self.visited.add(str(nex))
                            self.q.append(nex)
                            self.parent.update({str(nex): scur})
                else:
                    nex = [cur[0] + state[0], cur[1] + state[1], 0]
                    if self.check.isValid(nex):
                        if str(nex) not in self.visited:
                            self.visited.add(str(nex))
                            self.q.append(nex)
                            self.parent.update({str(nex): scur})

if __name__ == "__main__":
    show = Problem()
    ans_bfs = BFS()
    path_bfs = ans_bfs.bfs()
    show.print(path_bfs, )
