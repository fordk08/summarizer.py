# summarizer.py
# basic summarizer script
# Make sure you have Python and the required NLTK library installed.
# to install the NLTK library, you can use the following command in your terminal or command prompt: pip install nltk

# content of the input text, the number of sentences in the input, and the value you set for the num_sentences parameter when calling the    
# summarize_text function.

# In the script provided the default value for num_sentences is 3. This means that the script will attempt to extract the top 3 most important # sentences from the input text based on word frequencies.

# Here are some general Tips:

# Short Input Texts: For short input texts, the output summary may also be short, potentially consisting of just a few sentences.

# Long Input Texts: If the input text is longer and more complex, the script may still produce a summary with a relatively small number of 
# sentences. The goal is to capture the most important information.

# Adjusting num_sentences: You can control the length of the output summary by adjusting the num_sentences parameter when calling the 
# summarize_text function. Increasing this value will result in longer summaries.
