## pmids from before March, 2019
pmids <- readLines("journal-club-archive.mht")
chopped <- head(grepl("=$", pmids),-1)
starts <- which(c(T,!chopped))
ends <- which(c(!chopped,T))
pmids <- sub("=$", "", pmids)
pmids <- sapply(1:length(starts), function(i) {
    if (starts[i] < ends[i]) 
        paste(pmids[starts[i]:ends[i]], collapse="")
    else
        pmids[starts[i]]
})
    
pmids <- pmids[grep("pubmed/[0-9]+", pmids)]
pmids <- pmids[grep("www.ncbi.nlm.nih.gov",pmids)]
pmids <- gsub(".*pubmed/([0-9]+).*", "\\1", pmids)
pmids <- unique(pmids)
pmids <- c("22422453", pmids)


## pmids from the EWAS catalog up to July 2019
pmids <- c(pmids, readLines("ewas-catalog-pmids-20190703.txt"))

## pmids from the journal club from March-Sept 16, 2019
pmids <- c(pmids, readLines("journalclub-20190312-20190916.txt"))

writeLines(unique(pmids), con="pmids.txt")




