# word2vecVN
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
	+ Data information: 7.1G text with 1,675,819 word types from a corpus of 974,393,244 raw words and 97,440 documents. Note that all words are tokenized words.


## Cited in papers:
> 1. Thanh Vu, Dat Quoc Nguyen, Dai Quoc Nguyen, Mark Dras and Mark Johnson. 2018. VnCoreNLP: A Vietnamese Natural Language Processing Toolkit. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Demonstrations, NAACL 2018, pages 56-60. [bibtext](http://aclweb.org/anthology/N18-5012.bib), [github](https://github.com/vncorenlp/VnCoreNLP)


## Citation
```
  @misc{word2vecvn_2016,
    author = {Xuan-Son Vu},
    title = {Pre-trained Word2Vec models for Vietnamese},
    year = {2016},
    howpublished = {\url{https://github.com/sonvx/word2vecVN}},
    note = {commit xxxxxxx}
  }
```

# Screenshot of word2vec
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/w2vecVN_tb.png "Screenshot example of one given input")
# Screenshot of spacy-n-fastext
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/spacy_example.png "Screenshot example of spacy and fastext")
      

### Attributions/Thanks
- This project could not have happened without the data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72
