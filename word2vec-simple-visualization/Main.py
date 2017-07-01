import requests
#from flask import Flask, render_template, jsonify
from flask import Flask, render_template, abort, request, jsonify
from flask import request, redirect, url_for
import codecs
import gensim
from distutils.version import LooseVersion, StrictVersion


app = Flask(__name__)


global word2vec_model


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.values['search'] or ''
        # query = unicode(query, "utf-8")
        # query = query.decode().encode("utf-8")
        query = unicode(query).lower()
        print 'query = ' + query
        output = []
        try:
            sim_list = word2vec_model.most_similar(query, topn=50)
            #output = word2vec_model.most_similar('u' + '\"' + query + '\"', topn=5)
            for wordsimilar in sim_list:
                # output[wordsimilar[0]] = wordsimilar[1]
                output.append(wordsimilar[0] + ' - '+ str(wordsimilar[1]))
                # file = codecs.open("output.txt", "a", "utf-8")
                # file.write(wordsimilar[0] + "\t" + str(wordsimilar[1]) + "\n")
                # file.close()
        except:
            output = 'Not found' + query
    return render_template('search.html', pages=output)


@app.route("/")
def get_index():
    return render_template('search.html')


if __name__ == "__main__":
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # download from https://drive.google.com/open?id=0B1GKSX6YCHXlakkzQ2plZVdUUE0
    model = dir_path + '/data/wiki.vi.model.bin'
    word2vec_model = None

    if os.path.isfile(model):
        print 'Loading word2vec model ...'
	if LooseVersion(gensim.__version__) >= LooseVersion("1.0.1"):
	    from gensim.models import KeyedVectors
	    word2vec_model = KeyedVectors.load_word2vec_format(model, binary=True)
	else:
	    from gensim.models import Word2Vec
            word2vec_model = Word2Vec.load_word2vec_format(model, binary=True)
	    
        app.run(port=8089)
    else:
        print "Download word2vec model and put into ./data/. File: https://drive.google.com/open?id=0B1GKSX6YCHXlakkzQ2plZVdUUE0"
