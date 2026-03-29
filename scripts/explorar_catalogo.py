import pandas as pd

# Carregar o catálogo
df = pd.read_csv("dados/catalogo.csv", encoding="utf-8")

# Visualizar todos os datasets
print("=== Catálogo de Dados Públicos Brasileiros ===")
print(f"\nTotal de datasets catalogados: {len(df)}\n")

# Listar temas disponíveis
temas = df["temas"].unique().tolist()
print("Temas disponíveis:")
for tema in temas:
    print(f"  • {tema}")

# Filtrar por tema
tema_escolhido = input("Digite um tema para filtrar (ou ENTER para ver todos): ")

# Se o usuário só apertar ENTER, mostra o catálogo completo
if tema_escolhido.strip() == "":
    resultado = df
else:
    resultado = df[df["temas"].str.contains(tema_escolhido, case=False, na=False)]

# Exibir resultado
print("\n" + "=" * 55)

if resultado.empty:
    print(f"Nenhum dataset encontrado para '{tema_escolhido}'.")
    print("Tente um dos temas listados acima.")
else:
    print(f"{len(resultado)} dataset(s) encontrado(s):\n")

    resultado_exibir = resultado[
        ["nome", "fonte", "temas", "formato", "atualizacao", "descricao"]
    ].reset_index(drop=True)

    for i, row in resultado_exibir.iterrows():
        print(f"[{i+1}] {row['nome']}")
        print(f"     Fonte:       {row['fonte']}")
        print(f"     Tema:        {row['temas']}")
        print(f"     Formato:     {row['formato']}")
        print(f"     Atualização: {row['atualizacao']}")
        print(f"     Descrição:   {row['descricao']}")
        print()

print(" === Acesse os links completos em dados/catalogo.csv ===")
