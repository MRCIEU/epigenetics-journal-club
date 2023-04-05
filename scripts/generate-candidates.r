 ## Rscript --vanilla scripts/generate-candidates.r [DAYS] [FILENAME]

days <- 60
filename <- "candidates.csv"

args <- commandArgs(trailingOnly=TRUE)
if (length(args) > 1) {
    days <- as.integer(args[2])
    if (days < 30 || days > 365) {
        warning(paste("Requested value", days, "is too extreme!"))
        days <- 60
    }
}
if (length(args) > 2) 
    filename <- args[3]

if (file.exists(filename))
    stop("Output file", filename, "already exists.")

cat(paste("Looking back", days, "days for new papers."))

cat(paste(
    "Should take about",
    round(length(readLines("data/presented.txt"))/1600*30,0),
    "minutes ...\n"))

library(journalclub) ## https://github.com/perishky/journalclub 
candidates <- journalclub.candidates("data", recent=days, retmax=10, debug=F)
## If the command above gives an error about "XML content",
## then pubmed retrieval output has been restricted so
## you might need to reduce "retmax" and try again.

write.csv(candidates[,c("pmid","title","source","abstract")], file=filename, row.names=F) 

cat(paste0("Candidate papers saved to '", filename, "'.\n"))


