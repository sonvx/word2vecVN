# word2vecVN
Word2Vec model for Vietnamese
- For Vietnamese:
	+ word2vec-visualization: I am testing the UI by quickly replacing English dict with a Vietnamese dict. It doesn't work already so there must be encoding problems. Feel free to test with ./word2vec-visualization/frontend/data/vi_*.json. Please send a request to commit any changes that can fix the bug. Feel free to use the simple UI instead if you don't know how to fix this problem or don't have time to check on it.

	+ word2vec-simple-visualization: It is working well. Please read the readme file inside that folder to know how to test the model.
- For English and JP: Use the original project at https://github.com/pvthuy/word2vec-visualization
- Note: This model is trained using data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72

### Citation
```
  @misc{word2vecvn_2016,
    author = {Xuan-Son Vu},
    title = {Pre-trained Word2Vec model for Vietnamese},
    year = {2016},
    howpublished = {\url{https://github.com/sonvx/word2vecVN}},
    note = {commit xxxxxxx}
  }
```

# Screenshot
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/word2vec-simple-visualization/images/w2v_vn.png "Screenshot example of one given input")
      

### Attributions/Thanks
- This project could not have happened without the data of Le et al. http://mim.hus.vnu.edu.vn/phuonglh/node/72
