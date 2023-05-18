"""
Handler for using Summarize NLP
"""
from string import punctuation
from heapq import nlargest
from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

#from datetime import datetime, timedelta


def summarize(text, per=0.1):
    """
    Summarize takes in a text string and reduces it to a percentage of the 
    original
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    #tokens = [token.text for token in doc]
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                #if word.text not in word_frequencies.keys():
                if word.text not in word_frequencies:
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())
    #for word in word_frequencies.keys():
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens) * per)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary

def summarize_url(url, per=0.1):
    """
    Takes in a URL, downloads the artical and returns a summary of the artical
    """
    article = Article(url)
    article.download()
    article.parse()

    return summarize(article.text, per)
