library(readxl)
ewas <- read_xlsx("candidates.xlsx", sheet="ewas")
ewas <- sapply(unique(ewas$group), function(group) {
	ewas[which(ewas$group == group),]
}, simplify=F)

library(knitr)
options(knitr.kable.NA = '')
for (group in names(ewas)) {
	print(kable(ewas[[group]][,c("variable","tissue","n","assocs","notes","pmid","journal")]))
}