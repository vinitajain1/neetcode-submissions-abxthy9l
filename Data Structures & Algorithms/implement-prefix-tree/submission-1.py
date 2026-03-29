class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndNode = False
class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndNode = True
    def search(self, word: str) -> bool:
        currNode = self.trie
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c] 
        return currNode.isEndNode
    def startsWith(self, prefix: str) -> bool:
        currNode = self.trie
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True
        