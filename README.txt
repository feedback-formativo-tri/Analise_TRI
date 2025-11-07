BIBLIOTECAS NECESSÁRIAS - PYTHON
pandas
chardet
numpy
matplotlib
reportlab
plotly

PACOTES NECESSÁRIOS - R
dplyr
eRm
ltm


pre-processamento/Itens_prova_geral_2022.ipynb
- Função: extrair as provas usadas na análise do banco de dados do ENEM e salvá-las nas pastas Itens_provas_amarela e Itens_prova_azul
- Execução: sendo um notebook, pode executar todas as células após instalar as bibliotecas necessárias (pandas e chardet)


pre-processamento/tratamento_geracao_matriz_binaria.ipynb
- Função: extrair as provas salvas nas pastas Itens_provas_amarela e Itens_prova_azul e criar as matrizes binárias, salvando-as na pasta matrizes_binarias
- Execução: sendo um notebook, pode executar todas as células após instalar as bibliotecas necessárias (pandas, numpy e chardet)

codigos_R/ERM/erm_1PL.R
- Função: extrair as matrizes binárias, transformá-las em objetos ERM, pegar os parâmetros habilidade e dificuldade e salvá-los.
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (eRm e dplyr)

codigos_R/ERM/probabilidade_ERM_1PL.R
- Função: extrair os parâmetros salvos, calcular a probabilidade de acerto com base neles e salvá-la na pasta 'probabilidades'
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (dplyr)

codigos_R/ERM/gera_graficos.py
- Função: extrair o csv de probabilidades para gerar CCI's
- Execução: ir até a pasta do arquivo e executar após instalar as bibliotecas necessárias (plotly e pandas)

codigos_R/LTM_2PL/ltm_2PL.Rmd
- Função: extrair as matrizes binárias, transformá-las em objetos ltm, pegar os parâmetros habilidade, dificuldade e discriminação e salvá-los.
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (ltm e dplyr)

codigos_R/LTM_2PL/probabilidade_LTM_2PL.Rmd
- Função: extrair os parâmetros salvos, calcular a probabilidade de acerto com base neles e salvá-la na pasta 'probabilidades'
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (dplyr)

codigos_R/LTM_2PL/gera_graficos.py
- Função: extrair o csv de probabilidades para gerar CCI's
- Execução: ir até a pasta do arquivo e executar após instalar as bibliotecas necessárias (plotly e pandas)

codigos_R/LTM_3PL/ltm_3PL.Rmd
- Função: extrair as matrizes binárias, transformá-las em objetos ltm, pegar os parâmetros habilidade, dificuldade, discriminação e acerto ao acaso e salvá-los.
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (ltm e dplyr)

codigos_R/LTM_3PL/probabilidade_LTM_3PL.Rmd
- Função: extrair os parâmetros salvos, calcular a probabilidade de acerto com base neles e salvá-la na pasta 'probabilidades'
- Execução: sendo um arquivo Rmd, pode executar as células após instalar os pacotes necessários (dplyr)

codigos_R/LTM_3PL/gera_graficos.py
- Função: extrair o csv de probabilidades para gerar CCI's
- Execução: ir até a pasta do arquivo e executar após instalar as bibliotecas necessárias (plotly e pandas)

report/create_report.py
- Função: extrair todas as informações geradas ao longo do processo sobre o examinando e as questões para gerar um relatório com base em um aluno e uma questão
- Execução: ir ao diretório do arquivo e executar "python create_report.py" após instalar as bibliotecas neccessárias (pandas, numpy, plotly, reportlab)