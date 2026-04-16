class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word.lower():
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True

    def autocomplete(self, prefix):
        current = self.root
        for ch in prefix.lower():
            if ch not in current.children:
                return []
            current = current.children[ch]

        results = []
        self._dfs(current, prefix.lower(), results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end:
            results.append(path)
        for ch, child in node.children.items():
            self._dfs(child, path + ch, results)
