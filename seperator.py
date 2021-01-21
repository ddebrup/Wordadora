def seperator(final_Words):
	import wordninja
	Sep_words=[]
	for word in final_Words:
    		for sep in wordninja.split(word):
        		Sep_words.append(sep)
	return Sep_words
