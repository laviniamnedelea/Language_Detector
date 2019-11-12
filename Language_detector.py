from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize

def lang_det(text):
    languages_freq = {}
    tokens = wordpunct_tokenize(text)
    langg  = stopwords.fileids()
    mywords = [myword.lower() for myword in tokens]
    for language in langg:
        stopwords_set = set(stopwords.words(language))
        mywords_set = set(mywords)
        common_elements = mywords_set.intersection(stopwords_set)
        languages_freq[language] = len (common_elements)

    return languages_freq

max = 0

mylang = lang_det(input("Text:"))
for i,k in mylang.items():
    if k>max:
        max=k
        key = i

#aici mergea si o sortare dupa cea mai mare valoare, era mult mai profi asa
#plus ar fi fost mai ok cu clase 
print("LANGUAGE:", key)




