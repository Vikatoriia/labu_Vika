# TODO
# 'love', 'like' are also noun


#Viktoriia Palianytsia
#Chapter 5, Task 21

import nltk
from nltk.corpus import brown
fd = nltk.FreqDist()
text=nltk.corpus.brown.words(categories='adventure')
dic=['']
for (wd, tg) in nltk.corpus.brown.tagged_words():
            if tg[:2] == 'QL':
                fd.inc(wd)
                verbs=['adore', 'love', 'like', 'prefer']
                nouns=['love', 'like']
                for i in range(len(text)):
                    if text[i]in fd.keys()and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
                        dic.append(text[i]+' '+text[i+1])
                        print dic

#� ��������� ��������� �������� �� �������� ��� �������������,
#�� ��������� ������������ ����� ������� adore, love, like �� prefer.
#�a��� ����� ������� ��������, �� �� ����� ����� ������ ����������������
#�� ���� �� 䳺�����, ������� �� ���������, � � �� ��������, �� ����, ��������� ����������.
