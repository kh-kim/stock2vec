# Stock2Vec

Stock prices are flutuated in every day. So, in each day, put those stocks in order of price change to one sentence. Then, with certain window size, each stock will show up with highly related stock frequently, because they tend to move their prices together.  
For example, [005380(Hyundai Motors)](http://finance.yahoo.com/quote/005380.KS/?p=005380.KS) moves together [000270(Kia Motors)](http://finance.yahoo.com/quote/000270.KS/?p=000270.KS). Because not only they are in same industry, but also Hyndai owns Kia.

In this repo, embedding is done with Skip-gram from Word2Vec, and GloVe, but code for embedding is not included because there are already wide spreaded. 

You can figure out which stock is related with cosine similarity. In addition, some of result files are delimited with "\001" because I wanted to put those to Hive. Belows are short description about included files.

## File description
- sentences.txt: Source file. Each day has one row. Each row represent a set of stocks which is sorted by price difference between the day and a day before that day.
- sentences.refined.output.txt: There are 3 columns (source stock, dest stock, similarity based on **Skip-gram**) and they are "\001" delimited. 
- sentences.refined.output_glove.txt: There are 3 columns (source stock, dest stock, similarity based on **GloVe**) and they are "\001" delimited. 
- sentences.refined.vectors.txt: Columns are "\t" delimited. First column represents a stock code and rest are vectors from **Skip-gram**.
- sentences.refined.gloves.txt: Columns are "\t" delimited. First column represents a stock code and rest are vectors from **GloVe**.
