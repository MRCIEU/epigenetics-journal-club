gene <- readLines("current-vs-never-genes.txt")
meth <- read.table("27651444_smoking_current_vs_never_smoking.tsv",sep="\t",header=T)
length(unique(meth$gene))
#[1] 4196
length(unique(gene))
#[1] 670
length(intersect(toupper(gene), toupper(meth$gene)))
#[1] 204
meth[1,]
#      author consortium     pmid       date   trait                                   efo                 analysis   source         outcome
#1 Joehanes R         NA 27651444 2016-10-01 Smoking EFO_0006527, EFO_0005671, EFO_0004318 Current vs never smoking Table S2 DNA methylation
#                      exposure                        covariates outcome_unit exposure_unit                        array                  tissue further_details    n
#1 Current versus never smoking Age, sex, cell composition, batch  Beta values            NA Illumina HumanMethylation450 CD4+ T cells, monocytes              NA 9389
#  n_studies    age  sex         ethnicity        cpg        chrpos chr      pos   gene        type   beta    se       p details
#1        16 Adults Both European, African cg16145216 chr1:42385662   1 42385662 HIVEP3 South shore 0.0298 0.002 6.7e-48       -
#                                   study_id
#1 27651444_smoking_current_vs_never_smoking
meth <- meth[which(meth$p < 1e-7),]
length(unique(meth$gene))
#[1] 1406
length(intersect(toupper(gene), toupper(meth$gene)))
#[1] 81
fisher.test(cbind(c(20000, 1406),c(670, 81)), alternative="greater")
#
#	Fisher's Exact Test for Count Data
#
#data:  cbind(c(20000, 1406), c(670, 81))
#p-value = 1.57e-05
#alternative hypothesis: true odds ratio is greater than 1
#95 percent confidence interval:
# 1.394687      Inf
#sample estimates:
#odds ratio 
#  1.719652 