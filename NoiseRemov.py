import spacy
import nltk

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
