# Projeto de Análise TRI (Teoria da Resposta ao Item)

## 📦 Bibliotecas necessárias

### 🐍 Python
- pandas  
- chardet  
- numpy  
- matplotlib  
- reportlab  
- plotly 
- Ollama 

### 📊 R
- dplyr  
- eRm  
- ltm

## Modelo necessário
- É necessário instalar o `deepseek-r1:14b` pelo `Ollama` para que a geração de relatórios com `Deepseek` funcione

---

## 🗂️ Estrutura e Funções dos Arquivos

### **pre-processamento/Itens_prova_geral_2022.ipynb**
- **Função:** Extrair as provas usadas na análise do banco ENEM e salvar nas pastas `Itens_provas_amarela` e `Itens_provas_azul`
- **Execução:** Notebook — basta executar todas as células após instalar `pandas` e `chardet`. Executar cada célula do ipynb

---

### **pre-processamento/tratamento_geracao_matriz_binaria.ipynb**
- **Função:** Ler itens das pastas `Itens_provas_amarela` e `Itens_provas_azul` e gerar matrizes binárias em `pre-processamento\matrizes_binarias`
- **Execução:** Notebook — executar após instalar `pandas`, `numpy` e `chardet`. Executar cada célula do ipynb

---

### **codigos_R/ERM/erm_1PL.R**
- **Função:** Carregar matrizes binárias, transformá-las em objetos ERM, extrair parâmetros de habilidade e dificuldade e salvar os resultados
- **Execução:** Arquivo Rmd — executar células após instalar `eRm` e `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/ERM/probabilidade_ERM_1PL.R**
- **Função:** Calcular a probabilidade de acerto com base nos parâmetros gerados e salvar na pasta `codigos_R\ERM\probabilidades`
- **Execução:** Arquivo Rmd — executar após instalar `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/ERM/gera_graficos.py**
- **Função:** Ler o CSV de probabilidades e gerar curvas características do item (CCI)
- **Execução:** Rodar após instalar `pandas` e `plotly`
```bash
cd codigos_R/ERM
python gera_graficos.py
```

---

### **codigos_R/LTM_2PL/ltm_2PL.Rmd**
- **Função:** Transformar matrizes binárias em objetos `ltm`, extrair habilidade, dificuldade e discriminação e salvar resultados
- **Execução:** Arquivo Rmd — instalar `ltm` e `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/LTM_2PL/probabilidade_LTM_2PL.Rmd**
- **Função:** Calcular probabilidade de acerto e salvar em `codigos_R\LTM_2PL\probabilidades`
- **Execução:** Arquivo Rmd — instalar `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/LTM_2PL/gera_graficos.py**
- **Função:** Gerar CCI baseado no CSV de probabilidades
- **Execução:** Rodar após instalar `pandas` e `plotly`
```bash
cd codigos_R/LTM_2PL
python gera_graficos.py
```

---

### **codigos_R/LTM_3PL/ltm_3PL.Rmd**
- **Função:** Transformar matrizes em objetos `ltm`, extrair habilidade, dificuldade, discriminação e acerto ao acaso e salvar resultados
- **Execução:** Arquivo Rmd — instalar `ltm` e `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/LTM_3PL/probabilidade_LTM_3PL.Rmd**
- **Função:** Calcular probabilidade de acerto e salvar na pasta `codigos_R\LTM_3PL\probabilidades`
- **Execução:** Arquivo Rmd — instalar `dplyr`. Executar cada célula do Rmd

---

### **codigos_R/LTM_3PL/gera_graficos.py**
- **Função:** Gerar curvas CCI a partir dos CSVs de probabilidades
- **Execução:** Rodar após instalar `pandas` e `plotly`
```bash
cd codigos_R/LTM_3PL
python gera_graficos.py
```

---

### **report/normalize_data.py**
- **Função:** Pega dados das pastas `codigos_R\LTM_3PL\dificuldades\` e `codigos_R\LTM_3PL\habilidades\` e os normaliza, salvando os novos dados na pasta `report\normalized_data\dificuldades\` e `report\normalized_data\habilidades\`.
- **Execução:** Rodar após instalar `pandas` e `numpy`
```bash
cd report
python normalize_data.py
```

---

### **report/create_pdf_report.py**
- **Função:** Carregar resultados gerados (examinando + questões) e gerar relatório final em formato pdf (sem uso de llms) para um aluno e uma questão, salvando-o em `report\report_pdf`
- **Execução:** Rodar após instalar `pandas`, `numpy`, `plotly` e `reportlab`
```bash
cd report
python create_report.py
```

---

### **report/pdf_report_prof**
- **Função:** Criar um relatório geral do estado para o professor em formato pdf (sem uso de llms) e o salva em `report\report_pdf`
- **Execução:** Rodar após instalar `pandas`, `numpy`, `plotly` e `reportlab`
```bash
cd report
python pdf_report_prof.py
```

---

### **report/report_deepseek/gera_relatorio_aluno.py**
- **Função:** Gerar relatório com o `Deepseek` via `Ollama` para o desempenho de um aluno em uma questão
- **Execução:** Rodar após instalar `ollama`, `pandas`, `numpy` e `plotly`
```bash
cd report/report_deepseek
python gera_relatorio_aluno.py
```
- **Alerta:** Devido ao uso do Deepseek localmente, esta execução pode demorar um pouco

---

### **report/report_deepseek/gera_relatorio_prof.py**
- **Função:** Gerar relatório com o `Deepseek` via `Ollama` para a qualidade de uma questão
- **Execução:** Rodar após instalar `ollama`, `pandas`, `numpy` e `plotly`
```bash
cd report/report_deepseek
python gera_relatorio_prof.py
```
- **Alerta:** Devido ao uso do Deepseek localmente, esta execução pode demorar um pouco

---

