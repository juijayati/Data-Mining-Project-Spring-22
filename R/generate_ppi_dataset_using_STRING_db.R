library(data.table)
library(dplyr)
library(STRINGdb)



gene_df = read.table("mapped_symbols.txt")
colnames(gene_df) = "gene"

string_db <- STRINGdb$new( version="11", species=9606,score_threshold=200, input_directory="")

mapping <-  string_db$map( gene_df, "gene", removeUnmappedRows = TRUE )

interactions <- string_db$get_interactions(mapping$STRING_id)

interactions <- interactions %>% filter(combined_score > 700)

inds <- interactions %>% duplicated()
interactions <- interactions[inds,]

from_df <- mapping %>% rename(from_gene = gene, from = STRING_id)
interactions <- interactions %>% inner_join(from_df, by = "from")

to_df <- mapping %>% rename(to_gene = gene, to = STRING_id)
interactions <- interactions %>% inner_join(to_df, by = "to")

interactions <- interactions %>% select(from_gene, to_gene, combined_score) %>% rename(from = from_gene, to = to_gene)
interactions$label <- "True"

genes <- union(interactions$from, interactions$to)

set.seed(1234)

for(gene in genes){
  df <- interactions %>% filter(from == gene)
  non_rel_genes <- setdiff(genes, df$to)
  samp_genes <- sample(non_rel_genes, 16)
  newdf <- data.frame(from = gene, to = samp_genes, combined_score = 0, label = "False")
  interactions <- rbind(interactions, newdf)
}

write.table(interactions, "PPI.tsv",row.names = FALSE, quote = FALSE, sep = "\t")
