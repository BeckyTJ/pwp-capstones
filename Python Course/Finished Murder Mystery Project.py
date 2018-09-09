
# coding: utf-8

# # Preamble: A Brand new Jay
# 
# After an eventful season on season 8 of *A Brand New Jay*, the 3 remaining contestants were invited to Jay Stacksby's private island for the last three episodes. When the day of filming the finale came Mr. Stacksby was found with one of his Professional Series 8-inch Chef Knives plunged through his heart! After the initial investigation highlighted that the film crew all lived in a separate house on the other side of the island, it was concluded that only the three contestants were near enough to Stacksby in order to commit a crime. At the scene of the crime, a letter was left. Here are the contents of that letter:
# 
# > You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him.
# 
# Pretty sinister stuff! Luckily, in addition to this bold-faced admission, we have the introduction letters of the three contestants. Maybe there is a way to use this information to determine who the author of this murder letter is?
# 
# Myrtle Beech's introduction letter:
# > Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a "walk". A "walk" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition. 
# 
# Lily Trebuchet's introduction letter:
# > Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show! 
# 
# Gregg T Fishy's introduction letter:
# 
# > A most good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young, an adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might find yourself asking? Why, I happen to always be fishing for compliments of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television, I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life, every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay To Remember, it certainly seems like a grand time to explore life and love.

# ## Saving The Different Examples as Variables
# 
# First let's create variables to hold the text data in! Save the muder note as a string in a variable called `murder_note`. Save Lily Trebuchet's introduction into `lily_trebuchet_intro`. Save Myrtle Beech's introduction into `myrtle_beech_intro`. Save Gregg T Fishy's introduction into `gregg_t_fishy_intro`.

# In[9]:


murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
gregg_t_fishy_intro = "A most good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young, an adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might find yourself asking? Why, I happen to always be fishing for compliments of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television, I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life, every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay To Remember, it certainly seems like a grand time to explore life and love."


# ## The First Indicator: Sentence Length
# 
# Perhaps some meaningful data can first be gleaned from these text examples if we measure how long the average sentence length is. Different authors have different patterns of written speech, so this could be very useful in tracking down the killer.
# 
# Write a function `get_average_sentence_length` that takes some `text` as an argument. This function should return the average length of a sentence in the text.
# 
# Hint (highlight this hint in order to reveal it): 
# <font color="white">Use your knowledge of _string methods_ to create a list of all of the sentences in a text, called **sentences_in_text**. 
# Further break up each **sentences_in_text** into a list of words and save the _length_ of that list of words to a new list that contains all the sentence lengths, called **sentence_lengths**. Take the average of all of the sentence lengths by adding them all together and dividing by the number of sentences (which should be the same as the length of the **sentence_lengths**).
# 
# Remember sentences can end with more than one kind of punctuation, you might find it easiest to use **.replace()** so you only have to split on one punctuation mark. Remember **.replace()** doesn't modify the string itself, it returns a new string!</font>

# In[19]:


def get_average_sentence_length(text):
    punctuation = ".!?"
    length = 0
    number_of_sentences = 0
    for letter in text:
        length +=1
        if letter in punctuation:
            number_of_sentences += 1
    return length / number_of_sentences
print("The average length of sentences in the murder note is " + str(get_average_sentence_length(murder_note)))
print("The average length of sentences in the Lily Intro is " + str(get_average_sentence_length(lily_trebuchet_intro)))
print("The average length of sentences in the Myrtle Intro is " + str(get_average_sentence_length(myrtle_beech_intro)))
print("The average length of sentences in the Gregg Intro is " + str(get_average_sentence_length(gregg_t_fishy_intro)))


# ## Creating The Definition for Our Model
# 
# Now that we have a metric we want to save and data that is coupled with that metric, it might be time to create our data type. Let's define a class called `TextSample` with a constructor. The constructor should take two arguments: `text` and `author`. `text` should be saved as `self.raw_text`. Call `get_average_sentence_length` with the raw text and save it to `self.average_sentence_length`. You should save the author of the text as `self.author`.
# 
# Additionally, define a string representation for the model. If you print a `TextSample` it should render:
#  - The author's name
#  - The average sentence length
#  
# This will be your main class for the problem at hand. All later instruction to update `TextSample` should be done in the code block below. After updating `TextSample`, click on the `Cell` option in the Jupyter Notebook main menu above, then click `Run All` to rerun the cells from top to bottom. If you need to restart your Jupyter Notebook either run the cells below first or move the `TextSample` class definition & instantiation cells to the bottom.

# In[192]:


class TextSample:
    def __init__(self, text, author):
        self.raw_text = text
        self.author = author
        self.average_sentence_length = get_average_sentence_length(text)
        self.prepared_text = prepare_text(text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram = ngram_creator(self.prepared_text)
        self.ngram_frequency = build_frequency_table(self.ngram)
    def print_author(self):
        print(self.author + " " + str(self.average_sentence_length))
    def print_prepared_text(self):
        print(self.prepared_text)
    def frequency_table(self):
        self.word_count_frequency
    def print_ngram_frequency(self):
        print(self.ngram_frequency)

murderer_sample = TextSample(murder_note, "Murderer")
lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T Fishy")


# ### Creating our TextSample Instances
# 
# Now create a `TextSample` object for each of the samples of text that we have.
#  - `murderer_sample` for the murderer's note.
#  - `lily_sample` for Lily Trebuchet's note.
#  - `myrtle_sample` for Myrtle Beech's note.
#  - `gregg_sample` for Gregg T Fishy's note.
#  
# Print out each one after instantiating them.

# In[161]:


murderer_sample.print_author()
lily_sample.print_author()
myrtle_sample.print_author()
gregg_sample.print_author()
murderer_sample.print_frequency_table()
murderer_sample.print_ngram_frequency()


# ## Cleaning Our Data
# 
# We want to compare the word choice and usage between the samples, but sentences make our text data fairly messy. In order to analyze the different messages fairly, we'll need to remove all the punctuation and uppercase letters from the samples.
# 
# Create a function called `prepare_text` that takes a single parameter `text`, makes the text entirely lowercase, removes all the punctuation and returns a list of the words in the text in order.
# 
# For example: `"Where did you go, friend? We nearly saw each other."` would become `['where', 'did', 'you', 'go', 'friend', 'we', 'nearly', 'saw', 'each', 'other']`.

# In[145]:


def prepare_text(text):
    split_text = []
    for words in text.lower().split():
        split_text.append(words.strip().strip(",").strip(".").strip("!").strip("?"))     
    return split_text       


# Update the constructor for `TextSample` to save the prepared text as `self.prepared_text`.

# ## Building A Frequency Table
# 
# Now we want to see which words were most frequently used in each of the samples. Create a function called `build_frequency_table`. It takes in a list called `corpus` and creates a dictionary called `frequency_table`. For every element in `corpus` the value `frequency_table[element]` should be equal to the number of times that element appears in `corpus`. For example the input `['do', 'you', 'see', 'what', 'i', 'see']` would create the frequency table `{'what': 1, 'you': 1, 'see' 2, 'i': 1}`.

# In[205]:


def build_frequency_table(corpus):
    frequency_table = {}
    for words in corpus:
        frequency_table[words] = corpus.count(words)
    return frequency_table

print(gregg_sample.word_count_frequency)


# ## The Second Indicator: Favorite Words
# 
# Use `build_frequency_table` with the prepared text to create a frequency table that counts how frequently all the words in each text sample appears. Call these functions in the constructor for `TextSample` and assign the word frequency table to a value called `self.word_count_frequency`.

# ## The Third Indicator: N-Grams
# 
# An <a href='https://en.wikipedia.org/wiki/N-gram' target="_blank">n-gram</a> is a text analysis technique used for pattern recognition and applicable throughout lingusitics. We're going to use n-grams to find who uses similar word-pairs to the murderer, and we think it's going to make our evidence strong enough to conclusively find the killer.
# 
# Create a function called `ngram_creator` that takes a parameter `text_list`, a treated in-order list of the words in a text sample. `ngram_creator` should return a list of all adjacent pairs of words, styled as strings with a space in the center.
# 
# For instance, calling `ngram_creator` with the input `['what', 'in', 'the', 'world', 'is', 'going', 'on']`
# Should produce the output `['what in', 'in the', 'the world', 'world is', 'is going', 'going on']`.
# 
# These are two-word n-grams.

# In[210]:


def ngram_creator(text_list):
    ngram = []
    for words in range(len(text_list) - 1):
        first_word = text_list[words]
        second_word = text_list[words + 1]
        both_words = (first_word + " " + second_word)
        ngram.append(both_words)
    return ngram   


# Use `ngram_creator` along with the prepared text to create a list of all the two-word ngrams in each `TextSample`. Use `build_frequency_table` to tabulate the frequency of each ngram. In the constructor for `TextSample` save this frequency table as `self.ngram_frequency`.

# ## Comparing Two Frequency Tables
# 
# We want to know how similar two frequency tables are, let's write a function that computes the comparison between two frequency tables and scores them based on similarity.
# 
# Write a function called `frequency_comparison` that takes two parameters, `table1` and `table2`. It should define two local variables, `appearances` and `mutual_appearances`. 
# 
# Iterate through `table1`'s keys and check if `table2` has the same key defined. If it is, compare the two values for the key -- the smaller value should get added to `mutual_appearances` and the larger should get added to `appearances`. If the key doesn't exist in `table2` the value for the key in `table1` should be added to `appearances`.
# 
# Remember afterwards to iterate through all of `table2`'s keys that aren't in `table1` and add those to `appearances` as well.
# 
# Return a frequency comparison score equal to the mutual appearances divided by the total appearances.

# In[206]:


def frequency_comparison(table1, table2):
    appearances = 0
    mutual_appearances = 0
    for keys in table1.keys():
        if keys in table2.keys():
            if table1[keys] >= table2[keys]:
                appearances += table1[keys]
                mutual_appearances += table2[keys]
            elif table2[keys] > table1[keys]:
                appearances += table2[keys]
                mutual_appearances += table1[keys]
        elif not keys in table2.keys():
            appearances += table1[keys]
    for keys in table2.keys():
        if not keys in table1.keys():
            appearances += table2[keys]
    return mutual_appearances / appearances

print(frequency_comparison({'you': 6, 'may': 1, 'call': 1, 'me': 1, 'heartless': 1, 'a': 11, 'killer': 1, 'monster': 1, 'murderer': 1, 'but': 2, "i'm": 1, 'still': 1, 'nothing': 1, 'compared': 1, 'to': 10, 'the': 12, 'villian': 1, 'that': 7, 'jay': 2, 'was': 10, 'this': 2, 'whole': 1, 'contest': 2, 'sham': 1, 'an': 1, 'elaborate': 1, 'plot': 1, 'shame': 1, 'contestants': 1, 'and': 9, 'feed': 1, "jay's": 1, 'massive': 2, 'ego': 1, 'sure': 1, 'think': 1, 'know': 3, 'him': 8, "you've": 1, 'seen': 1, 'smiling': 1, 'for': 2, 'cameras': 1, 'laughing': 1, 'joking': 1, 'telling': 1, 'stories': 1, 'waving': 1, 'his': 5, 'money': 1, 'around': 2, 'like': 5, 'prop': 1, 'off': 1, 'camera': 1, 'he': 13, 'sinister': 1, 'beast': 1, 'cruel': 2, 'taskmaster': 1, 'treated': 1, 'all': 9, 'of': 8, 'us': 5, 'slaves': 1, 'cattle': 1, 'animals': 1, 'do': 1, 'remember': 1, 'lindsay': 1, 'she': 2, 'first': 1, 'go': 2, 'called': 1, 'her': 2, 'such': 1, 'horrible': 1, 'things': 3, 'cried': 1, 'night': 2, 'keeping': 1, 'up': 2, 'crying': 3, 'more': 1, 'broke': 1, 'with': 3, 'words': 1, 'i': 7, 'miss': 1, 'my': 1, 'former': 1, 'cast': 1, 'members': 1, 'them': 1, 'very': 1, 'much': 1, 'we': 2, 'had': 1, 'live': 3, 'in': 3, 'home': 1, 'power': 1, 'deal': 1, 'crazy': 1, 'demands': 1, 'what': 3, 'did': 1, 'prize': 1, "isn't": 1, 'real': 1, 'never': 2, 'intended': 1, 'marry': 1, 'one': 1, 'carrot': 1, 'on': 2, 'stick': 2, 'gone': 1, 'left': 1, 'told': 1, 'last': 1, 'were': 1, 'terrible': 2, 'disappointment': 1, 'none': 1, 'would': 2, 'ever': 1, 'amount': 1, 'anything': 1, 'regardless': 1, 'who': 2, 'won': 1, 'speak': 1, 'any': 2, 'again': 1, "it's": 1, 'definitely': 1, 'can': 1, 'feel': 1, 'your': 1, 'gut': 1, 'how': 1, 'wrong': 1, 'is': 3, 'well': 1, 'showed': 3, 'got': 2, 'deserved': 2, 'right': 1, 'person': 1, 'am': 1, "wasn't": 2, 'going': 2, 'be': 1, 'pushed': 1, 'longer': 1, 'let': 1, 'pretending': 1, 'some': 1, 'saint': 1, 'when': 1, 'sick': 2, 'twisted': 1, 'man': 1, 'every': 1, 'bit': 1, 'fans': 1, 'need': 1, 'stacksby': 1, 'vile': 1, 'amalgamation': 1, 'evil': 1, 'bad': 1, 'world': 1, 'better': 1, 'place': 1, 'without': 1}, {'hi': 1, "i'm": 1, 'lily': 1, 'trebuchet': 1, 'from': 1, 'east': 1, 'egg': 1, 'long': 1, 'island': 1, 'i': 11, 'love': 2, 'cats': 1, 'hiking': 1, 'and': 10, 'curling': 1, 'up': 1, 'under': 1, 'a': 6, 'warm': 1, 'blanket': 1, 'with': 5, 'book': 1, 'so': 2, 'they': 2, 'gave': 1, 'this': 1, 'little': 1, 'questionnaire': 1, 'to': 8, 'use': 1, 'for': 4, 'our': 1, 'bios': 1, 'lets': 1, 'get': 1, 'started': 1, 'what': 4, 'are': 2, 'some': 1, 'of': 7, 'my': 5, 'least': 1, 'favorite': 3, 'household': 1, 'chores': 1, 'dishes': 2, 'oh': 1, 'yes': 1, "it's": 1, 'definitely': 2, 'the': 10, 'just': 1, 'hate': 1, 'doing': 1, 'them': 2, "don't": 1, 'you': 9, 'who': 1, 'is': 9, 'your': 4, 'actor': 1, 'why': 1, 'hmm': 1, "that's": 2, 'hard': 2, 'one': 4, 'but': 4, 'think': 4, 'recently': 1, "i'll": 2, 'have': 3, 'go': 2, 'michael': 1, 'b': 1, 'jordan': 1, 'every': 1, 'bit': 1, 'that': 1, 'man': 2, 'handsome': 3, 'do': 2, 'remember': 1, 'seeing': 1, 'him': 2, 'shirtless': 1, "can't": 1, 'believe': 1, 'he': 3, 'does': 1, 'cameras': 1, 'okay': 4, 'next': 1, 'question': 2, 'perfect': 1, 'date': 1, 'well': 2, 'it': 4, 'starts': 1, 'nice': 1, 'dinner': 1, 'at': 1, 'delicious': 1, 'small': 1, 'restaurant': 1, 'know': 2, 'like': 1, 'those': 1, 'places': 1, 'where': 1, 'owner': 1, 'in': 3, 'back': 1, 'comes': 1, 'out': 1, 'talk': 1, 'ask': 1, 'how': 1, 'meal': 1, 'was': 1, 'form': 1, 'art': 1, 'another': 1, 'music': 2, 'can': 2, 'feel': 1, 'whole': 1, 'body': 1, 'electrifying': 1, 'best': 1, 'all': 3, 'dance': 1, 'final': 1, "let's": 1, 'see': 1, 'three': 1, 'things': 1, 'cannot': 1, 'live': 1, 'without': 1, 'first': 2, 'off': 1, 'beautiful': 2, 'cat': 1, 'jerry': 1, 'heart': 1, 'spirit': 1, 'animal': 1, 'second': 1, 'pasta': 2, 'third': 1, 'family': 1, 'very': 1, 'much': 1, 'support': 1, 'me': 2, 'everything': 1, 'jay': 1, 'stacksby': 1, 'us': 1, 'want': 1, 'be': 2, 'walk': 1, 'down': 1, 'aisle': 1, 'might': 1, 'truly': 1, 'bio': 1, 'hope': 1, 'fun': 1, 'watching': 1, 'show': 1}))
print(frequency_comparison({'you': 6, 'may': 1, 'call': 1, 'me': 1, 'heartless': 1, 'a': 11, 'killer': 1, 'monster': 1, 'murderer': 1, 'but': 2, "i'm": 1, 'still': 1, 'nothing': 1, 'compared': 1, 'to': 10, 'the': 12, 'villian': 1, 'that': 7, 'jay': 2, 'was': 10, 'this': 2, 'whole': 1, 'contest': 2, 'sham': 1, 'an': 1, 'elaborate': 1, 'plot': 1, 'shame': 1, 'contestants': 1, 'and': 9, 'feed': 1, "jay's": 1, 'massive': 2, 'ego': 1, 'sure': 1, 'think': 1, 'know': 3, 'him': 8, "you've": 1, 'seen': 1, 'smiling': 1, 'for': 2, 'cameras': 1, 'laughing': 1, 'joking': 1, 'telling': 1, 'stories': 1, 'waving': 1, 'his': 5, 'money': 1, 'around': 2, 'like': 5, 'prop': 1, 'off': 1, 'camera': 1, 'he': 13, 'sinister': 1, 'beast': 1, 'cruel': 2, 'taskmaster': 1, 'treated': 1, 'all': 9, 'of': 8, 'us': 5, 'slaves': 1, 'cattle': 1, 'animals': 1, 'do': 1, 'remember': 1, 'lindsay': 1, 'she': 2, 'first': 1, 'go': 2, 'called': 1, 'her': 2, 'such': 1, 'horrible': 1, 'things': 3, 'cried': 1, 'night': 2, 'keeping': 1, 'up': 2, 'crying': 3, 'more': 1, 'broke': 1, 'with': 3, 'words': 1, 'i': 7, 'miss': 1, 'my': 1, 'former': 1, 'cast': 1, 'members': 1, 'them': 1, 'very': 1, 'much': 1, 'we': 2, 'had': 1, 'live': 3, 'in': 3, 'home': 1, 'power': 1, 'deal': 1, 'crazy': 1, 'demands': 1, 'what': 3, 'did': 1, 'prize': 1, "isn't": 1, 'real': 1, 'never': 2, 'intended': 1, 'marry': 1, 'one': 1, 'carrot': 1, 'on': 2, 'stick': 2, 'gone': 1, 'left': 1, 'told': 1, 'last': 1, 'were': 1, 'terrible': 2, 'disappointment': 1, 'none': 1, 'would': 2, 'ever': 1, 'amount': 1, 'anything': 1, 'regardless': 1, 'who': 2, 'won': 1, 'speak': 1, 'any': 2, 'again': 1, "it's": 1, 'definitely': 1, 'can': 1, 'feel': 1, 'your': 1, 'gut': 1, 'how': 1, 'wrong': 1, 'is': 3, 'well': 1, 'showed': 3, 'got': 2, 'deserved': 2, 'right': 1, 'person': 1, 'am': 1, "wasn't": 2, 'going': 2, 'be': 1, 'pushed': 1, 'longer': 1, 'let': 1, 'pretending': 1, 'some': 1, 'saint': 1, 'when': 1, 'sick': 2, 'twisted': 1, 'man': 1, 'every': 1, 'bit': 1, 'fans': 1, 'need': 1, 'stacksby': 1, 'vile': 1, 'amalgamation': 1, 'evil': 1, 'bad': 1, 'world': 1, 'better': 1, 'place': 1, 'without': 1}, {'salutations': 1, 'my': 3, 'name': 1, 'myrtle': 2, 'beech': 1, 'i': 16, 'am': 2, 'a': 10, 'woman': 1, 'of': 3, 'simple': 1, 'tastes': 1, 'enjoy': 1, 'reading': 1, 'thinking': 1, 'and': 2, 'doing': 1, 'taxes': 1, 'entered': 1, 'this': 2, 'competition': 2, 'because': 1, 'want': 2, 'serious': 1, 'relationship': 1, 'commitment': 1, 'the': 6, 'last': 1, 'man': 1, 'dated': 1, 'was': 1, 'too': 1, 'whimsical': 1, 'he': 2, 'wanted': 1, 'to': 5, 'go': 1, 'on': 1, 'dates': 1, 'that': 3, 'had': 1, 'no': 3, 'plan': 1, 'end': 3, 'goal': 1, 'sometimes': 1, 'we': 1, 'would': 1, 'just': 1, 'up': 1, 'wandering': 1, 'streets': 1, 'after': 1, 'dinner': 1, 'called': 1, 'it': 2, '"walk"': 2, 'with': 2, 'destination': 2, 'can': 1, 'you': 2, 'imagine': 1, 'like': 2, 'every': 1, 'action': 1, 'take': 2, 'have': 2, 'measurable': 1, 'effect': 1, 'when': 2, 'see': 1, 'movie': 1, 'walk': 1, 'away': 1, 'insights': 1, 'did': 1, 'not': 2, 'before': 1, 'bike': 2, 'ride': 1, 'there': 1, 'better': 1, 'be': 1, 'worthy': 1, 'at': 2, 'path': 1, 'jay': 1, 'seems': 1, 'frivolous': 1, 'times': 1, 'worries': 1, 'me': 1, 'however': 1, 'is': 1, 'staunch': 1, 'belief': 1, 'one': 1, 'does': 1, 'make': 1, 'keep': 1, 'money': 1, 'without': 2, 'having': 1, 'modicum': 1, 'discipline': 1, 'as': 1, 'such': 1, 'hopeful': 1, 'will': 1, 'now': 1, 'list': 1, 'three': 1, 'things': 1, 'cannot': 1, 'live': 1, 'water': 1, 'emery': 1, 'boards': 1, 'dogs': 1, 'thank': 1, 'for': 1, 'opportunity': 1, 'introduce': 1, 'myself': 1, 'look': 1, 'forward': 1}))
print(frequency_comparison({'you': 6, 'may': 1, 'call': 1, 'me': 1, 'heartless': 1, 'a': 11, 'killer': 1, 'monster': 1, 'murderer': 1, 'but': 2, "i'm": 1, 'still': 1, 'nothing': 1, 'compared': 1, 'to': 10, 'the': 12, 'villian': 1, 'that': 7, 'jay': 2, 'was': 10, 'this': 2, 'whole': 1, 'contest': 2, 'sham': 1, 'an': 1, 'elaborate': 1, 'plot': 1, 'shame': 1, 'contestants': 1, 'and': 9, 'feed': 1, "jay's": 1, 'massive': 2, 'ego': 1, 'sure': 1, 'think': 1, 'know': 3, 'him': 8, "you've": 1, 'seen': 1, 'smiling': 1, 'for': 2, 'cameras': 1, 'laughing': 1, 'joking': 1, 'telling': 1, 'stories': 1, 'waving': 1, 'his': 5, 'money': 1, 'around': 2, 'like': 5, 'prop': 1, 'off': 1, 'camera': 1, 'he': 13, 'sinister': 1, 'beast': 1, 'cruel': 2, 'taskmaster': 1, 'treated': 1, 'all': 9, 'of': 8, 'us': 5, 'slaves': 1, 'cattle': 1, 'animals': 1, 'do': 1, 'remember': 1, 'lindsay': 1, 'she': 2, 'first': 1, 'go': 2, 'called': 1, 'her': 2, 'such': 1, 'horrible': 1, 'things': 3, 'cried': 1, 'night': 2, 'keeping': 1, 'up': 2, 'crying': 3, 'more': 1, 'broke': 1, 'with': 3, 'words': 1, 'i': 7, 'miss': 1, 'my': 1, 'former': 1, 'cast': 1, 'members': 1, 'them': 1, 'very': 1, 'much': 1, 'we': 2, 'had': 1, 'live': 3, 'in': 3, 'home': 1, 'power': 1, 'deal': 1, 'crazy': 1, 'demands': 1, 'what': 3, 'did': 1, 'prize': 1, "isn't": 1, 'real': 1, 'never': 2, 'intended': 1, 'marry': 1, 'one': 1, 'carrot': 1, 'on': 2, 'stick': 2, 'gone': 1, 'left': 1, 'told': 1, 'last': 1, 'were': 1, 'terrible': 2, 'disappointment': 1, 'none': 1, 'would': 2, 'ever': 1, 'amount': 1, 'anything': 1, 'regardless': 1, 'who': 2, 'won': 1, 'speak': 1, 'any': 2, 'again': 1, "it's": 1, 'definitely': 1, 'can': 1, 'feel': 1, 'your': 1, 'gut': 1, 'how': 1, 'wrong': 1, 'is': 3, 'well': 1, 'showed': 3, 'got': 2, 'deserved': 2, 'right': 1, 'person': 1, 'am': 1, "wasn't": 2, 'going': 2, 'be': 1, 'pushed': 1, 'longer': 1, 'let': 1, 'pretending': 1, 'some': 1, 'saint': 1, 'when': 1, 'sick': 2, 'twisted': 1, 'man': 1, 'every': 1, 'bit': 1, 'fans': 1, 'need': 1, 'stacksby': 1, 'vile': 1, 'amalgamation': 1, 'evil': 1, 'bad': 1, 'world': 1, 'better': 1, 'place': 1, 'without': 1}, {'a': 4, 'most': 3, 'good': 1, 'day': 2, 'to': 6, 'you': 2, 'all': 1, 'i': 11, 'am': 2, 'gregg': 1, 't': 1, 'fishy': 2, 'of': 9, 'the': 8, 'enterprise': 1, 'fortune': 1, '37': 1, 'years': 1, 'young': 1, 'an': 1, 'adventurous': 1, 'spirit': 1, 'and': 8, "i've": 1, 'never': 1, 'lost': 1, 'my': 6, 'sense': 1, 'childlike': 1, 'wonder': 1, 'do': 1, 'love': 2, 'be': 3, 'in': 3, 'backyard': 1, 'gardening': 1, 'have': 2, 'extraordinary': 1, 'time': 2, 'when': 2, "i'm": 2, 'fishing': 3, 'for': 2, 'what': 1, 'might': 1, 'find': 2, 'yourself': 1, 'asking': 1, 'why': 1, 'happen': 1, 'always': 1, 'compliments': 1, 'course': 1, 'stunning': 1, 'pair': 1, 'radiant': 1, 'blue': 1, 'eyes': 1, 'that': 5, 'will': 2, 'pierce': 1, 'soul': 1, 'anyone': 1, 'who': 1, 'dare': 1, 'gaze': 1, 'upon': 1, 'countenance': 1, 'quite': 2, 'enjoy': 3, 'going': 1, 'on': 3, 'long': 1, 'jaunts': 1, 'through': 2, 'garden': 1, 'paths': 1, 'short': 1, 'walks': 1, 'greenhouses': 1, 'hope': 1, 'jay': 2, 'as': 2, 'absolutely': 1, 'interesting': 1, 'he': 2, 'appears': 1, 'television': 2, 'has': 1, 'some': 1, 'curious': 1, 'tastes': 1, 'style': 1, 'humor': 1, 'out': 1, 'about': 1, 'hearing': 1, 'tales': 1, 'instill': 1, 'heart': 1, 'hearts': 1, 'fascination': 1, 'beguiles': 1, 'every': 2, 'life': 2, 'fiber': 1, 'being': 2, 'scintillates': 1, 'vascillates': 1, 'with': 1, 'extreme': 1, 'pleasure': 1, 'during': 1, 'one': 1, 'these': 1, 'charming': 1, 'anecdotes': 1, 'significantly': 1, 'pleases': 1, 'beautiful': 1, 'personage': 1, 'cannot': 1, 'wait': 1, 'program': 1, 'remember': 1, 'it': 1, 'certainly': 1, 'seems': 1, 'like': 1, 'grand': 1, 'explore': 1}))


# ## Comparing Average Sentence Length
# 
# In order to calculate the change between the average sentence lengths of two `TextSamples` we're going to use the formula for the percent difference.
# 
# Write a function called `percent_difference` that returns the percent difference as calculated from the following formula:
# 
# $$\frac{|\ value1 - value2\ |}{\frac{value1 + value2}{2}}$$
# 
# In the numerator is the absolute value (use `abs()`) of the two values subtracted from each other. In the denominator is the average of the two values (value1 + value2 divided by two).

# In[177]:


def percent_difference(value1, value2):
    difference = (abs(value1 - value2) / ((value1 + value2) / 2))
    return difference


# ## Scoring Similarity with All Three Indicators
# 
# We want to figure out who did it, so let's use all three of the indicators we built to score text similarity. Define a function `find_text_similarity` that takes two `TextSample` arguments and returns a float between 0 and 1 where 0 means completely different and 1 means the same exact sample. You can evaluate the similarity by the following criteria:
# 
# - Calculate the percent difference of their average sentence length using `percent_difference`. Save that into a variable called `sentence_length_difference`. Since we want to find how _similar_ the two passages are calculate the inverse of `sentence_length_difference` by using the formula `abs(1 - sentence_length_difference)`. Save that into a variable called `sentence_length_similarity`.
# - Calculate the difference between their word usage using `frequency_comparison` on both `TextSample`'s `word_count_frequency` attributes. Save that into a variable called `word_count_similarity`.
# - Calculate the difference between their two-word ngram using `frequency_table` on both `TextSample`'s `ngram_frequency` attributes. Save that into a variable called `ngram_similarity`.
# - Add all three similarities together and divide by 3.

# In[182]:


def find_text_similarity(TextSample1, TextSample2):
    length1 = get_average_sentence_length(TextSample1)
    length2 = get_average_sentence_length(TextSample2)
    sentence_length_difference = percent_difference(length1, length2)
    sentence_length_similarity = abs(1 - sentence_length_difference)
    frequency1 = build_frequency_table(TextSample1)
    frequency2 = build_frequency_table(TextSample2)
    word_count_similarity = frequency_comparison(frequency1, frequency2)
    preparedtext1 = prepare_text(TextSample1)
    preparedtext2 = prepare_text(TextSample2)
    ngram1 = ngram_creator(preparedtext1)
    ngram2 = ngram_creator(preparedtext2)
    ngramfrequency1 = build_frequency_table(ngram1)
    ngramfrequency2 = build_frequency_table(ngram2)
    ngram_similarity = frequency_comparison(ngramfrequency1, ngramfrequency2)
    overall_similarity = (sentence_length_similarity + word_count_similarity + ngram_similarity) / 3
    return overall_similarity


# ## Rendering the Results
# 
# We want to print out the results in a way that we can read! For each contestant on _A Brand New Jay_ print out the following:
# 
# - Their name
# - Their similarity score to the murder letter

# In[208]:


print("Lily Trebuchet " + str(find_text_similarity(murder_note, lily_trebuchet_intro)))
print("Myrtle Beech " + str(find_text_similarity(murder_note, myrtle_beech_intro)))
print("Gregg T Fishy " + str(find_text_similarity(murder_note, gregg_t_fishy_intro)))


# # Who Dunnit?
# 
# In the cell below, print the name of the person who killed Jay Stacksby.

# In[209]:


print("Gregg T Fishy is the murderer.")

