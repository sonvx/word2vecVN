# Requirements:
- ```pip install gensim flask```
- Download any dictionary and put it into ./data/ (Note: ./data/vnex.model.bin is a super tiny model that was created for testing purpose only).
    - Trained on Vietnamese Wiki: https://drive.google.com/open?id=0B1GKSX6YCHXlakkzQ2plZVdUUE0
    - Trained on Le at al.'s data (window_size 5, 400 dimensions): https://drive.google.com/open?id=0B1GKSX6YCHXlMTVZNkFEYzRyd1E
    - Trained on Le at al.'s data (window_size 2, 300 dimensions): https://drive.google.com/open?id=1LV9z1RXkEg0niuC15jcW2JeeYDilXiiC

# How to run
- python ./Main.py
- Visit http://localhost:8089

# Screenshot
![Alt text](https://raw.githubusercontent.com/sonvx/word2vecVN/master/word2vec-simple-visualization/images/w2v_vn.png "Screenshot example of one given input")

