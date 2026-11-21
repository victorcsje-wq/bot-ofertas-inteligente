import requests

API = "https://api.mercadolibre.com/sites/MLB/search"

PESQUISAS = [
    "smartphone",
    "notebook",
    "fone bluetooth",
    "smart tv",
    "mouse gamer",
    "teclado mecanico",
    "monitor",
    "videogame"
]


def buscar_ofertas():

    ofertas = []

    for pesquisa in PESQUISAS:

        print(f"Pesquisando: {pesquisa}")

        parametros = {
            "q": pesquisa,
            "limit": 10
        }

        try:
            resposta = requests.get(
                API,
                params=parametros,
                timeout=30
            )

            resposta.raise_for_status()

            produtos = resposta.json().get("results", [])

            for produto in produtos:

                preco = produto.get("price")
                original = produto.get("original_price")

                if not preco or not original:
                    continue

                if original <= preco:
                    continue

                desconto = (
                    (original - preco) / original
                ) * 100

                if desconto >= 20:

                    ofertas.append({
                        "nome": produto["title"],
                        "preco": preco,
                        "original": original,
                        "desconto": round(desconto, 1),
                        "link": produto["permalink"]
                    })

        except requests.RequestException as erro:
            print(f"Erro na pesquisa: {erro}")

    ofertas.sort(
        key=lambda x: x["desconto"],
        reverse=True
    )

    print("\n========== MELHORES OFERTAS ==========")

    for oferta in ofertas[:20]:

        print("\n🔥", oferta["nome"])
        print(f"Preço: R$ {oferta['preco']:.2f}")
        print(f"Antes: R$ {oferta['original']:.2f}")
        print(f"Desconto: {oferta['desconto']}%")
        print(oferta["link"])

    print(f"\nTotal de ofertas encontradas: {len(ofertas)}")


if __name__ == "__main__":
    buscar_ofertas()
