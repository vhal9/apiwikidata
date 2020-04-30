# Api Wikidata

## Resumo:
Este repositório contém a implementação de uma API para realizar requisições na base de dados Wikidata, para retornar dados sobre entidades mapeadas nessa base.

## Execução:

#### Linux:

Instalar gerenciador de pacote pip:
  ```sh
  sudo apt install python3-pip
  ```
Instalar o pacote requests:
  ```sh
  pip3 install requests
  ```
Clone o repositorio para a pasta do projeto:
  ```sh
  git clone git@github.com:vhal9/apiwikidata.git
  ```
  ou
  ```sh
  git clone https://github.com/vhal9/apiwikidata.git
  ```
No seu projeto Python, importe a biblioteca:

```from apiwikidata.searching import Searching```

## Exemplo de uso:
``` api = Searching()```

``` api.getEntitie('UFLA')```

## Retornos das requisições:

Os dados retornados na api estão no formato JSON, com isso é possível extrair dados do objeto utilizando chaves, como em um dicionário.
Por exemplo:

```Dados = api.getEntitie('UFLA')```

```Dados['Q10387826']['claims']```

O resultado obtido desta consulta, contém todas as propriedades que a entidade UFLA possui, representadas pelo seus identificadores que iniciam com a letra P, como na imagem abaixo o idenficador P131:

![Screenshot](/imagens/exemploGetProperty.png)

Nota-se que há um identificador(Q1638425) de outra entidade a qual contém uma relação com a entidade ufla por meio da propriedade P131.

## Mais informações sobre como os dados do Wikidata estão dispostos:

https://www.wikidata.org/wiki/Wikidata:Main_Page

https://www.wikidata.org/wiki/Wikidata:Data_access/pt-br

