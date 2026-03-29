import pandas as pd

# Carregar o catálogo
df = pd.read_csv("dados/catalogo.csv")

# Visualizar todos os datasets
print("=== Catálogo de Dados Públicos Brasileiros ===")
print(f"Total de datasets catalogados: {len(df)}\n")

# Listar temas disponíveis
print("Temas disponíveis:")
print(df["temas"].unique())

# Filtrar por tema
tema_escolhido = input("\nDigite um tema para filtrar: ")
resultado = df[df["temas"].str.contains(tema_escolhido, case=False, na=False)]

if resultado.empty:
    print("Nenhum dataset encontrado para esse tema.")
else:
    print(f"\n{len(resultado)} dataset(s) encontrado(s):\n")
    print(resultado[["nome", "fonte", "descricao", "url"]].to_string(index=False))