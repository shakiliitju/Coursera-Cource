# Uses python3
import sys


class Trie:

    def __init__(self):
        self.tree = {0: {}}
        self.patterns = []
        self.max_index = 0

    def read(self):
        n = int(input())

        for _ in range(n):
            self.patterns.append(input())

    def build_trie(self):

        for pattern in self.patterns:
            node = 0

            for letter in pattern:
                if letter not in self.tree[node]:
                    self.max_index += 1
                    self.tree[node][letter] = self.max_index
                    self.tree[self.max_index] = {}

                node = self.tree[node][letter]
            self.tree[node]['$'] = '$'

        return self.tree

    def match(self, text):
        indexes = set()

        i = 0
        while i < len(text):
            j = i
            node = 0

            for letter in text[i:]:
                if letter not in self.tree[node]: break
                if '$' in self.tree[node]: break

                node = self.tree[node][letter]

            if '$' in self.tree[node]:
                indexes.add(i)
            i += 1

        return sorted(list(indexes))

    def print_trie(self):
        for node in self.tree:
            for letter in self.tree[node]:
                print('{}->{}:{}'.format(node, self.tree[node][letter], letter))


if __name__ == '__main__':
    text = input()

    trie = Trie()
    trie.read()
    trie.build_trie()

    indexes = trie.match(text)
    print(' '.join([str(x) for x in indexes]))