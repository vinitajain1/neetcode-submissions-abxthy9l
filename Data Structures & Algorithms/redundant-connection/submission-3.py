class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Make set
        par = [i for i in range(len(edges)+1)]
        #Make rank
        rank = [1] * (len(edges) + 1)

        #find
        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            return par[n]
        #union
        def union(n1,n2):
            parn1 = find(n1)
            parn2 = find(n2)
            if parn1==parn2:
                return False
            if rank[parn1] > rank[parn2]:
                par[parn2] = parn1
                rank[parn1]+= rank[parn2]
            else:
                par[parn1] = parn2
                rank[parn2]+=rank[parn1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]