
# coding: utf-8

# In[24]:

with open('brown.txt','r') as f:
	corpus = f.read() 
	#print(corpus)


# In[25]:

words = corpus.split()        # split function converting whole corpus in to list of words so it will be eassy to handle
#print(words[:])


# In[26]:

N = len(words)
print(N)


# In[27]:

brown_test = []
brown_train = []
sen = 0
for i in words:
    if i == './.':
        sen += 1
    if sen < 2000:
        brown_test.append(i)
    else:
        brown_train.append(i)


# In[73]:

f= open("brown_test.txt","w+")
for i in brown_test:
     f.write("%s " %i)    
f.close() 

f= open("brown_train.txt","w+")
for i in brown_train:
     f.write("%s " %i)   
f.close() 


# In[29]:

print(len(brown_test))
print(len(brown_train))


# In[39]:

# getting frequency of tags from brown_train
import collections
types =  collections.Counter(brown_train)
#print(types)  # types is in the form of directories

# converting dictionary into two dimentional array "a"
a = []
for value in types.items() :
    a.append(value)
#print(a)

#sorting array "a" in decending order
def sortthird(a): 
    return a[1] 
a.sort(key = sortthird ,reverse = True) 
#print(a)

#spliting words and tags fron sorted array "a"
b = []
t = 0 
for i in a:
    x = a[t][0]
    j = x.rsplit('/')
    b.append(j)
    t += 1 
# len of b is 64413
    
#cosidering only maximum frequent word-tag pairs from array "b" 
temp =[]
max_fre_word_tag = []
for l in b:
    if (l[0] not in temp):
        temp.append(l[0])
        max_fre_word_tag.append(l)
    
print(max_fre_word_tag)  # now the size of training set come down to 54068 from 1111244 word_tags pairs


# In[31]:

# word_tags pair from brown_test corpus
# getting frequency of tags from brown_test
import collections
types =  collections.Counter(brown_test)
#print(types)  # types is in the form of directories

# converting dictionary into two dimentional array "a"
s = []
for value in types.items() :
    s.append(value)
#print(a)

#sorting array "a" in decending order
def sortthird(s): 
    return s[1] 
s.sort(key = sortthird ,reverse = True) 
#print(a)

#spliting words and tags fron sorted array "a"
test_words = []
t = 0 
for i in s:
    x = s[t][0]
    j = x.rsplit('/')
    test_words.append(j)
    t += 1 
# len of test_words1 is 10061    
print(test_words)  # now the size of test set come down to 10061 from 49948 word_tags pairs



# In[43]:

#maximum occuring tag in training corpus
mt = []
for i in max_fre_word_tag:
    mt.append(i[1])

import collections
mmt =  collections.Counter(mt)
print(mmt)  # list of maxximum occuring tag


# In[74]:

#unigram tagger for each unique words from training corpus

unigram_tag = []
y = len(max_fre_word_tag)
for i in test_words:
    for l in range(y): 
        if (i[0] == max_fre_word_tag[l][0]):
            temp = [i , max_fre_word_tag[l][1]]
            unigram_tag.append(temp)
            break;
#unigram_tag
temp = []
for i in unigram_tag:
    temp.append(i[0])

for i in test_words:
    if(i not in temp):
        temp1 = [i , 'unk']
        unigram_tag.append(temp1)
        
#print(unigram_tag) # unknown words are tagged as 'unk' tag at the bottom of list 

# we can tag unknown words by taking maximum occurring tag in this case it is "nn" have frequency 12403

f= open("unigram_tag_pred.txt","w+")
for i in unigram_tag:
     f.write("%s " %i)
    
f.close() 


# In[65]:

# seprating tags and words from brown _test
q = []
for i in brown_test:
    j = i.rsplit('/')
    q.append(j)


# In[68]:

z = len(unigram_tag)
seq_unigram_tag = []
for i in q:
    for j in range(z):
        if (i[0] == unigram_tag[j][0][0]):
            temp = [i, unigram_tag[j][1]]
            seq_unigram_tag.append(temp)
            break;


# In[75]:

f= open("brown_test_unigram_pred.txt","w+")
for i in seq_unigram_tag:
     f.write("%s " %i)
    
f.close() 


# In[87]:

# unigram pos accuracy
temp = 0
for i in seq_unigram_tag:
    if (i[0][1]==i[1]):
        temp += 1
d = len(seq_unigram_tag)
pos_accuracy = (temp/d)*100

print(pos_accuracy)


# In[82]:

# bigram tagging model of brown_train corpus
# seprating tags and words and counting each word tag pair for brown _train
q = []
for i in brown_train:
    j = i.rsplit('/')
    q.append(j)
    
# forming bigram model as list from training corpus
x = len(q)
bigram_train = [[]for i in range(x)]
for i in range(x):
    if i+1 < x:   
        bigram_train[i].append( q[i] )   
        bigram_train[i].append( q[i+1])
    
#print (bigram_train)   #bigram_train list have 1111244 

x = len(bigram_train)
bigram_tag = []
for i in range(x-1):
    p =[bigram_train[i][0][1] , bigram_train[i][1][1]]
    bigram_tag.append(p)
    
    
# getting frequency of tags from brown_train
from collections import Counter
types =  Counter(tuple(x) for x in bigram_tag)
#print(types)  # types is in the form of directories

# converting dictionary into two dimentional array "a"
s = []
for value in types.items() :
    s.append(value)
#print(s)

#sorting array "a" in decending order
def sortthird(s): 
    return s[1] 
s.sort(key = sortthird ,reverse = True) 
#print(s)            # bigram_training corpus get reduced from 1111244 to 455628 pairs

q = [] 
for i in s:
    q.append(i[0])

temp =[]
bi_max_fre_word_tag = []
for l in q:
    if (l[0] not in temp):
        temp.append(l[0])
        bi_max_fre_word_tag.append(l)
    
#print(bi_max_fre_word_tag)  # now the size of training set come down to 519 from 1111244 word_tags pairs

f= open("bi_max_fre_word_tag.txt","w+")
for i in bi_max_fre_word_tag:
     f.write(str(i))
     f.write("\n")
f.close() 


# In[84]:

# forming bigram model as list from test corpus
# seprating tags and words and counting each word tag pair for brown _test
q = []
for i in brown_test:
    j = i.rsplit('/')
    q.append(j)
    
# forming bigram model as list from training corpus
x = len(q)
bigram_test = [[]for i in range(x)]
for i in range(x):
    if i+1 < x:   
        bigram_test[i].append( q[i] )   
        bigram_test[i].append( q[i+1])
    
#print (bigram_test)   #bigram_test list have 49948

f= open("bigram_test.txt","w+")
for i in bigram_test:
     f.write(str(i))
     f.write("\n")
f.close() 


# In[130]:

#bigram tagger  predictions for test set from training corpus

bigram_tag_pre = []
x = len(bigram_test)
y = len(bi_max_fre_word_tag)
for i in range(x-1):
    g = bigram_test[i][0][1]
    for l in range(y): 
        if (g == bi_max_fre_word_tag[l][0]):
            temp = [bigram_test[i] , bi_max_fre_word_tag[l][1]]
            bigram_tag_pre.append(temp)
            break;

#print(bigram_tag)  # bigram_tag = [[[word,tag],[word,tag]], predicted tag]
# here we are considering only previous tag for bigram so unknown word will get tagged based there previous tag by MLE of tags 

f= open("bigram_tag_predicted.txt","w+")
for i in bigram_tag_pre:
     f.write(str(i))
     f.write("\n")
f.close() 


# In[86]:

#bigram pos accuray
temp = 0
for i in bigram_tag:
    if (i[0][1][1]==i[1]):
        temp += 1
d = len(bigram_tag)
pos_accuracy = (temp/d)*100

print(pos_accuracy)


# In[109]:

# confusion matrix for unigram
temp = [] 
for i in seq_unigram_tag:
    w =[i[0][1] , i[1]]
    temp.append(w)

conf_matrix = []
from collections import Counter
conf_matrix =  Counter(tuple(x) for x in temp)
print(conf_matrix)


# In[113]:

# confusion matrix for bigram
temp = [] 
for i in bigram_tag:
    w =[i[0][1][1] , i[1]]
    temp.append(w)

bi_conf_matrix = []
from collections import Counter
bi_conf_matrix =  Counter(tuple(x) for x in temp)
print(bi_conf_matrix)



# In[116]:

# tagging unknown words in unigram model
#considering only tagging unknown words
unk_uni = []
for i in seq_unigram_tag:
    if(i[1] == 'unk'):
        temp = [i , 'nn']
        unk_uni.append(temp)
        
# accuracy of unknown words 
temp = 0
for i in unk_uni:
    if (i[0][0][1] == i[1]):
        temp+=1
        
d = len(unk_uni)
unk_accuracy = (temp/d)*100

print(unk_accuracy)


# In[141]:

# extra credit bigram model 
q = []
for i in brown_train:
    j = i.rsplit('/')
    q.append(j)
    
# forming bigram model as list from training corpus
x = len(q)
bigram_train_exp = [[]for i in range(x)]
for i in range(x-2):
    if i+1 < x:   
        bigram_train_exp[i].append( q[i] )   
        bigram_train_exp[i].append( q[i+1])
        bigram_train_exp[i].append( q[i+2])
    
#print (bigram_train_exp)   


# In[136]:

x = len(bigram_train_exp)
bigram_tag_exp = []
for i in range(x-2):
    p =[bigram_train_exp[i][0][1] , bigram_train_exp[i][1][1] , bigram_train_exp[i][2][1] ]
    bigram_tag_exp.append(p)
    


# In[138]:

# getting frequency of tags from brown_train
from collections import Counter
types =  Counter(tuple(x) for x in bigram_tag_exp)
#print(types)  # types is in the form of directories

# converting dictionary into two dimentional array "a"
s = []
for value in types.items() :
    s.append(value)
#print(s)

#sorting array "a" in decending order
def sortthird(s): 
    return s[1] 
s.sort(key = sortthird ,reverse = True) 
#print(s)            # bigram_training corpus get reduced from 1111244 to 455628 pairs

q = [] 
for i in s:
    q.append(i[0])

temp =[]
bi_max_fre_word_tag_exp = []
for l in q:
    if (l[0] not in temp):
        temp.append(l[0])
        bi_max_fre_word_tag_exp.append(l)
    
#print(bi_max_fre_word_tag)  # now the size of training set come down to 519 from 1111244 word_tags pairs



# In[158]:

#brown test model 
q = []
for i in brown_test:
    j = i.rsplit('/')
    q.append(j)
    
# forming bigram model as list from training corpus
x = len(q)
bigram_test_exp = [[]for i in range(x)]
for i in range(x-2):
    if i+1 < x:   
        bigram_test_exp[i].append( q[i] )   
        bigram_test_exp[i].append( q[i+1])
        bigram_test_exp[i].append( q[i+2])
        
#bigram_test_exp


# In[157]:

#bigram tagger  predictions for test set from training corpus

bigram_tag_pre_exp = []
x = len(bigram_test_exp)
y = len(bi_max_fre_word_tag_exp)
for i in range(x-2):
    g = bigram_test_exp[i][0][1]
    h = bigram_test_exp[i][2][1]
    for l in range(y): 
        if (g == bi_max_fre_word_tag_exp[l][0] and h == bi_max_fre_word_tag_exp[l][0]):
            temp = [bigram_test_exp[i] , bi_max_fre_word_tag_exp[l][1]]
            bigram_tag_pre_exp.append(temp)
            break;

#bigram_tag_pre_exp  

f= open("bigram_tag_predicted_exp.txt","w+")
for i in bigram_tag_pre_exp:
     f.write(str(i))
     f.write("\n")
f.close() 
        


# In[156]:

#bigram pos accuray for different method
temp = 0
for i in bigram_tag_pre_exp:
    if (i[0][1][1]==i[1]):
        temp += 1
d = len(bigram_tag_pre_exp)
pos_accuracy_exp = (temp/d)*100

print(pos_accuracy_exp)


# In[ ]:



