# To use this script:

# Save the code in a file named summarizer.py.
# Make sure you have Python and the required NLTK library installed.
# Run the script from the command line or terminal: python summarizer.py "This is the text you want to summarize."

import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequency
    freq_dist = FreqDist(words)

    # Rank sentences based on the sum of their word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_dist.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq

    # Get the top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    return ' '.join(top_sentences)

if __name__ == "__main__":
    # Check if text is provided as a command line argument
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
    else:
        # If no command line argument is provided, prompt the user
        input_text = input("Paste the text you want to summarize:\n")

    # Summarize the text
    summary = summarize_text(input_text)

    # Print the summary
    print("\nSummary:\n", summary)
