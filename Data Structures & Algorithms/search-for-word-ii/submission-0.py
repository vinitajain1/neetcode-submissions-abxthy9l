class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        res = set()
        visit = set()
        rows = len(board)
        cols = len(board[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node.children or (r,c) in visit:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
            for dr,dc in directions:
                dfs(r+dr,c+dc,node,word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
