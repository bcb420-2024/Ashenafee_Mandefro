from typing import List

import pandas as pd


class GeneOntologyTerm:
    def __init__(self, go_id: str, description: str):
        self.go_id = go_id
        self.description = description
    
    def __str__(self):
        return f'{self.go_id} - {self.description}'


def get_go_ids_for_gene(gene: str, gemfile: str) -> List[GeneOntologyTerm]:
    """
    Get the Gene Ontology (GO) terms for a given gene from a GEM file.

    Parameters:
    gene (str): The gene name or identifier.
    gemfile (str): The file path to the GEM file.

    Returns:
    List[GeneOntologyTerm]: A list of GeneOntologyTerm objects.
    """
    df = pd.read_csv(gemfile, sep='\t')
    filtered_df = df[df['Genes'].str.contains(gene)]

    go_terms = []
    for _, row in filtered_df.iterrows():
        go_terms.append(GeneOntologyTerm(row['GO.ID'], row['Description']))

    return go_terms


if __name__ == '__main__':
    gemfile = 'gProfiler_hsapiens_3-7-2024_6-54-20 PM.gem.txt'
    gene = 'TFEC'
    go_terms = get_go_ids_for_gene(gene, gemfile)
    for term in go_terms:
        print(term)