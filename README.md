# Wordadora - Vocabulary Builder 
#### *~The next-door Vocabulary Teacher*
Read some books, articles, or blogs, and came across some new words? Wanna know what they meant? Wordadora comes to your rescue.

#### Wordadora is your next-door Vocabulary Teacher, built into codes, made with love, just for you! With it offering a range of smart features, the main word base upon which it functions on can be modified as per the user choice.

### Module 1 - Form
Wordadora houses the capability to scrape off words, as per the user choice, from a set of given website URLs, which ultimately owes to the development of the primary word-base, upon which the different fangs of the app works on. The scrapped words results through a series of different steps/ operations, with finally getting stored into a CSV file against their score values into the app directory. This in a way aids it's way to becoming and functioning as a Database Independent routine.

As of now, the scoring systems exploited towards levelling of the words, correspond to the using the readibilty index scorings, offered in the 'textstat' module. The users have an option to choose from the metrics of flesch reading ease and automated readability index, after which the words appear in different hardness levels. Also available in the house is the Flesch-Kincaid method which have not made it's way into the scoring calculation yet. Considerations of adding a feature involving human interference towards effective calculation of word scores have already been made into the context, and am working on it.


Spacy module has been used to detect the regular expressions and parts of speech from the unstructured scraped text, which then makes into the score calculation module. Several techniques such as Lemmatization are applied onto the unstructured text before they are fed into the other modules.

### Module 2 - Execute 
<p align="center">
  <img alt="GIF1" src="https://github.com/ddebrup/Wordadora/blob/main/Images/Learn01.gif" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="GIF2" src="https://github.com/ddebrup/Wordadora/blob/main/Images/Learn02.gif" width="45%">
</p>
Upon executing this module a GUI will pop up with corresponding instructions. Users can choose to Learn or Practice as per their necessity. The details of both the modes of operations are as follows </br>


~ **LEARN** - *This mode offers to it's users the ability to learn new words, depending on the chosen difficulty level. When selected, the users get to choose from a particular set the interval values, after which every new word gets popped up with their meanings and usage in a notification format.* </br>
~ **PRACTICE** - *This mode lets it's users take an assessment test, wherein the definition of a random words gets displayed along with a few number of options containing different words to choose from. On selecting the right option containing the right word, the user gets to move to the next question, on the contrary, when selected an incorrect answer the right word with it's definition gets popped into the screen. Since the main aim of this project is to build an individual's vocabulary and not just test it.* </br>
<p align="center">
  <img width="460" height="300" src="https://github.com/ddebrup/Wordadora/blob/main/Images/Practice.gif">
</p> </br>
~ AUTO - I am currently working on this mode, upon the completion of which, there will be a smart engine which will automatically schedule the learn and practice modes depending on the outcome of a short quiz, which should be take at first. The engine will have capabilities to control the number and level of questions being asked in the pre-quizzing session.

### Steps of Operation











