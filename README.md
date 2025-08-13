# Urban Routes - Projeto de Testes de QA Automatizado

Projeto para automação de testes para o aplicativo de rotas Urban Routes, utilizando **Python**, **Selenium** e **Pytest**, desenvolvido como parte do curso de QA da TripleTen.

---

## 🎯 Objetivo do projeto

Desenvolver testes automatizados completos para o processo de solicitação de táxi no Urban Routes.  
O objetivo foi aprender e praticar automação de testes em uma aplicação web com **Selenium** e aplicar boas práticas como o **Page Object Model (POM)**, além de consolidar o uso do **Pytest** para execução estruturada dos testes.

---

## 📌 Funcionalidades testadas

- Definição dos endereços de origem e destino na interface
- Seleção do plano Comfort disponível
- Validação do preenchimento do número de telefone com SMS
- Inserção e validação do cartão de crédito para pagamento
- Inclusão de comentários opcionais para o motorista
- Solicitação de itens extras como cobertor e lenços
- Pedido de sorvetes 
- Verificação da janela modal de busca e escolha do carro disponível

---

## ✅ Resultado

Os testes foram organizados em módulos claros, aplicando o padrão **POM** para manter o código limpo e de fácil manutenção.

### Exemplo de teste automatizado com Selenium + Page Object Model
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import data
from pages import UrbanRoutesPage

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=options
        )
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        urban_routes.set_route(address_from, address_to)
        assert urban_routes.get_from_field() == address_from
        assert urban_routes.get_to_field() == address_to
```

Testes automatizados para todo o processo de pedido de táxi no Urban Routes:

- Definir endereços de partida e destino
- Selecionar plano Comfort
- Preencher número de telefone com SMS
- Adicionar cartão de crédito
- Inserir comentário para o motorista
- Pedir cobertor e lenços
- Pedir 2 sorvetes
- Verificar janela modal de busca de carros

---

## 🛠️ Ferramentas utilizadas

- Python
- Selenium
- Pytest
- Page Object Model (POM)
- Git e GitHub

---

## 🧩 O que eu aprendi

- Estruturar um projeto de automação de testes em Python
- Gerenciar dados de teste em módulos separados
- Usar o Selenium para interagir com elementos da interface web
- Aplicar o Page Object Model (POM) para maior legibilidade e reuso
- Criar, rodar e validar testes automatizados com Pytest
- Organizar e versionar o código com Git e GitHub

---

## ⚠️ Observação importante

**Sobre a URL do servidor Urban Routes**  
Este projeto foi desenvolvido em um ambiente de curso com um servidor temporário específico fornecido pela plataforma de ensino.  
O link do servidor é individual e temporário, não sendo possível compartilhá-lo publicamente.  

Por isso, para executar os testes localmente seria necessário ter acesso ao mesmo ambiente de curso e atualizar a variável `URBAN_ROUTES_URL` no arquivo `data.py` com o link válido.  

Mesmo sem execução imediata, o código demonstra o design dos testes e a aplicação das ferramentas e boas práticas de automação.

---
