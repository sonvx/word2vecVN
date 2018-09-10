# word2vecVN
Word2Vec models for Vietnamese
## Download models:
- Model trained on Vietnamese Wiki: [click here](https://drive.google.com/open?id=0B1GKSX6YCHXlakkzQ2plZVdUUE0).
- Model trained on Le et al.'s data (window-size 5, 400 dims): [click here](https://drive.google.com/open?id=0B1GKSX6YCHXlMTVZNkFEYzRyd1E).
- Model trained on Le et al.'s data (window-size 2, 300 dims): [click here](https://drive.google.com/open?id=1LV9z1RXkEg0niuC15jcW2JeeYDilXiiC).
## Visualization:
- word2vec-visualization (using TensorBoard):
	+ Download tf\_files: [click here](tba)
	+ Run $ tensorboard --logs=./<path-to-the-folder> --port=10001
- word2vec-simple-visualization: It is working well. Please read the readme file inside that folder to know how to test the model.
## Note: 
-  This model is trained using data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72

### Citation
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
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/w2vecVN_tb.png "Screenshot example of one given input" =250x)
# Screenshot of spacy-n-fastext
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/images/spacy_example.png "Screenshot example of spacy and fastext" =250x)
      

### Attributions/Thanks
- This project could not have happened without the data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72
