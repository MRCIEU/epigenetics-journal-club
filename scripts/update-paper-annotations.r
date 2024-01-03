library(journalclub)

pmids <- readLines("data/ignore.txt")
papers <- read.csv("data/ignore.csv")

pmids <- setdiff(pmids, c("NA", papers$pmid))

if (length(pmids) > 0) {

    pmids <- split(pmids, 1:ceiling(length(pmids)/50))
    
    i <- 0
    new <- lapply(pmids, function(pmids) {
        i <<- i + 1
        if (i > 1)
            Sys.sleep(60)
        cat(date(), "step", i, "\n")
        papers <- NULL
        tryCatch({
            papers <- journalclub.annotate(pmids)
            if (ncol(papers) < 10)
                papers <- NULL
            else
                papers <- papers[which(!is.na(papers$abstract)),]
        }, error=function(e) {
            cat("Error", i, "\n")
        })        
        papers
    })
    new <- do.call(rbind, new)

    if (!is.null(new) && nrow(new) > 0) {  
        papers <- rbind(papers, new)
        write.csv(papers, file="data/ignore.csv", row.names=F)
    }
}
