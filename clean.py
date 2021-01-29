#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import unicodedata
import nltk

class CleanText:

    def __init__(self):

        english_stopwords = nltk.corpus.stopwords.words('english')
        
        new_stop_words = ['year', 'new', 'includ', 'current', 'receiv', 'experience', 'work']
        english_stopwords.extend(new_stop_words)
        
        self.stopwords=english_stopwords
        

        self.stemmer = nltk.stem.SnowballStemmer('english')

    @staticmethod
    def convert_text_to_lower_case(txt):
        return txt.lower()
    
    @staticmethod
    def remove_non_letters(txt):
        return re.sub('[^a-z_]', ' ', txt)

    def remove_stopwords(self, txt):
        return [w for w in txt if (w not in self.stopwords)]

    def get_stem(self, txt):
        return [self.stemmer.stem(token) for token in txt.split()]
    
    def apply_cleaning (self,txt) :
        txt=self.convert_text_to_lower_case(txt)
        txt=self.remove_non_letters(txt) 
        tokens_stem=self.get_stem(txt) 
        tokens=self.remove_stopwords(tokens_stem)
        return tokens  

    def clean_df_column(self,df, column_name, clean_column_name):
        df[clean_column_name]=[" ".join(self.apply_cleaning(x)) for x in tqdm(df[column_name].values)]

