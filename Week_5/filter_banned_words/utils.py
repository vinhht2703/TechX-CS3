from banned_words_data import banned_words_data


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def search_in_message(self, message):
        node = self.root
        indices = []
        for i in range(len(message)):
            node = self.root
            for j in range(i, len(message)):
                if message[j] not in node.children:
                    break
                node = node.children[message[j]]
                if node.end_of_word:
                    indices.append((i, j))
        return indices


# Initialize the Trie and insert banned words
banned_words_trie = Trie()

for word in banned_words_data:
    banned_words_trie.insert(word)

def hide_banned_words(message):
    indices = banned_words_trie.search_in_message(message)
    message_list = list(message)
    for start, end in indices:
        for i in range(start, end + 1):
            message_list[i] = "*"
    return "".join(message_list)
