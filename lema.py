def lem(Sep_words):
	from nltk.stem import WordNetLemmatizer 
	words=[] 
	lemmatizer = WordNetLemmatizer() 
	for word in Sep_words:
    		words.append(lemmatizer.lemmatize(word))

	return words
