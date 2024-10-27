
class TransportationProblem:
    def __init__(self, N):
        self.N = N
    def start_state(self):
        return 1
    def is_end(self, N):
        return N == self.N
    def actions(self, s):
        actions = []
        if s+1 <= self.N:
            actions.append("walk")
        if s*2 <= self.N:
            actions.append("tram")
        return actions
    def cost(self, a):
        if a == "walk":
            return 1
        elif a == "tram":
            return 2
        else:
            return 'inf'
    def succ(self, s, a):
        if a == "walk":
            return s+1
        elif a == "tram":
            return s*2
        else:
            return s
        
def backtracking_search():
    pass

def dfs(t):
    count = 0
    stack = []
    stack.append(t.start_state())
    while stack:
        node = stack.pop()
        if node == t.is_end(node):
            print(count)
        count += 1
        actions = []
        for i in t.actions(node):
            actions.append(i)
        stack.append(t.succ(node, actions[1])) if len(actions) > 1 else None
        stack.append(t.succ(node, actions[0])) if len(actions) > 0 else None
        print(stack)


def dynammic_programming():
    pass

def uniform_cost_search():
    pass

if __name__ == "__main__":
    t = TransportationProblem(10)
    print(t.succ(3, 'tram'))
    dfs(t)