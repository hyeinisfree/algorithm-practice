from typing import List

class Solution:
    def canFinish(self, numCourses:int, prerequisites:List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.seen = set()
        
        for start, to in prerequisites:
            self.graph[start].append(to)
            
        for idx in range(numCourses):
            loop_track = set()
            ret = self.recurDFS(idx, loop_track)
            if ret:
                return False
        
        return True

    def recurDFS(self, idx, loop_track):
        if idx in self.seen:
            return False
        if idx in loop_track:
            return True
        
        loop_track.add(idx)
        
        nexts = self.graph[idx]
        for next_idx in nexts:
            ret = self.recurDFS(next_idx, loop_track)
            if ret:
                return True
        
        loop_track.remove(idx)
        self.seen.add(idx)
        
        return False