## Epigenetics journal club

The IEU epigenetics journal club meets 1-2 Mondays per month.
Each meeting relevant papers published since the last meeting are
briefly presented and discussed. This repository contains:
- [presentations](https://mrcieu.github.io/epigenetics-journal-club/)
- scripts for selecting candidate papers
- data files recording previous candidate papers and [presented papers](https://github.com/MRCIEU/epigenetics-journal-club/blob/main/data/papers.csv)

## How candidate papers are selected 

Candidate papers are all those published since the last meeting
that 

1. come up in a pubmed query (saved in "data/pubmed-query.txt"), OR

2. cite a paper presented in a previous journal club (saved in "data/presented.txt") AND

3. do not appear in  journal whose name is in "data/blacklisted.txt" AND

4. has not come up in previous searches but was not selected for
   presentation (these are papers are saved in "data/ignore.txt").


## Generating a list of candidate papers 

Run the following from the command line:

  ```
  Rscript --vanilla scripts/generate-candidates.r
  ```

By default, the script will look back 30 days for new papers
and save them to 'candidates.csv'.

These defaults can be changed, e.g.
  ```
  Rscript --vanilla scripts/generate-candidates.r 60 jc.csv
  ```


## Experimental

Probabilities of interest can be assigned to papers using
a simple script script/train-bag-of-words.py.

```
python script/train-bag-of-words.py
```

This will load the generated 'candidates.csv' file, calculate probabilities
and save the result in a file called 'candidates-with-probs.csv'.

*Once you have selected papers to present, add their PMIDs to "data/presented.txt"
and add the list of papers to 'data/papers.csv'.*


