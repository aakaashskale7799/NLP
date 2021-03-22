text_hindi = "देश में मार्च के महीने में कोरोना विस्फोट का दूसरा दौर रफ्तार पकड़ रहा है. कई राज्यों में हालात चिंताजनक है. ऐसे में दिल्ली सरकार भी अलर्ट मोड पर आ गई"
from nltk.tag import tnt
from nltk.corpus import indian
import nltk
train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tagged_words = (tnt_pos_tagger.tag(nltk.word_tokenize(text_hindi)))
print(tagged_words)
text_marathi = "महाराष्ट्राचे मुख्यमंत्री हेच सचिन वाझे यांचे गॉडफादर असल्याचं सांगत त्यांनीच सचिन वाझे यांना खंडणी वसूल करण्याची परवानगी दिली असल्याचा आरोप भाजप नेते नारायण राणे यांनी केला आहे."
print(" ")
train_data = indian.tagged_sents('marathi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tagged_words = (tnt_pos_tagger.tag(nltk.word_tokenize(text_marathi)))
print(tagged_words)