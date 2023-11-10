from urllib.parse import urlparse


def is_valid_url(input_string):
    try:
        result = urlparse(input_string)
        return all(
            [result.scheme, result.netloc]
        )  # Verifica se há esquema e local de rede
    except ValueError:
        return False


if __name__ == "__main__":
    print(is_valid_url("http://www.google.com"))
    # Exemplo de uso:
    url1 = "https://www.exemplo.com"
    url2 = "isso_nao_e_uma_url"

    if is_valid_url(url1):
        print(f"{url1} é uma URL válida.")
    else:
        print(f"{url1} não é uma URL válida.")

    if is_valid_url(url2):
        print(f"{url2} é uma URL válida.")
    else:
        print(f"{url2} não é uma URL válida.")
