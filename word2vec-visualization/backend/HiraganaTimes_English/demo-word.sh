time ./word2vec -train HiraganaTimes_English_preprocessed.txt -output model.bin -cbow 0 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15
./distance model_skipgram.bin
