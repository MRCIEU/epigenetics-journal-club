#---- logo -----------------------------

writeLines(
'&nbsp; &nbsp;
 <img src="bristol-logo.png" style="width: 200px"></img>
 <img src="ieu-logo.png" style="width: 200px"></img>')

#---- papers -----------------------------

if (!require("journalclub"))
  remotes::install_github("perishky/journalclub")
library(journalclub) 
candidates <- read.csv("candidates.csv")
papers <- journalclub.annotate(candidates$pmid, abstract=F)
rownames(papers) <- papers$pmid
papers$authors <- sapply(strsplit(papers$authorlist, ","), function(authors) {
  if (length(authors) <= 5) paste(authors, collapse=", ")
  else paste(head(authors,1), "...", tail(authors,1))
})
papers$doi <- sub(".*doi: ","", papers$elocationid)
papers$cite <- with(papers, paste0(
  authors, ". ",
  "**", title, "** ", 
  "*", source, "* ", 
  ". doi: [", doi, "](http://doi.org/", doi, ")"))

#---- ewas -----------------------------

ewas <- read.csv("ewas.csv")
cols <- c("pmid", "journal", "variable", "tissue", "population", "result")
types <- unique(ewas$type)
for (type in types) {
  writeLines(c(
    paste("## EWAS of", type),
    ".striped[",
    kable(ewas[ewas$type==type,cols], row.names=F),
    "]"))
  if (type != tail(types,1))
    writeLines("---")
}


