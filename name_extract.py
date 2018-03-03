import nltk

sample = "Rahul Gandhi was smart. Bush was great. Martin Luther King and United States. Linclon was big. Nelson Mandela is from Africa"
     
sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.chunk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'label') and t.label:
    
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)
    
    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print (entity_names)

name_search = []

#for i in entity_names:
#    
#    if i == entity_names[j]:
#        print(i)
#        name_search[j] = i;
#                   
#        j = j+1;
#        
##print([sam + '.' for sam in sample.split('.') if name_search in sam])
#
#
#for k in range(3):
#    print(name_search[k])

length_names = len(entity_names)

for i in range(length_names):
    print([sam + '.' for sam in sample.split('.') if entity_names[i] in sam])