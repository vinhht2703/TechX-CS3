
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# car  =>  c  a  r
# cat  =>  c  a  t


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def print_tree(self):
        self._print_tree(self.root, "")

    def _print_tree(self, node, current_prefix):
        if node.is_end_of_word == True:
            print(current_prefix)
        for char, child_node in node.children.items():
            self._print_tree(child_node, current_prefix + char)


    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self._find_words_with_prefix(node, prefix)

    def _find_words_with_prefix(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
            
        for char, child_node in node.children.items():
            results.extend(self._find_words_with_prefix(child_node, prefix + char))

        return results



lstDemo = ["car","bat","batman","card","banana","cat"]

trie = Trie()

for item in lstDemo:
    trie.insert(item)

findChar = input("nhập từ tìm kiếm: ")
print(trie.search(findChar))


# đệ quy