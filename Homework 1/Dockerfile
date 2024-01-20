FROM risserlin/bcb420-base-image:winter2024-arm64

# Install pheatmap
RUN install2.r \
    -d TRUE \
    -r "https://cran.rstudio.com" \
    pheatmap

# Install DESeq2
RUN R -e 'BiocManager::install(c("DESeq2"))'