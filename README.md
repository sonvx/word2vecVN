# I. word2vecVN
Word2Vec models for Vietnamese
## Download models:
- Model trained on Vietnamese Wiki: [click here](https://drive.google.com/open?id=0B1GKSX6YCHXlakkzQ2plZVdUUE0).
- Model trained on Le et al.'s data (window-size 5, 400 dims): [click here](https://drive.google.com/open?id=0B1GKSX6YCHXlMTVZNkFEYzRyd1E).
- Model trained on Le et al.'s data (window-size 2, 300 dims): [click here](https://drive.google.com/open?id=1LV9z1RXkEg0niuC15jcW2JeeYDilXiiC).
## Visualization:
- word2vec-visualization (using TensorBoard):
	+ Download tf\_files: [TBA](tba)
	+ Run $ tensorboard --log_dir=./<path-to-the-folder> --port=10001
- word2vec-simple-visualization: It is working well. Please read the readme file inside that folder to know how to test the model.
## Note: 
-  This model is trained using data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72
	+ Data information: 7.1G text with 1,675,819 unique words from a corpus of 974,393,244 raw words and 97,440 documents. Note that all words are tokenized words.

# II. How do I cite?
Please CITE paper the Arxiv paper whenever ETNLP (or the pre-trained embeddings) is used to produce published results or incorporated into other software:

```
@article{vu:2019n,
  title={ETNLP: A Visual-Aided Systematic Approach to Select Pre-Trained Embeddings for a Downstream Task},
  author={Xuan-Son Vu, Thanh Vu, Son N. Tran, Lili Jiang},
  journal={In: Proceedings of the International Conference Recent Advances in Natural Language Processing (RANLP)},
  year={2019}
  }
  
 @misc{word2vecvn_2016,
    author = {Xuan-Son Vu},
    title = {Pre-trained Word2Vec models for Vietnamese},
    year = {2016},
    howpublished = {\url{https://github.com/sonvx/word2vecVN}},
    note = {commit xxxxxxx}
  }
```


## Cited in papers:
> 1. Thanh Vu, Dat Quoc Nguyen, Dai Quoc Nguyen, Mark Dras and Mark Johnson. 2018. VnCoreNLP: A Vietnamese Natural Language Processing Toolkit. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Demonstrations, NAACL 2018, pages 56-60. [bibtext](http://aclweb.org/anthology/N18-5012.bib), [github](https://github.com/vncorenlp/VnCoreNLP)

# III. Some screenshots:
## Screenshot of word2vec
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/w2vecVN_tb.png "Screenshot example of one given input")
## Screenshot of spacy-n-fastext
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/spacy_example.png "Screenshot example of spacy and fastext")
      

### Attributions/Thanks
- This project could not have happened without the data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72
