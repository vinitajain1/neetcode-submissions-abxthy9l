class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)
        
        queue = deque()
        visit = set()
        queue.append(beginWord)
        res=0
        while queue:
            res+=1
            for i in range(len(queue)):
                elem = queue.popleft()
                if elem==endWord:
                    return res
                visit.add(elem)
                for i in range(len(elem)):
                    pattern = elem[:i]+"*"+elem[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            queue.append(nei)

        return 0
