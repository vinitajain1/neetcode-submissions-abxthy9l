class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        res = set()
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c,node,word):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or board[r][c] not in node.children:
                return
            ch = board[r][c]
            node = node.children[ch]
            word+=ch
            visited.add((r,c))
            if node.endOfWord:
                res.add(word)
            for dr,dc in directions:
                dfs(dr+r,dc+c,node,word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)