# word2vec-visualization
Word Vectors Visualization in Tree Form

Authors: Phi Van Thuy and Taishi Ikeda.

Supervisor: Assistant Professor Kevin Duh.

- Two types of distances: Cosine distance and Euclidean distance.
- Totally 8 different models for the English and the Japanese data.
- Run simple HTTP server: "python -m SimpleHTTPServer 8888".

![fig1] (demo_en.png)
<br><br><br><br>
![fig2] (demo_ja.png)

- Main files and folders:
	+ backend<br>
		+ HiraganaTimes_English<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in English; skip-gram (slower, better for infrequent words) vs CBOW (fast).
		+ HiraganaTimes_Japanese<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in Japanese; skip-gram (slower, better for infrequent words) vs CBOW (fast).
		+ Convert_to_JSON <br>
			scripts for converting word2vec models to JSON databases.
	+ frontend<br>
		+ data<br>
			contain all data for searching word and vizualize them: "data_cosine.json" and "data_euclidean.json" are the databases. The flare-format data is created from the database when running the web page.
		+ js<br>
			contain D3.js library (visualization javascript library).
		+ word2vec_tree_final.html<br>
			the main web page.

- Visualize your own data
	+ To convert the word2vec models to the JSON files, the Gensim library (https://radimrehurek.com/gensim/install.html) is required.
	Quick install Gensim: "easy_install -U gensim" or, alternatively: "pip install --upgrade gensim".
	+ For Cosine distance metric: use script "create_database_cosine.py".
	+ For Euclidean distance metric: use script "create_database_euclidean.py", and copy the file "word2vec.py" to Gensim library's location, e.g., "/Library/Python/2.7/site-packages/gensim-0.10.3-py2.7-macosx-10.10-intel.egg/gensim/models". In this new implementation, the new method most_similar_euclidean() is included to calculate the distance between pairs of words/phrases by Euclidean metric.
	+ Special characters should be excluded from JSON files to generate the correct JSON format. More details are in "Remove_Special_Characters.txt" file.

- For Vietnamese:
	+ I am testing the UI by quickly replacing English dict with a Vietnamese dict. It doesn't work already so there must be encoding problems. Feel free to test with vi_data_euclidean_skipgram_tiny.json/vi_data_cosine_skipgram_tiny.json.
