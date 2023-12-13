import pandas as pd
from nltk import FreqDist, word_tokenize
from nltk.util import ngrams
import os

# Check the path of the desktop
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Load the Excel file
df = pd.read_excel(f'{desktop_path}/Friction Points by Category - Clean.xlsx')

# Assuming that 'text' is the column with the text you want to analyze
texts = df['feedback']

# Tokenize the texts and create bigrams
bigrams = []
for text in texts:
    tokens = word_tokenize(text)
    bigrams.extend(list(ngrams(tokens, 2)))

# Count the bigram frequencies
bigram_freq = FreqDist(bigrams)

# Print the top 10 most common bigrams
for bigram, freq in bigram_freq.most_common(10):
    print(f"{' '.join(bigram)}: {freq}")