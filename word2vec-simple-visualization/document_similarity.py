# from nltk import sent_tokenize, word_tokenize
#
# #word2vec
# import codecs
# import gensim
import numpy as np
import operator
from numpy import array
from scipy import spatial
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from gensim.models import Word2Vec
np.errstate(divide='ignore', invalid='ignore')
from nltk.corpus import stopwords

global glb_word2vec_model
global glb_dimension
global glb_vocab
global glb_stopwords_en
global glb_outof_w2vec_dict


def setup_data():
    doc_list = ['I love you', 'You are her lover', 'She kiss him']
    return doc_list


def vocab_builder(doc_list):
    all_text = ''
    for element in doc_list:
        for word in nltk.wordpunct_tokenize(element):
            if (len(word) > 1):
                all_text += word.lower() + " "
    tokens = nltk.wordpunct_tokenize(all_text)
    # words = [w.lower() for w in tokens]
    vocab = sorted(set(tokens))
    return vocab


def avg_feature_vector(words, model, num_features, index2word_set):
    feature_vec = np.zeros((num_features,), dtype="float32")
    nwords = 0

    outof_w2vec_dict = ''
    print 'Len of words = ' + str(len(words))
    for word in words:
        if word in index2word_set:
            nwords = nwords + 1
            #print "word:model=" + word + ":" + str(model[word])

            try:
                processword = model[word]
            except KeyError, e:
                outof_w2vec_dict += str(e) + " "
                continue
            except:
                continue
            feature_vec = np.add(feature_vec, processword)

            if(nwords > 0):
                feature_vec = np.divide(feature_vec, nwords)

    #print "featureVec: " + str(featureVec)
    file_out = open("./outof_w2vec.dict", "a")
    file_out.write(outof_w2vec_dict + "\n")
    file_out.close()

    return feature_vec


def rerank_word2vec_similarity(doc1, doc2):
    #answer.lower();
    #query.lower();
    print 'doc1 = ' + doc1 + '; doc2 = ' + doc2
    sen1_avg_vector = avg_feature_vector(nltk.wordpunct_tokenize(doc1.lower()), model=glb_word2vec_model, num_features=glb_dimension,
                                         index2word_set=glb_vocab)
    print 'vec1 = ' + str(sen1_avg_vector)
    sen2_avg_vector = avg_feature_vector(nltk.wordpunct_tokenize(doc1.lower()), model=glb_word2vec_model, num_features=glb_dimension,
                                         index2word_set=glb_vocab)

    print 'vec2 = ' + str(sen2_avg_vector)
    sen1_sen2_similarity = 1 - spatial.distance.cosine(sen1_avg_vector, sen2_avg_vector)
    return sen1_sen2_similarity


def ranking_docs(list_docs):
    glb_vocab = vocab_builder(list_docs)
    list_vectors = []
    for doc in list_docs:
        list_vectors.append(avg_feature_vector())


def sim(doc1, doc2):
    return abs(len(doc1) - len(doc2))


def print_matrix(matrix, w, h):
    out_str = ''
    for idx in range(0, w):
        for jdx in range(0, h):
            out_str += str(matrix[idx][jdx]) + '\t\t'
        out_str += '\n'
    print out_str


def ranking_matrix(list_docs):
    # list_docs = [
    #     '1',
    #     '123',
    #     '123456',
    #     '1234567890'
    # ]
    w, h = len(list_docs), len(list_docs)
    matrix = [[0 for x in range(w)] for y in range(h)]

    for idx in range(0, len(list_docs)):
        for jdx in range(0, len(list_docs)):
            matrix[idx][jdx] = 0

    # print_matrix(matrix, w, h)

    for idx in range(0, len(list_docs)):
        for jdx in range(idx+1, len(list_docs)):
            matrix[idx][jdx] = rerank_word2vec_similarity(list_docs[idx], list_docs[jdx])

    # print 'after calculate top-left angle: \n'
    # print_matrix(matrix, w, h)

    for idx in range(0, len(list_docs)):
        for jdx in range(idx + 1, len(list_docs)):
            matrix[jdx][idx] = matrix[idx][jdx]

    # print 'after update down-left angle: \n'
    # print_matrix(matrix, w, h)

    # print 'test :\n'
    final_rank = [0 for i in xrange(w)]
    for idx in range(0, len(list_docs)):
        # print str(matrix[idx][0:])
        final_rank[idx] = np.sum(matrix[idx][0:])

    final_dic = {}
    for idx in range(0, len(list_docs)):
        final_dic['doc_' + str(idx)] = final_rank[idx]

    sorted_x = sorted(final_dic.items(), key=operator.itemgetter(1), reverse=True)

    print 'final out: ' + str(sorted_x)

if __name__ == '__main__':
    list_docs = ['she is so lovely', 'i love her so much', 'i hate that guy who does not love me', 'i hate him a lot']
    print 'Loading model ...'
    word2vec_model = '/Users/apple/Documents/UKP/Projects/DLQA/GIT_SRC/argumentqa.sonvx/argumentqa/static/model/tiny.en.model.bin'
    glb_word2vec_model = Word2Vec.load_word2vec_format(word2vec_model, binary=True)
    glb_dimension = 5
    glb_vocab = vocab_builder(list_docs)
    print 'vocab = {' + str(glb_vocab) + '}'
    glb_stopwords_en = stopwords.words('english')
    ranking_matrix(list_docs)
