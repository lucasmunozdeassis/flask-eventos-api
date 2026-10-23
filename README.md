# API REST de Gestão de Eventos — Flask

Uma API RESTful desenvolvida em **Python** utilizando o micro-framework **Flask**, projetada para o gerenciamento de eventos presenciais e online.

O projeto aplica **Programação Orientada a Objetos (POO)** com herança de classes, manipulação e serialização de objetos para JSON, tratamento de erros HTTP customizados e rotas completas de **CRUD** (Create, Read, Update, Delete) com suporte a atualizações parciais via verbos `PUT` e `PATCH`.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Flask
* **Servidor WSGI/Dev:** Werkzeug
* **Testes & Documentação de Rotas:** Postman
* **Controle de Versão:** Git & GitHub

---

##  Destaques do Projeto

* **Arquitetura Orientada a Objetos (POO):** Modelo de domínio estruturado com a classe base `Evento` e extensão via herança com `EventoOnline`, com geração dinâmica de IDs e atribuição automática de URLs de salas virtuais.
* **Padrões RESTful & Boas Práticas:** Rotas organizadas sob o prefixo `/api/eventos`, respostas padronizadas em JSON e códigos de status HTTP apropriados (`200 OK`, `400 Bad Request`, `404 Not Found`).
* **Garantia de Qualidade & Testes:** Coleção completa de testes de requisição exportada do **Postman** (`API FLASK.postman_collection.json`) já incluída no repositório.
* **Tratamento Elegante de Erros:** Captura e manipulação customizada de exceções `404 Not Found` retornando estruturas JSON padronizadas via `make_response`.

---

## 📂 Estrutura do Projeto

```text
flask-eventos-api/
├── main.py                          # Aplicação Flask principal, rotas e tratamento de erros
├── evento.py                        # Classe base Evento e métodos de serialização
├── eventoonline.py                  # Classe filha EventoOnline (Herança e Métodos de Classe)
├── API FLASK.postman_collection.json # Coleção de testes do Postman pronta para importação
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação do repositório
```

---

##  Mapeamento de Endpoints (API)

### Rotas Informativas

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Retorna o status da API, total de eventos ativos e os atalhos para os endpoints |

### Rotas do Recurso Eventos

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/eventos` | Lista todos os eventos cadastrados |
| `GET` | `/api/eventos/<id>/` | Exibe os detalhes de um evento específico pelo ID |
| `POST` | `/api/eventos` | Cria um novo evento (presencial ou online) |
| `PUT` | `/api/eventos/<id>/` | Atualização total das informações de um evento |
| `PATCH` | `/api/eventos/<id>/` | Atualização parcial das informações de um evento |
| `DELETE` | `/api/eventos/<id>/` | Remove um evento do sistema pelo ID |

---

## Como Testar com o Postman

1. Abra o **Postman**.
2. Clique no botão **Import** (canto superior esquerdo).
3. Selecione o ficheiro **`API FLASK.postman_collection.json`** presente na raiz deste repositório.
4. As requisições para todos os verbos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) serão importadas prontas para uso.

---

## Como Executar a Aplicação Localmente

### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/lucasmunozdeassis/flask-eventos-api.git
   cd flask-eventos-api
   ```

2. **Criar e ativar o ambiente virtual (`venv`):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Linux/macOS
   # No Windows utilize: venv\Scripts\activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python main.py
   ```

5. O servidor estará rodando em: `http://127.0.0.1:5000/`

---

## Autor

**Lucas Fernando Muñoz de Assis**  
* GitHub: [@lucasmunozdeassis](https://github.com/lucasmunozdeassis)
