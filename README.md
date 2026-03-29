# 🗂️ metadados-brasil

Catálogo estruturado de datasets públicos brasileiros com metadados documentados.

---

## Sobre o projeto

O Brasil possui uma vasta quantidade de dados públicos disponíveis —
mas dispersos, com formatos variados e sem documentação padronizada.

Este projeto nasce de uma pergunta simples:
**e se esses datasets tivessem um catálogo com metadados claros,
organizados e prontos para uso?**

O `metadados-brasil` é um catálogo que reúne datasets de fontes
oficiais brasileiras, documentando cada um com informações essenciais:
origem, formato, frequência de atualização, atributos principais
e possíveis usos analíticos.

---

## O que você encontra aqui

| Arquivo | Descrição |
|---|---|
| `dados/catalogo.csv` | Catálogo principal com os metadados dos datasets |
| `scripts/explorar_catalogo.py` | Script Python para filtrar datasets por tema |
| `docs/fontes.md` | Referências e links das fontes utilizadas |

---

## Datasets catalogados

| Tema | Datasets |
|---|---|
| 🎓 Educação | Censo Escolar, ENEM Microdados |
| 🏥 Saúde | Mortalidade (SIM), CNES |
| 💼 Trabalho | RAIS |
| 🌱 Social | Índice de Desenvolvimento Humano |
| 💰 Economia | Orçamento Federal |
| 🚦 Segurança | Acidentes de Trânsito (PRF) |

---

## Como usar

**Pré-requisitos:** Python 3.8+ e a biblioteca Pandas instalada.
```bash
pip install pandas
```

**Rodando o script:**
```bash
python scripts/explorar_catalogo.py
```

O script vai carregar o catálogo e permitir filtrar datasets por tema.
Exemplo de saída:
```
=== Catálogo de Dados Públicos Brasileiros ===
Total de datasets catalogados: 8

Temas disponíveis: Educação, Saúde, Trabalho, Social, Economia, Segurança

Digite um tema para filtrar: Saúde

2 dataset(s) encontrado(s):

nome                              fonte     descricao
Mortalidade - SIM                 DataSUS   Registros de óbitos no Brasil...
CNES - Estabelecimentos de Saúde  DataSUS   Cadastro nacional de estabelecimentos...
```

---

## Estrutura do projeto
```
metadados-brasil/
│
├── dados/
│   └── catalogo.csv
│
├── scripts/
│   └── explorar_catalogo.py
│
├── docs/
│   └── fontes.md
│
└── README.md
```

---

## Próximos passos

- [ ] Ampliar o catálogo para 20+ datasets
- [ ] Adicionar coluna de qualidade dos dados (completude, atualização)
- [ ] Criar visualização dos datasets por tema e fonte

---

## Sobre a autora

Desenvolvido por **Danielle Mayumi Tamazato Santos**
como parte de um portfólio de transição para a área de dados.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniellemtamazato/)
