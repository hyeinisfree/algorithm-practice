from typing import List

class Solution:
    def restoreIpAddresses(self, s:str) -> List[str]:
        self.result = []
        self.s = s
        IPs = []
        self.bt(0, IPs)
        return self.result
        
    def valid(self, num_str:str) -> bool:
        if len(num_str) == 1:
            return True
        if num_str[0] == '0':
            return False
        if int(num_str) > 255:
            return False
        return True
        
    def bt(self, idx:int, IPs:List[str]):
        if len(IPs) > 4:
            return
        elif idx==len(self.s) and len(IPs)==4:
            IP = '.'.join(IPs)
            self.result.append(IP)
            return
        
        s_length = len(self.s)
        idx_p3 = idx + 3
        for end_idx in range(idx, min(s_length, idx_p3)):
            num_str = self.s[idx:end_idx+1]
            if self.valid(num_str):
                IPs.append(num_str)
                self.bt(idx+len(num_str), IPs)
                IPs.pop()