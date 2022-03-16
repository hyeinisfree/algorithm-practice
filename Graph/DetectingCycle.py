from typing import List

class HasCycle:
    def hasCycle(self, graph:List[List[int]]) -> bool:
        self.graph = graph
        self.seen = set()
        
        for idx in range(len(graph)):
            loop_track = set()
            ret = self.recurDFS(idx, loop_track)
            if ret:
                return True
        
        return False
    
    def recurDFS(self, idx, loop_track) -> bool:
        if idx in self.seen:
            return False
        if idx in loop_track:
            return True
        
        loop_track.add(idx)
        nexts = self.graph[idx]
        for adj_idx in nexts:
            ret = self.recurDFS(adj_idx, loop_track)
            if ret:
                return True
        loop_track.remove(idx)
        
        self.seen.add(idx)
        return False
        
        
hasCycle = HasCycle()
print(hasCycle.hasCycle([[1],[],[0],[0,4],[1,6],[4],[5]]))