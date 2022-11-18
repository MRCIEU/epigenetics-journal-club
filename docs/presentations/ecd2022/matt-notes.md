# ECD 2002

## Dirk Schubeler 

"Finding your place: transcription factors as sensors and modifiers of the epigenome"

Lots of lab work to investigate details about transcription factors

- transcription factors are different, some are inibited by or attracted to DNA methylation, chromatin, etc.

- DNA methylation maintenance depends on context, in heterochromatin it tends to be stable, at TF binding sites it may be highly unstable.

## Liran Carmel

"Paleoepigenetics: Using ancient bones to peek into the Neanderthal brain"

Compare DNA methylation in chimps, neanderthal, denisovan and modern human, generally follows evolutionary history.

Genes that affect the voice box are most differently methylated in modern humans among 600 genes that influence anatomy.

3 brain genes differently methylated between modern humans and others, 41 between humans and chimps

## Matthew Van de Pette

"Epigenetic changes induced by environmental exposures"

Focus on imprinted genes because these tend to have stable regulation. Any changes are likely to have functional impact.

Cdkn1c (maternally expressed) and Dlk1 (paternally expressed) targetted with reporting system in mice

Investigated Cdkn1c/Dlk1 expression in offspring whose fathers/mothers had the reporter gene (so reporter silenced)

Observed loss of imprinting (Dlk1) in mice whose mothers were fed a high-fat diet
- loss was progressive during gestation
- correlates with expression

Next generation 
- weaker effect
- highly variable
- only transmitted maternally

Next next generation
- no effect

## Elizabeth Binder

Show that *prior* exposure to glucocorticoids increases *future* transcriptional response

Further examined using cerebral organoids 
- (because rodents don't have the structure and cell types of humans)
- GR expressed at different levels in all organoid cell types
- Glucocorticoid treatment had cell-type specific effects (hundreds of genes per cell type, but only 48 in common)
- One is gene ZBTB16, a GR response transcription factor, contains GR response elements with reduced DNAm after glucocorticoid treatment, one contains a SNP associated with educational attainment, MR PheWAS showed glucocorticoid response element effect associated with a variety of phenotypes related to education
- Another gene, PAX6, is regulated by ZBTB16

However: 
- Not sure what keeps DNAm changes stable after glucocorticoids are no longer present
- Not sure what cases the *future* transcriptional response

## Christophe Kuppe

Spatial and single cell multi-omic analysis of human cardiac disease

- Kuppe et al. Nature 2022
- Infarction has spatial effects on the heart (tissue fibrosis) 
- What causes this?
- Have created a spatial multi-omic heart infarction atlas (snRNA-seq, snATAC-seq)
- Used tissue from heart transplants
- Observed cell count variation across individuals
- Somehow know spatially where each cell came from 
- Used cell2location to determine most likely cell type
- 'cell type niche' - small regions containing 5-6 cells
- characterised niches by cell type composition


## Marie De Borre

Cell-free DNAm analysis enables early preeclampsia prediction

bisulfite treated DNA, captured regions, read depth >= 40

cfDNA predictor performs similarly to maternal characteristics, but are somewhat independent so AUC of the combined predictor increases by about 0.1 (independent dataset)

predictions made in first trimester (I think...)

potentially just detecting placental DNAm

capture regions selected from placenta DNAm analysis

(appears to have presented this previously as a poster in April)

Related:

> Moufarrej, M. N., Vorperian, S. K., Wong, R. J., Campos, A. A., Quaintance, C. C., Sit, R. V., Tan, M., Detweiler, A. M., Mekonen, H., Neff, N. F., Baruch-Gravett, C., Litch, J. A., Druzin, M. L., Winn, V. D., Shaw, G. M., Stevenson, D. K., & Quake, S. R. (2022). Early prediction of preeclampsia in pregnancy with cell-free RNA. Nature, 602(7898), 689–694. https://doi.org/10.1038/s41586-022-04410-z

## Sonia Garcia Calzon

Novel subtypes of type-2 diabetes have been identified

Investigated DNAm differences between subtypes

DNAm scores better than (needs replication) predicted outcomes than clinical predictors


## Maja Jagodic

Multiple sclerosis

**Early on** there are several relapses and remissions and then eventually disability takes over

Most pronounced DNAm differences are in B lymphocytes (compared to cd8, cd4, cd14);
however there are shared changes across cell types

Created consortium investigating factors that predispose for MS development

e.g. investigating mediation of genotype by DNAm to MS
	- currently validating mediation of HLA variants by DNAm in samples from early MS

B cell story suggests EBV infection a factor, known to have big and somewhat similar effects on B cell DNAm

Running cell experiments treating B cells with 'epigenetic drugs'

Epigenome editing by crisper to show effect of increased DNAm on gene expression (decreased DNAm is apparently easier)

Observed off-target effects on expression and variation in the stability of deposited DNA methylation

Conclusions: adaptive immunity involved in MS development, potentially mediated by DNAm in B cells

What determines MS **outcomes**?

SYSF-ZNF638 known to predispose for more severe MS

Disregulation of myeloid cells and phagocytosis 

Difficult to investigate because brain tissue not available to observe progression

## Rama Natarajan

Epigenetics and LncRNAs in diabetic complications and metabolic memory

So far, not much evidence for genetic role in complications, observed recent increases even in young people

'metabolic memory' - long term sustained diabetic complications even after glycemic control 

Investigated mouse model

DCCT/EDIC 30 year trial
- achieving glycemic control massively reduced complications, the sooner the better
- profiled histone modifications and DNAm at two times 17 years apart 
- several sites showed persistant DNAm differences in white blood cells (TXNIP 3'UTR)
- follow-up study (n=500) identifies 186 sites associated with HbA1c
- HbA1c associated with complications, appears to be mediated by some of the DNAm sites including some at TXNIP

Long non-coding RNAs
- DRAIR is down-regulated in monocytes from type 2 diabetes
- applied assays to determine where DRAIR interacts with chromatin and what proteins DRAIR interacts with
- several papers from 2017-2022 present the results ...

Translational potential 
- found a microRNA knockout mouse that is protected from diabetic kidney disease, etc. 
- *too fast to take notes!*

## Renata Jurkowska

Epigenetic profiling across disease stages identifies novel regulators of COPD phenotypes

Lung tissue samples, three cell types: fibroblasts, BC, AT2, n=11

Epigenetic changes appear early in COPD

Targetted DNAm decrease of INS activates the gene

## Hannah Maude

The epigenome of liver sinusoidal ...

## Martin Hirst

IHEC oversees
- Blueprint
- EpiAtlas is the latest effort

RNA-seq
WGBS
Chip-seq of histone modifications

Standardizing experimental workflows

Standardizing analytical pipelines
- using Singularity  http://github.com/IHEC
- quality metrics - can compare your metric to those in IHEC data

Epigenomic Reference Registry (EpiRR)
- only searchable repository for human epigenomic datasets
- standardized metadata framework and validator to facilitate community submissions
- Peter Harrison and Garth Ilsley
- plan is to open it up to the community for reuse

Gaps in protected data sharing
- datasets are in dbgap -- which takes a long time to get permission
- downloading 1000s of datasets requires a concerted long-term effort over years!

Findings
- cell lines do not recapitulate patterns in primary tissues
- Use a Bayesian hierarchical model to calculate probabilistic epigenomic profiles
  that summarizes the epigenomes of multiple individuals (Steif et al. unpublished) 
  -- useful to get an idea where 'normal' epigenomes vary
- breast cancer example 

Future
- more tissues/cell types
- computational tools
- more reanalyses

*Funders aren't generally interested in building Singularity objects and reanalysing dbGap datasets without a dominanting scentific hypothesis.  What is your secret?!*

Answer: move to Canada a few years ago

## Andrew Teschendorff

EpiSCORE for estimating cell type fraction in solid-state tumours

Hierarchical EpiDISH

Barnett JE et al. Nat Commun 2022
- DNAm from blood, buccal, cervical smears from 300 women
- conclusion: large inter-individual variation in cell-type composition of tissues ("healthy variation")

Reference-based inference is very robust to noise in the DNAm reference matrix (25% errors)

But, reference data is often not available

Hence, EpiSCORE -- deconvolution of bulk-tissue DNA methylation from single-cell RNA-seq data 
- based on hypothesis that gene expression differences between tissues 
  are almost always driven by promoter DNA methylation 

EpiSCORE DNAm atlas
- Zhu et al Nat Methods 2022
- github.com/aet21/EpiSCORE
- validation of the atlas
  - compare to tumour purity in TCGA
  - snmC-seq2 data available in brain
  - accuracy 74%-82% in Kaplan's DNAm-Atlas

Kaplan's DNAm-Atlas 
 - manuscript https://www.biorxiv.org/content/10.1101/2022.01.24.477547v1
 - whole-genome bisulfite sequenced at 30X depth
 - "39 cell types sorted from 207 healthy tissue samples"

Applications
- molecular classification of olfactory neuroblastoma
- episcore reveals misdiagnosed pancreatic cancer cases 
  (correctly identifies them as neuroendocrine tumours)
- identified smoking-associations in saliva DNAm specific to immune cells and epithelial cells
- did something with episcore + celldmc
- mitotic epigenetic clocks with cell-type specific correlations

Have done some validation of human-based EpiSCORE in animal data

## Christine Hansen

Detecting rare epigenetic dysregulation in common psychiatric disorder

Outlier methylation region: a DMR but where one sample is an outlier 
- Could be defined as outside 95% CI.  Is this correct/best? 
- How to identify regions? - something like comb-p to combine z-scores from individual compared to everyone else
- method available on gitlab 

Applied in 
- three DNAm schizophrenia datasets (from GEO)
- 4 iPSYCH datasets from neonatal blood

Did any gene have OMR overrepresentation?
- GFI1 identified for schizophrenia

*Couldn't you use this as a biomarker of disease risk, diagnosis, outcome, etc.?*

*Likely enriched for true biological variation compared to single-site outlier analyses.*

*Seems like dmrff could be used for this*

## Elad Segev

Epigenetic aging waves, switch points in DNA

Only **nine** genes are responsible for the majority of accelerated aging

DNAm at many sites does not change linearly with time

Dickey-Fuller stationary test used to remove sites that don't change with age (mean or variance)

Modelling changes with age
- pieces regression results in many errors
- first derivative sigmoid fitting analysis (seemed better)

Results (in approx 2000 samples)
- 5000 sites with 'switch point', 4000 in common between men and women
- switch points cluster at 3 different ages
- published on biorxiv https://www.biorxiv.org/content/10.1101/2022.10.02.510495v1

## Jacob Bergstedt
The immune factors driving DNA methylation variation in human blood

(extended) IDOL cell composition estimates
- Salas et al PMID 35140201
- includes CD4 and CD8 T cell subsets

Adjusting for only 6 cell types in blood leaves a lot of remaining cell count effects
e.g. for age: 35701 associations when adjusting for 16 cell types, 118885 when adjusting for 6
e.g. 88K associations with CMV mediated by cell composition 

However, little effect on sex and smoking associations.

189 sites associated with CMV after more complete adjustment
most of them are binding sites for a single transcription factor BRD4

## Nora Franceschini

Epigenetics and human genetic diversity

Disease burden varies across populations due to
- genetics
- group exposures - pollution
- individual exposures - lifestyle

Chronic kidney disease 
- most common causes: diabetes and hypertension
- estimated glomerular filtration rate 

EWAS (n=5428) of differences between
- african americans
- european americans
- hispanic/latinos

13 DMPs replicated in 8109 EA and AA

Overrepresentation in kidney-specific gene regions

Major problem: reference datasets are almost entirely based on Europeans, 
including immortalised cell lines.
This could reduce ability to correctly interpret findings in non-Europeans, 
especially related to diseases are more rare in Europeans 
than in certain non-European groups.

## Løkås Haftorn

Nucleated red blood cells explain most of the association between DNA methylation and gestational ageKristine 

Data
- data Moba cord blood DNAm (n=953)
- reference-based cell count estimates

Methods
- Conventional EWAS
- CellDMC (uses interaction terms with cell counts to estimate cell-type specific effects)

CellDMC finds 231 associations (80% of all) in nucleated red blood cell (nRBC) DNAm
Replicated in another dataset

nRBCs disappear disappear within a few days of birth

May explain why peripheral blood collected after birth is weakly associated with gestational age

## Lucy Sinke

Circulating interleukin-6 levels are associated with DNA methylation in regulatory regions of key inflammatory genes

- EWAS meta-analysis of 4361 samples (whole blood)
- EWAS of 994 samples (CD4+ T cells) 

## Rong Fan

Spatial Epigenome Sequencing

Sheeeeeeeeeeeeit! 

## Ariel Gershman

The first complete human genome and epigenome

Used CHM13 cell line - had two copies of the paternal genome rather than maternal and paternal
- Added 182 Mbp of new sequence, removed 1.2 Mbp of falsely duplicated sequence
- Annote 2226 new genes, of which 115 protein coding

Novel mapping technique (to use short-read sequencing for repetitive DNA)
- Identify unique 95mer sequences 
- However, some regions have no unique 95mers

Solution: Nanopore long-read sequencing

Results

- because no amplification, removes GC-bias from data
- 3 million more CpG sites can be measured (vs short-read WGBS)
- **used M.CviPI methyltransferase to decorate accessible chromatin with exogenous GpC methylation, this allowed detection of DNAm and DNA accessibility on the same read**
- identified gene regions with identical repetitive DNA sequence but different epigenetic state

April 2022 edition of Science
https://pubmed.ncbi.nlm.nih.gov/35357917/
https://pubmed.ncbi.nlm.nih.gov/35357915/
https://pubmed.ncbi.nlm.nih.gov/35357925/
https://pubmed.ncbi.nlm.nih.gov/35357911/
https://pubmed.ncbi.nlm.nih.gov/33230324/

In the discussion stages to generate data for samples from a human population rather than from cell lines.

## Duncan Sproul

Single molecule analysis of DNA methylation in long reads

https://www.biorxiv.org/content/10.1101/2022.11.15.516549v1

Nanopore sequencing data derived from GM24385 lymphoblastoid cells. 

This consisted of 6,289,480 reads aligned to autosomes with a mean length of 24.6kb

In heterochromatin, DNAm correlation between sites oscillate at 180bp -- seems due to nucleosomes

## Sarah Marzi

Mouse model of Alzheimers disease

Most genetic risk seems to be mediated by microglia, APOE appears central

APOE chimeric mouse model 



