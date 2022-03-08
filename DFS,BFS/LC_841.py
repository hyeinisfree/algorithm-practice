from collections import deque
from typing import List

class Solution:
    def canVisitAllRoom(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms
        self.seen = set()
        
        self.recurDFS(0)
        
        if len(self.rooms) == len(self.seen):
            return True   
        else:
            return False
    
    # Recursive
    def recurDFS(self, room_idx:int) -> None:
        self.seen.add(room_idx)
        keys = self.rooms[room_idx]
        
        for key in keys:
            if key not in self.seen:
                self.recurDFS(key)
    
    # Iterative
    def iterDFS(self, rooms) -> bool:
        seen = set()
        stack = []
        stack.append(0)
        seen.add(0)
        
        while stack:
            room_idx = stack.pop()
            keys = rooms[room_idx]
            
            for key in keys:
                if key not in seen:
                    stack.append(key)
                    seen.add(key)
                    
        if len(rooms) == len(seen):
            return True
        else:
            return False
    
    def BFS(self, rooms):
        seen = set()
        queue = deque()
        queue.append(0)
        seen.add(0)
        
        while queue:
            room_idx = queue.popleft()
            keys = rooms[room_idx]
            
            for key in keys:
                if key not in seen:
                    queue.append(key)
                    seen.add(key)
                    
        if len(rooms) == len(seen):
            return True
        else:
            return False