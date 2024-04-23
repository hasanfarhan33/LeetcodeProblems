from collections import deque


graph = {
    'A': ['B', 'G'], 
    'B': ['C', 'D', 'E'], 
    'C': [], 
    'D': [], 
    'E': ['F'],
    'F': [], 
    'G': ['H'], 
    'H': ['I'], 
    'I': [], 
}

# Depth first search
def dfs(graph, node): 
    visited = set() 
    stack = [] 
    
    # Add the current node in visited and stack     
    visited.add(node) 
    stack.append(node) 
    
    # As long as the stack is not empty 
    while stack: 
        # Pop the top element from the stack 
        s = stack.pop() 
        print(s, end = " ") 
        
        for n in reversed(graph[s]): 
            # If the adjacent node is not visited, add it to the stack and visited 
            if n not in visited: 
                stack.append(n) 
                visited.add(n)

def bfs(graph, node): 
    visited = set() 
    queue = deque()
    
    visited.add(node)
    queue.append(node) 
    
    while queue: 
        s = queue.popleft() 
        print(s, end = " ")
        
        for n in graph[s]: 
            if n not in visited: 
                queue.append(n) 
                visited.add(n) 

def main(): 
    print("\nBreadth First Search: ")
    bfs(graph, "A")
    
    print("\nDepth First Search: ")
    dfs(graph, "A")
    
    
main() 