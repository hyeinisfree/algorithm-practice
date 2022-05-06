from typing import List

class HasCycle:
    def hasCycle(self, graph) -> bool:
        self.graph = graph
        self.seen = set()
        
        for idx in graph:
            loop_track = set()
            ret = self.recurDFS(idx, loop_track)
            if ret:
                print(loop_track)
                break
        
        return False
    
    def recurDFS(self, idx, loop_track) -> bool:
        if idx in self.seen:
            return False
        if idx in loop_track:
            return True
        
        print(idx)
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
print(hasCycle.hasCycle({'b': ['c'], 'a': ['b'], 'e': ['f'], 'h': [], 'd': ['e'], 'f': ['d'], 'c': []}))