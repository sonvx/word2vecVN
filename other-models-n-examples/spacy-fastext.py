from __future__ import unicode_literals
import plac
import numpy

import spacy
from spacy.language import Language

# Get it from https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.vi.vec
vectors_loc=("/mnt/data/ResearchData/Word2vecDict/wiki.vi.vec")


def load_nlp(vectors_loc, lang=None):
    if lang is None:
        nlp = Language()
    else:
        # create empty language class – this is required if you're planning to
        # save the model to disk and load it back later (models always need a
        # "lang" setting). Use 'xx' for blank multi-language class.
        nlp = spacy.blank(lang)
    with open(vectors_loc, 'rb') as file_:
        header = file_.readline()
        nr_row, nr_dim = header.split()
        nlp.vocab.reset_vectors(width=int(nr_dim))
        for line in file_:
            line = line.rstrip().decode('utf8')
            pieces = line.rsplit(' ', int(nr_dim))
            word = pieces[0]
            vector = numpy.asarray([float(v) for v in pieces[1:]], dtype='f')
            nlp.vocab.set_vector(word, vector)  # add the vectors to the vocab
    return nlp


def test_similarity(nlp):
    # test the vectors and similarity
    # text = u'ngủ ngon'
    # doc = nlp(text)
    # print(text, doc[0].similarity(doc[1]))
    docs = [nlp(u"Tôi yêu Hà Nội"), nlp(u"Hà Nội đẹp quá"),
        nlp(u"Cô ấy đẹp quá"), nlp(u"Hà Nội là thủ đô của Việt Nam")]

    for doc in docs:
        for other_doc in docs:
            print('{:<10}\t{}\t{}'.format(doc.text, other_doc.text, doc.similarity(other_doc)))
test_similarity(nlp_model)
