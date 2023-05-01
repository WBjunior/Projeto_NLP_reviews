# Análise de Sentimentos de Reviews de Kindles da Amazon Utilizando SVM+BOW, SVM+EMBEDDING e BERT

Este projeto tem como objetivo realizar a análise de sentimentos em reviews de Kindles da Amazon, utilizando diferentes abordagens de processamento de linguagem natural (NLP).

Para isso, foram utilizados três modelos de aprendizado de máquina diferentes: SVM+BOW, SVM+EMBEDDING e BERT. O SVM (Support Vector Machine) é um algoritmo de aprendizado de máquina que pode ser utilizado tanto para classificação quanto para regressão. O BOW (Bag-of-Words) é uma técnica simples de representação de texto que considera a frequência das palavras em um documento. O EMBEDDING é uma técnica mais avançada de representação de texto, que permite capturar o contexto semântico das palavras em um texto. Já o BERT (Bidirectional Encoder Representations from Transformers) é um modelo pré-treinado de linguagem natural que permite realizar tarefas de NLP, como a análise de sentimentos, com alta precisão.

Os dados utilizados neste projeto consistem em reviews de Kindles da Amazon, coletados a partir da biblioteca Selenium. O conjunto de dados é composto por cerca de 3344 reviews, classificados entre 1 e 5 estrelas.

O projeto foi desenvolvido utilizando a linguagem Python e as bibliotecas NLP, TensorFlow e Sckit-learn. Foram realizadas as seguintes etapas:

Pré-processamento dos dados: remoção de caracteres especiais, números e stopwords; stemming e lematização das palavras.
Representação dos dados: para o modelo SVM+BOW, foi utilizada a técnica de Bag-of-Words para representar os dados; para o modelo SVM+EMBEDDING, foi utilizado o algoritmo Word2Vec para criar embeddings das palavras; para o modelo BERT, foi utilizada a técnica de fine-tuning para treinar o modelo com os dados de treinamento.
Treinamento dos modelos: os modelos foram treinados utilizando os dados de treinamento e avaliados utilizando os dados de teste.
Avaliação dos modelos: a acurácia, precisão, recall e F1-score foram utilizados como métricas de avaliação dos modelos.
Os resultados obtidos mostraram que o modelo SVM+BOW obteve a melhor performance, com uma acurácia de 0,88 e um F1-score de 0,88. O modelo SVM+EMBEDDING obteve uma performance intermediária, com uma acurácia de 0,78 e um F1-score de 0,80. Já o modelo BERT obteve a pior performance, com uma acurácia de 0,64 e um F1-score de 0,77.

# Requiriments
> pip install selenium

> pip install transformers

> pip install scikit-learn

> pip install spacy==3.5

> pip install tensorflow

> pip install numpy 

> pip install pandas

> pip install gensim

> pip install nltk

> pip install matplotlib


