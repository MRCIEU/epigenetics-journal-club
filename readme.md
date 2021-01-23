## Epigenetics journal club

The IEU epigenetics journal club meets 1-2 Mondays per month.
Each meeting relevant papers published since the last meeting are
briefly presented and discussed. This repository contains:
- [presentations](https://mrcieu.github.io/epigenetics-journal-club/)
- scripts for selecting candidate papers
- data files recording previous candidate papers and presented papers

## How candidate papers are selected 

Candidate papers are all those published since the last meeting
that come up in a pubmed query (saved in "data/pubmed-query.txt")
or cite a paper presented in a
previous journal club (saved in "data/presented.txt"). Any papers
that have come up in previous searches but were not selected for
presentation are ignored (saved in "data/ignore.txt").

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

*Once you have selected papers to present, add their PMIDs to "data/presented.txt".*


