# information-extraction-the-extraction-squad
information-extraction-the-extraction-squad created by GitHub Classroom
In the following repository, we have made available the primary CSV file containing topics extracted from the LLAMA 2 model, as well as the CSV-formatted base model utilizing ChatGPT. 
Furthermore, the repository encompasses the source code for topic modeling, which can be executed in a Google Colab environment, for both the LLAMA 2 and ChatGPT models.

Subsequent to an exhaustive examination, we have ascertained that the most suitable model for clustering purposes is the Affinity Propagation algorithm. Additionally, we have identified the optimal number of dimensions for effective clustering, denoted as 'n_components=100'. 
Given the substantial dimensionality of our dataset, we have determined that the Jaccard index metric outperforms the cosine similarity metric in terms of model fitness.

To substantiate our findings, we have included multiple graphical representations as empirical evidence. Furthermore, our hierarchical clustering analysis has yielded two noteworthy conclusions: 
firstly, the ability to generate a set of generalized clusters, totaling approximately 5 to 10 clusters; and secondly, the capability to generate more specific, precise clusters, which amount to 146 distinct clusters.
