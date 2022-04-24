library(org.Hs.eg.db)

get_entrez_id = function(symbols){
  gene2entrez <- as.data.frame(mapIds(org.Hs.eg.db, symbols, keytype="SYMBOL", column="ENTREZID", multiVals="first"))
  df <- data.frame(gene2entrez) %>% rownames_to_column("Symbol")
  colnames(df) <- c("Symbol", "Entrenz")
  df$Entrenz <- paste0("Gene_", df$Entrenz)
  return(df)
}


####
geneset = "fibrinogen_genes"
#genes = union(m1m2_genes,union(collagen_genes, union(fibrinogen_genes, union(muscle_regeneration_genes, neural_regeneration_genes))))
genes = rownames(init$norm_tpms)

outputPath = paste0("Output/GeneLists/","all")
dir.create(outputPath, recursive = TRUE)

entrenz_ids = get_entrez_id(genes)

entrenz_ids = paste0("Gene_",entrenz_ids)

write.xlsx(entrenz_ids, file = file.path(outputPath, 
                                      "mapping.xlsx"), 
           append = FALSE, row.names = FALSE)
