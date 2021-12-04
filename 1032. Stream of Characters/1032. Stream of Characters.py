class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque()
        self.trie = TrieNode()
        for word in set(words):
            cur = self.trie
            for c in word[::-1]:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        cur = self.trie
        for c in self.stream:
            if cur.isEnd:
                return True
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
