# 📊 Estudo de Estatística Aplicada com Python e Pandas

Este repositório contém estudos e exercícios práticos de **Estatística** aplicados com **Python**. O foco é a **Análise de Dados**, criação de **gráficos informativos** e interpretação robusta de informações utilizando bibliotecas essenciais do ecossistema de **Data Science**.

O objetivo principal é consolidar conceitos estatísticos e aplicar técnicas modernas de **Análise Exploratória de Dados (EDA)** em projetos reais, preparando você para desafios complexos de Data Science.

---

## 🔧 Tecnologias Utilizadas

| Tecnologia       | Função Principal                                                  |
|------------------|-------------------------------------------------------------------|
| Python 3.11      | Linguagem de programação principal.                               |
| Pandas           | Manipulação, limpeza e análise de dados (DataFrames).             |
| NumPy            | Operações matemáticas avançadas e arrays de alto desempenho.      |
| Matplotlib       | Criação de gráficos e visualização estática de dados.             |
| Jupyter Notebook | Ambiente interativo para experimentação, documentação e Visualização de resultados.                        |
| pyenv            | Gerenciamento de múltiplas versões do Python.                     |
| pipenv           | Gerenciamento de ambientes virtuais e dependências do projeto.    |

---

## 📚 Tópicos de Estudo em Estatística

- **Estatística Descritiva**: cálculo e interpretação de métricas centrais (média, mediana, moda) e de dispersão (desvio padrão, variância, quartis).  
- **Análise Exploratória de Dados (EDA)**: técnicas para inspecionar e resumir os principais recursos de um dataset utilizando Pandas.  
- **Visualização de Dados**: criação de gráficos informativos (histogramas, box plots, scatter plots) com Matplotlib para identificar padrões e outliers.  
- **Manipulação de Datasets Reais**: trabalho prático com dados reais para simular cenários de mercado.  
- **Conceitos Teóricos**: aplicação prática de conceitos de probabilidade e estudo de distribuições estatísticas.

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, instale:

- **Git** (opcional, mas recomendado para clonar o repositório)  
- **pyenv** (para gerenciar a versão correta do Python)  
- **pipenv** (para isolar e gerenciar as dependências do projeto)  

---

## 🚀 Guia de Configuração e Execução

### 1️⃣ Clonar o Repositório (Opcional)

```
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```
### 2️⃣ Instalar e Configurar Python 3.11 com pyenv

```
# Instalar Python 3.11 (caso ainda não esteja instalado)
pyenv install 3.11.0

# Definir Python 3.11 como versão local do projeto
pyenv local 3.11.0
```
Isso criará um arquivo .python-version no diretório, garantindo que o pipenv utilize esta versão.

### 3️⃣ Criar e Ativar o Ambiente Virtual com pipenv

```
# Criar ambiente virtual usando Python 3.11
pipenv --python 3.11

# Ativar o ambiente virtual
pipenv shell
```

### 4️⃣ Instalar Dependências

```
pipenv install pandas numpy matplotlib jupyter
```

### 5️⃣ Executar o Jupyter Notebook

```
pipenv run jupyter notebook
```

Isso abrirá a interface do Jupyter no navegador. Navegue até a pasta notebooks/ para explorar os estudos.

## 📂 Estrutura do Repositório

| Diretório/Arquivo  | Descrição                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `notebooks/`       | Contém todos os arquivos `.ipynb` com estudos e exercícios.               |
| `data/`            | Armazena arquivos de dados (CSV, Excel, etc.) utilizados nas análises.    |
| `README.md`        | Este arquivo de documentação.                                             |
| `Pipfile`          | Define as dependências do projeto.                                        |
| `Pipfile.lock`     | Garante a reprodutibilidade das versões das dependências.                 |
| `.python-version`  | Define a versão local do Python (3.11.0).                                 |

---

## 💡 Dicas e Comandos Úteis

| Comando                      | Descrição                                                      |
|------------------------------|----------------------------------------------------------------|
| `pipenv shell`               | Entrar no ambiente virtual antes de trabalhar.                 |
| `exit`                       | Sair do ambiente virtual do pipenv.                            |
| `pipenv update`              | Atualizar todas as dependências do Pipfile.                    |
| `pipenv install <pacote>`    | Instalar um novo pacote no ambiente virtual.                   |
| `pipenv install --dev`       | Instalar dependências de desenvolvimento em outro computador.  |

---

## 🤝 Contribuições

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir issues ou pull requests.
Caso contrário, este repositório pode ser utilizado como estudo pessoal.
