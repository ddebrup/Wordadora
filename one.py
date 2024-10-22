import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import spacy
import nltk
import textstat
Newlines = re.compile(r'[\r\n]\s+')

def getPageText(url):
    # given a url, get page content
    data = urllib2.urlopen(url).read()
    # parse as html structured document
    bs = BeautifulSoup(data)
    # kill javascript content
    for s in bs.findAll('script'):
        s.replaceWith('')
    # find body and extract text
    txt = bs.find('body').getText('\n')
    # remove multiple linebreaks and whitespace
    return Newlines.sub('\n', txt)

def genwrd(txt):
    nlp = spacy.load('en_core_web_lg')


    #nlp = spacy.load('en_core_web_sm') #you can use other methods
    # excluded tags
    #excluded_tags = { "ADV", "ADP", "PROPN", "AUX", "CONJ", "DET", "NUM", "PART", "PRON", "PUNCT", "SCONJ", "SYM"}
    included_tags = {"ADJ", "INTJ", "NOUN", "VERB"}
    #document = [line.strip() for line in open(''.join(txt), encoding='utf8').readlines()]
    words=[]
    sent_text = nltk.sent_tokenize(''.join(txt).replace("\n","")) 
    document = sent_text 
    sentences = document[:10] #first 10 sentences
    #new_sentences = []
    for sentence in sentences:
        #new_sentence = []
        for token in nlp(sentence):
            if token.pos_ in included_tags:
                word=token.text
                if word not in words:
                    words.append(word)
                #new_sentence.append(token.text)
        #new_sentences.append(" ".join(new_sentence))
    return words

# Seperating individual words out
def seperate(words):
    final_Words=[]
    for word in words:
        if word.isalpha():
            final_Words.append(word)
    return final_Words

# Lemmatizing words 
def Lemmatiz(Sep_words):
    from nltk.stem import WordNetLemmatizer 
    words=[] 
    lemmatizer = WordNetLemmatizer() 
    for word in Sep_words:
        words.append(lemmatizer.lemmatize(word))
    return words


# Final Controller Module
def fin(words):
    word_list = []
    global wordle
    if 'wordle' not in globals():
        wordle = {}    
    #excepted = []
    #definition = []
    #example = []
    from nltk.corpus import wordnet 
    import textstat


    for word in words:
        syns = wordnet.synsets(word.lower())
        if not syns:
            continue
        else:
            #li=[]
            #word_list.append(word)
    #        #definition.append(syns[0].definition())
    #        #example.append(syns[0].examples()[0])
    #        li.append(syns[0].definition())
        
            #li.append(textstat.automated_readability_index(word.lower()))
	   # wordle[word]=textstat.flesch_reading_ease(word.lower())            
            wordle[word]=textstat.automated_readability_index(word.lower())
    
      
    jso()

def execute(words):
    words_sep=seperate(words)
    words=Lemmatiz(words_sep)
    fin(words)
    words=[]


        
    

    
def store():
    import csv
    with open('wordstest.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in wordle.items():
               writer.writerow([key, value])
                
def jso():
    import json
    
    json.dump(wordle, open("wordlist.txt",'w'))
 

    
def main():
    urls = [
        'http://www.stackoverflow.com/questions/5331266/python-easiest-way-to-scrape-text-from-list-of-urls-using-beautifulsoup',
        'http://stackoverflow.com/questions/5330248/how-to-rewrite-a-recursive-function-to-use-a-loop-instead',
        'https://www.geeksforgeeks.org/programming-language-choose/'
    ]
    txt = [getPageText(url) for url in urls]
    words=genwrd(txt)
    execute(words)
    
if __name__=="__main__": 
    main() 
