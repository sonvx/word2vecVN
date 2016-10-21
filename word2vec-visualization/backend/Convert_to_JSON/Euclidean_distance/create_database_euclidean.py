#Author: Phi Van Thuy
#Purpose: Convert word2vec models to JSON database by Euclidean distance metric (instead of Cosine distance)

from gensim.models import word2vec

#Trained model
model_path = "/home/sonvx/word2vecVN/trainmodel/baomoi.model.bin"

print "Loading model..."
model = word2vec.Word2Vec.load_word2vec_format(model_path, binary=True)  # C binary format
print "Loading model: Done"

f = open('vi_data_cosine_skipgram_original.json','w')

f.write("{\n")

number_words = len(model.vocab)
#number_words = 10000
for i in range(0, number_words):
	
	stringA = model.vocab.items()[i][0]
	f.write("\n\"" + stringA.encode("utf-8") + "\":[\n")

	nearest_words = model.most_similar_euclidean(positive=[stringA], negative=[],  topn=20)
	number_nearest_words = len(nearest_words)

	for j in range(0, number_nearest_words):
		f.write("{\"w\":\"" + nearest_words[j][0].encode("utf-8") + "\",\"d\":" + str(round(nearest_words[j][1], 3)) + "}")
		if j != number_nearest_words - 1:
			f.write(",\n")
		else:
			f.write("]")

	if i != number_words - 1:
		f.write(",\n")
	else:
		f.write("\n")

f.write("\n}\n")

f.close()

print "Finished!"
