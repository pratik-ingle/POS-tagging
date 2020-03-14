## POS Tagging 

Here instead of creating files I have used lists for simplicity if we need to create file for results the we can use file write format present in python same as first step of reading brown.txt  with write and read data type. 

1.Corpus 
Dividing corpus into two parts- 
	Brown train
	Brown test

with open('brown.txt','r') as f:
	corpus = f.read() 
	#print(corpus)

words = corpus.split()        # split function converting whole corpus in to list of words so it will be easy to handle
#print(words[:])


#creating two corpus as brown_test and brown_train
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


Length of test and train corpus is:

print(len(brown_test))
49948
print(len(brown_train))
1111244


2.Tagger implementation:

A. Unigram tagger 

Separating tags from brown_train corpus 

## getting frequency of tags from brown_train
import collections
types =  collections.Counter(brown_train)
#print(types)  # types is in the form of directories

## converting dictionary into two dimentional array "a"
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
#len of b is 64413
    
#cosidering only maximum frequent word-tag pairs from array "b" 
temp =[]
max_fre_word_tag = []
for l in b:
    if (l[0] not in temp):
        temp.append(l[0])
        max_fre_word_tag.append(l)
    
print(max_fre_word_tag)  # now the size of training set come down to 54068 from 1111244 word_tags pairs

Separating tags from Brown_test corpus

## word_tags pair from brown_test corpus
## getting frequency of tags from brown_test
import collections
types =  collections.Counter(brown_test)
#print(types)  # types is in the form of directories

#converting dictionary into two dimentional array "a"
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
len of test_words1 is 10061    
print(test_words)  # now the size of test set come down to 10061 from 49948 word_tags pairs

 
Unigram tagger predicted for each unique word:

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
        
#print(unigram_tag)   # unknown words are tagged as 'unk' tag at the bottom of list 

# we can tag unknown words by taking maximum occurring tag in this case it is "nn" have frequency 12403

f= open("unigram_tag_pred.txt","w+")
for i in unigram_tag:
     f.write("%s " %i)
    
f.close() 


Predicting tags in sequence for test set

## seprating tags and words from brown _test
q = []
for i in brown_test:
    j = i.rsplit('/')
    q.append(j)

z = len(unigram_tag)
seq_unigram_tag = []
for i in q:
    for j in range(z):
        if (i[0] == unigram_tag[j][0][0]):
            temp = [i, unigram_tag[j][1]]
            seq_unigram_tag.append(temp)
            break;


f= open("brown_test_unigram_pred.txt","w+")
for i in seq_unigram_tag:
     f.write("%s " %i)   
f.close()

In unigram tagger training set is using only 135 word_tag pairs according to MLE out of 185 tags


B.  Bigram tagger
 
Getting bigram tag pairs from training corpus 
By using counter and sorting we will only consider unique tag pairs and MLE from training corpus it will reduce our training data set to 519 from 1111244 pairs of tag from original brown_training corpus

For bigram tagger have used only 46 tangs by MLE out of 183 tags so bigram tagger accuracy (31.84%) is much less compare to unigram tagger (86.07%)
  
## bigram tagging model of brown_train corpus
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
    
    
## getting frequency of tags from brown_train
from collections import Counter
types =  Counter(tuple(x) for x in bigram_tag)
#print(types)  # types is in the form of directories

#converting dictionary into two dimentional array "a"
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
    
print(bi_max_fre_word_tag) 
 #now the size of training set come down to 519 from 1111244 word_tags pairs since we are considering MLE 


size of training set come down to 519 from 1111244 bigram_tags pairs since we are considering MLE of bigram tag pairs

Forming bigram pairs of test set for predictions

## forming bigram model as list from test corpus
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
    
#print (bigram_test)   #bigram_test list have 49948 pairs

bigram tagger  predictions for test set from training corpus

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


c.Strategy for dealing with unknown words 
Unigram = we can tag unknown words by taking maximum occurring tag in this case it is "nn" have frequency 12403.
By doing this we get almost 10-20% accuracy for unknown words

# considering only tagging unknown words
unk_uni = []
for i in seq_unigram_tag:
    if(i[1] == 'unk'):
        temp = [i , 'nn']
        unk_uni.append(temp)
## accuracy of unknown words
temp = 0
for i in unk_uni:
    if (i[0][0][1] == i[1]):
        temp+=1
        
d = len(unk_uni)
unk_accuracy = (temp/d)*100

print(unk_accuracy)

11.845624761176921
Bigram = for bigram tagging we are considering only previous tag for bigram so unknown word will get tagged based their previous tag by MLE of tags. 

3.tagger evolution

overall POS tagging accuracy 
For unigram

temp = 0
for i in seq_unigram_tag:
    if (i[0][1]==i[1]):
        temp += 1
d = len(seq_unigram_tag)
pos_accuracy = (temp/d)*100

print(pos_accuracy)
 POS accuracy for unigram = 86.07351645711539

For bigram:
temp = 0
for i in bigram_tag:
    if (i[0][1][1]==i[1]):
        temp += 1
d = len(bigram_tag)
pos_accuracy = (temp/d)*100

print(pos_accuracy)
POS accuracy for bigram =31.844940130551443


confusion matrix for each tagger 
Total tag present = 185
Tags used by MLE model = 135

Unused tags are marked as 'not in prediction set'

Confusion matrix for unigram

## confusion matrix for unigram
temp = [] 
for i in seq_unigram_tag:
    w =[i[0][1] , i[1]]
    temp.append(w)

conf_matrix = []
from collections import Counter
conf_matrix =  Counter(tuple(x) for x in temp)
print(conf_matrix)



For bigram confusion matrix

## confusion matrix for bigram
temp = [] 
for i in bigram_tag:
    w =[i[0][1][1] , i[1]]
    temp.append(w)

bi_conf_matrix = []
from collections import Counter
bi_conf_matrix =  Counter(tuple(x) for x in temp)
print(bi_conf_matrix)



3.Accuracy of unknown words
Unigram:
All unknown word will get tagged as ‘nn’ since it the MLE tag in training data(code can be get from unigram tagger code above were unknown are tagged as ’unk’) 

# considering only tagging unknown words
unk_uni = []
for i in seq_unigram_tag:
    if(i[1] == 'unk'):
        temp = [i , 'nn']
        unk_uni.append(temp)


## accuracy of unknown words
temp = 0
for i in unk_uni:
    if (i[0][0][1] == i[1]):
        temp+=1
        
d = len(unk_uni)
unk_accuracy = (temp/d)*100

print(unk_accuracy)

11.845624761176921

 
Bigram:
here we are considering only previous tag for bigram so unknown word will get tagged based there previous tag by MLE of tags(code can get from bigram_tagger code above)


Extra credit 
1.For tagging unknown words for bigram we can consider Laplace smoothing for tags since lots of tags are not used in predicting set only 47 tags get used in bigram model out of 183 tags
For unigram 135 were get used out of 185

Bigram 
2.we can also use previous word and next word tag to predict tag for given word in test set from training set
Give 33.819345661450924 % accuracy compare to normal bigram which is 31.844940130551443%


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


x = len(bigram_train_exp)
bigram_tag_exp = []
for i in range(x-2):
    p =[bigram_train_exp[i][0][1] , bigram_train_exp[i][1][1] , bigram_train_exp[i][2][1] ]
    bigram_tag_exp.append(p)
    

# getting frequency of tags from brown_train
from collections import Counter
types =  Counter(tuple(x) for x in bigram_tag_exp)
#print(types)  # types is in the form of directories

#converting dictionary into two dimentional array "a"
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

Bigram tagger experiment 

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

Accuracy

#bigram pos accuray for different method
temp = 0
for i in bigram_tag_pre_exp:
    if (i[0][1][1]==i[1]):
        temp += 1
d = len(bigram_tag_pre_exp)
pos_accuracy_exp = (temp/d)*100

print(pos_accuracy_exp)

33.819345661450924
