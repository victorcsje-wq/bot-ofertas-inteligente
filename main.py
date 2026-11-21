import requests

API = "https://api.mercadolibre.com/sites/MLB/search"

PESQUISAS = [
    "smartphone",
    "notebook",
    "fone bluetooth",
    "smart tv",
    "mouse gamer",
    "monitor"
]

def buscar_ofertas():

    total = 0

    for pesquisa in PESQUISAS:

        print(f"\n🔎 PESQUISANDO: {pesquisa}")

        try:
            resposta = requests.get(
                API,
                params={"q": pesquisa, "limit": 10},
                timeout=30
            )

            resposta.raise_for_status()

            produtos = resposta.json().get("results", [])

            print(f"Produtos encontrados: {len(produtos)}")

            for produto in produtos[:5]:

                total += 1

                print("\n----------------------")
                print("Produto:", produto.get("title"))
                print("Preço:", produto.get("price"))
                print("Preço original:", produto.get("original_price"))
                print("Link:", produto.get("permalink"))

        except Exception as erro:
            print("ERRO:", erro)

    print("\nTotal de produtos exibidos:", total)


if __name__ == "__main__":
    buscar_ofertas()
