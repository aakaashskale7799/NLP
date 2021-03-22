#Npl practical 1
#Write a program to do a text normalization of English Text

import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
p_stemmer = PorterStemmer()

def nltk_process(text):
    #Tokenization: converting sentence to list of words
     nltk_tokenList = word_tokenize(text)
     #stemming: Stemming is the process of reducing a word to its word stem that affixes to suffixes
     nltk_stemedList = []
     for word in nltk_tokenList:
        nltk_stemedList.append(p_stemmer.stem(word))
     #Lemmatization: iguring out the most basic form or lemma of each word in the sentence
     wordnet_lemmatizer = WordNetLemmatizer()
     nltk_lemmaList = []
     for word in nltk_stemedList:
         nltk_lemmaList.append(wordnet_lemmatizer.lemmatize(word))
     print("Stemming + Lemmatization")
     print(nltk_lemmaList)
     filtered_sentence = [] 
     nltk_stop_words = set(stopwords.words("english"))
     for w in nltk_lemmaList:  
        if w not in nltk_stop_words:  
            filtered_sentence.append(w)
     punctuations="?:!.,;"
     for word in filtered_sentence:
        if word in punctuations:
            filtered_sentence.remove(word)
     print(" ")
     print("Remove stopword & Punctuation")
     print(filtered_sentence)
     print(" ")
     
Example_Sentence="This program displays three statistics for each text: average word length, average sentence length, and the number of times each vocabulary item appears in the text on average"
nltk_process(Example_Sentence)