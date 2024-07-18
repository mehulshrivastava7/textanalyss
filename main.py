import string
import matplotlib.pyplot as plt
from collections import Counter
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
# print(string.punctuation)
new = lower_case.translate(str.maketrans('','',string.punctuation))
# working of maketrans : 1-list of char that need to be replaced , 2 - replace them with these , 3 - delete these characters.
tokenword = new.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenword:
    if word not in stop_words:
        final_words.append(word)
list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n" , "").replace("'","").strip()
        word,emotion = clear_line.split(':')
        # print(word)
        if word in final_words:
            list.append(emotion)
# print(list)
w = Counter(list)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()

