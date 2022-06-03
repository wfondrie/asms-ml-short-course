# Lab 2: Dimensionality Reduction

Dimensionality reduction is often used during the exploratory data analysis (EDA) phase. Understanding the characteristics of your data is the most important part in building a successful machine learning model! The type of model and its hyperparameters are only a secondary aspect.

## Exercise 1: Explore public metabolomics data

[ReDU](https://redu.ucsd.edu/) is a system to annotate public metabolomics data on the [GNPS](https://gnps.ucsd.edu/) repository with metadata information. This metadata captures various relevant pieces of information: from which organism the sample was derived, when and where the data was collected, data acquisition settings, etc.

Public data on GNPS was processed using spectral library searching, and the unique metabolite annotations were used as features. Thus, our data table consists of the unique metabolites in the columns and the file names in the rows, with `1` if the metabolite was detected in that file, and `0` otherwise. Because there are hundreds of thousands of unique metabolites that can be annotated using the GNPS spectral libraries, this data table cannot be visualized directly. Instead, PCA was used to project the data into two or three dimensions for visualization purposes.

Go to the [ReDU website](https://redu.ucsd.edu/) and start the PCA exploration by clicking on "Explore Multivariate Analysis of Public Data". This will bring up an interactive viewer where each dot represents a single mass spectrometry file.

**What can you learn about the chemical similarity of files with ReDU information? Explore the PCA data.**

- Color the files by different metadata categories. Can you find any patterns?
- Rotate the axes to explore subspaces of the data. Compare a two-dimensional plot to a three-dimensional plot. What do you prefer?
- What do the percentages next to the axis labels mean? Are these values good or bad?

## Exercise 2: Compare dimensionality reduction techniques

Which dimensionality reduction technique is best? There is no definitive answer, each techniques has its own assumptions, strengths, and weaknesses.

Here we'll explore the difference between PCA and t-SNE using the MNIST dataset. MNIST is a large database of handwritten digits that is often used as a simple benchmark dataset to evaluate image processing systems.

![MNIST](https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/MnistExamples.png/320px-MnistExamples.png)

Open the [Tensorflow Embedding Projector](https://projector.tensorflow.org/) website. This website provides a browser interface to implementations of a few common embedding algorithms (PCA, t-SNE, UMAP). An _embedding_ is a low-dimensional space into which you can translate high-dimensional vectors. MNIST images are 28x28 pixels, thus they can be represented as 784 dimensional vectors. (Q: How did we get this number?) For visualization purposes, we transform the original 784 dimensional data into embeddings of two or three dimensions.

**Compare the dimensionality reductions achieved by PCA and t-SNE.**

- Select "Mnist with images" in the drop-down menu in the top left corner.
- Choose "label" as the "Color by" value.
- Explore the **PCA embeddings**. Rotate and drag the data projection. Change between two and three dimensions (bottom left). Which digits occur close to each other? Why?
- What does "Total variance described" (bottom left) mean? Why does this value change when you switch between two and three components?
- Is PCA a good embedding? Why (not)?
- Switch to **t-SNE embeddings**. Is there a runtime difference between PCA and t-SNE?
- Observe how the embeddings evolve as t-SNE is trained for multiple generations.
- Do you see unexpected clustering of the data? For example, how does t-SNE group the digit `1`?
- Try different hyperparameters. What are the effects of the perplexity and learning rate hyperparameters?

## Exercise 3 (bonus): Explore t-SNE hyperparameters

The performance of t-SNE can be heavily influenced by its hyperparameters. Additionally, because t-SNE uses a non-deterministic optimization procedure, its results can differ even with the same hyperparameters (unlike for PCA). Suboptimal t-SNE hyperparameters might suggest a data clustering that is not present in the full-dimensional data.

The Distill article ["How to use t-SNE effectively?"](https://distill.pub/2016/misread-tsne/) allows you to interactively explore the effect of different t-SNE hyperparameters on several toy datasets. (The hyperparameter "epsilon" is the same as the "learning rate" in the previous exercise.)

**Play around with t-SNE hyperparameters.**

- Select different datasets and hyperparameter combinations. Let t-SNE run until convergence.
- Re-run t-SNE with unchanged hyperparameters. Is the embedding identical?
- Did you find typical failure cases of t-SNE? What is the influence of the perplexity hyperparameter?
