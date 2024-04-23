'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] 
indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node
of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, 
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

from collections import defaultdict, deque
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]: 
    adj = defaultdict(list)
    
    for n1, n2 in edges: 
        adj[n1].append(n2)
        adj[n2].append(n1)
        
    edge_cnt = {} 
    leaves = deque() 
    
    for src, neighbors in adj.items(): 
        if len(neighbors) == 1: 
            leaves.append(src)
        edge_cnt[src] = len(neighbors)
        
    while leaves:
        if n <= 2: 
            return list(leaves)
        for i in range(len(leaves)): 
            node = leaves.popleft()
            n -= 1
            for nei in adj[node]: 
                edge_cnt[nei] -= 1
                if edge_cnt[nei] == 1: 
                    leaves.append(nei)
                    