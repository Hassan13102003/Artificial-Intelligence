#Rabbit Leap Problem
#Problem Statement:
# In the rabbit leap problem, three east-bound rabbits stand in a line blocked by three west-bound rabbits. 
# They are crossing a stream with stones placed in the east west direction in a line.
#     There is one empty stone between them. Rabbits waiting to cross. Each rabbit can jump over one, but not more than that. 
#     How can they avoid getting into a deadlock? The rabbits can only move forward one step or two steps. 
#     They can jump over one rabbit if the need arises, but not more than that. Are they smart enough to cross each other without having to step into the water? 
#     Draw the state space for solving the problem.
class Problem:
    def __init__(self):
        pass
    def isValid(self, curstate):
        flag = 0
        for i, j in enumerate(curstate):
            if j in ["RE1", "RE2", "RE3"]:
                if i <= 4:
                    if curstate[i+1] == "_" or curstate[i+2] == "_":
                        flag = 1
            elif i == 5:
                if curstate[i+1] == "_":
                    flag = 1
            if j in ["RW1", "RW2", "RW3"]:
                if i >= 2:
                    if curstate[i-1] == "_" or curstate[i-2] == "_":
                        flag = 1
                elif i == 1:
                    if curstate[i - 1] == "_":
                        flag = 1
        return True if flag else False

    def isfinal(self, curstate):
        if curstate == ["RW1", "RW2", "RW3", "_", "RE1", "RE2", "RE3"]:
            return True
        return False

    def print(self, path):
        path.reverse()
        for x, y in enumerate(path):
            z = "0" if x < 10 else ""
            print(f"Step {z}{x}: {y}")
        print()

class BFS:
    def __init__(self):
        self.visited = set()
        self.q = [["RE1", "RE2", "RE3", "_", "RW1", "RW2", "RW3"]]
        self.start = ["RE1", "RE2", "RE3", "_", "RW1", "RW2", "RW3"]
        self.check = Problem()
        self.parent = {}

    def bfs(self):
        for curstate in self.q:
            if self.check.isfinal(curstate):
                ans = []
                temp = str(curstate)
                while temp!= str(self.start):
                    ans.append(temp)
                    temp = self.parent.get(temp)
                ans.append(self.start)
                return ans
            else:
                if self.check.isValid(curstate):
                    par = str(curstate)
                    for i in range(7):
                        if curstate[i] in ["RE1", "RE2", "RE3"]:
                            if i<=4:
                                if curstate[i+2] == "_":
                                    nextstate = curstate.copy()
                                    nextstate[i], nextstate[i + 2] =nextstate[i + 2], nextstate[i]

                                    if str(nextstate) not in self.visited:
                                        self.q.append(nextstate)
                                        self.visited.add(str(nextstate))
                                        self.parent.update({str(nextstate): par})

                            if i <= 5:
                                if curstate[i + 1] == "_":
                                    nextstate = curstate.copy()
                                    nextstate[i], nextstate[i + 1] =nextstate[i + 1], nextstate[i]

                                    if str(nextstate) not in self.visited:
                                        self.q.append(nextstate)
                                        self.visited.add(str(nextstate))
                                        self.parent.update({str(nextstate): par})

                        elif curstate[i] in ["RW1", "RW2", "RW3"]:
                            if i >= 2:
                                if curstate[i - 2] == "_":
                                    nextstate = curstate.copy()
                                    nextstate[i], nextstate[i - 2] =nextstate[i - 2], nextstate[i]

                                    if str(nextstate) not in self.visited:
                                        self.q.append(nextstate)
                                    self.visited.add(str(nextstate))
                                    self.parent.update({str(nextstate): par})

                            if i >= 1:
                                if curstate[i - 1] == "_":
                                    nextstate = curstate.copy()
                                    nextstate[i], nextstate[i - 1] =nextstate[i - 1], nextstate[i]

                                    if str(nextstate) not in self.visited:
                                        self.q.append(nextstate)
                                        self.visited.add(str(nextstate))
                                        self.parent.update({str(nextstate): par})


if __name__ == "__main__":
    show = Problem()
    ans_bfs = BFS()
    path_bfs = ans_bfs.bfs()
    show.print(path_bfs)


