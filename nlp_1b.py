from indic_transliteration import sanscript 
from indic_transliteration.sanscript import transliterate 
# Input text "Today the weather is good. Sun is bright and there are no signs of rain. Hence we can play today."

text = input("Enter the sentence : ")
print('Sentence is : ',text)
  
print("transliterated text is  " ,transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI))


text = input("Enter the sentence : ")
print('Sentence is : ',text)  

print("transliterated text is  " ,transliterate(text, sanscript.ITRANS, sanscript.BENGALI))

text = input("Enter the sentence : ")
print('Sentence is : ',text)  

print("transliterated text is  " ,transliterate(text, sanscript.ITRANS, sanscript.GUJARATI)) 