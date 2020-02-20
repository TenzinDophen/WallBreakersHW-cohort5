from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = defaultdict(int)
        res = []
        for domains in cpdomains:
            arr = domains.split(" ")
            visit = arr[0]
            name = arr[1]
            #subnames = name.split(".")
            
            
            while("." in name):
                result[name] += int(visit)
                name = name[name.find(".")+1:]
            
            result[name] += int(visit)
            
        for key, val in result.items():
            stri = str(val) + " " + key
            res.append(stri)
            
        return res