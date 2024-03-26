lst = []

with open("WORDSSSS/words.txt") as w:
    for i in w:
        temp = i.rstrip("\r\n")
        if(len(temp) == 4):
            lst.append(temp)

str1 = "time"
str2 = "gift"
intermediate_target = ""

import networkx as nx
from nltk.corpus import words

def is_one_char_apart(word1, word2):
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1

def create_word_graph(word_list):
    G = nx.Graph()
    for word1 in word_list:
        G.add_node(word1)
        for word2 in word_list:
            if word1 != word2 and is_one_char_apart(word1, word2):
                G.add_edge(word1, word2)
    return G

def find_shortest_path(graph, start, end):
    try:
        return nx.shortest_path(graph, start, end)
    except nx.NetworkXNoPath:
        return None

# Get a list of 4-letter words
word_list = lst

# Create a word graph
word_graph = create_word_graph(word_list)

# Find the shortest path from "time" to "gift"
start_word = "time"
end_word = "gift"
shortest_path = find_shortest_path(word_graph, start_word, end_word)

# Print the result
if shortest_path:
    print(f"Shortest path from {start_word} to {end_word}: {shortest_path}")
else:
    print(f"No path found from {start_word} to {end_word}")
