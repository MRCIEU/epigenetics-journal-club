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
cols <- c("pmid", "journal", "variable", "tissue", "population", "results")
types <- sort(unique(ewas$type))
groups <- sort(unique(ewas$group))
is.first <- T
for (group in groups) {
  for (type in types) {
    rows <- which(ewas$type==type & ewas$group==group)
    if (length(rows) > 0) {
      if (!is.first)
        writeLines("\n\n---\n\n")
      is.first <- F
      writeLines(c(
        paste("\n## EWAS of", type, "in", group,"\n"),
        ".striped[",
        kable(ewas[rows,cols], row.names=F),
        "]"))
    }
  }
}


