#  EBANX API Challenge

API desenvolvida como parte do processo seletivo da EBANX, utilizando **FastAPI** para simular operações bancárias simples como **depósito**, **saque**, **transferência** e **consulta de saldo**.  
Os dados são mantidos em memória conforme especificação do desafio.

---

##  Tecnologias

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

---

##  Estrutura do Projeto

```
ebanx-api/
├── main.py               # Roteamento principal: /balance e /reset
├── service.py            # Lógica de negócio
├── models.py             # Validação de entrada (Pydantic)
├── routes/
│   └── event.py          # Endpoint POST /event
├── requirements.txt      # Dependências do projeto
└── README.md             # Este documento
```

---

##  Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/api-ebanx.git
cd api-ebanx
```

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 3. Rodar o servidor local

```bash
uvicorn main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs) para a interface interativa Swagger.

---

## 🌐 Testar API Publicada

A API está publicada via Render:

 [https://api-ebanx.onrender.com/docs](https://api-ebanx.onrender.com/docs)

---

##  Endpoints

| Método | Rota         | Descrição                                      |
|--------|--------------|------------------------------------------------|
| POST   | /reset       | Reseta o estado da aplicação                   |
| GET    | /balance     | Consulta o saldo de uma conta (`?account_id`) |
| POST   | /event       | Processa depósitos, saques e transferências    |

---

##  Exemplos de requisições

### Criar conta com depósito
```json
POST /event
{
  "type": "deposit",
  "destination": "100",
  "amount": 10
}
```

### Transferência entre contas
```json
POST /event
{
  "type": "transfer",
  "origin": "100",
  "destination": "300",
  "amount": 15
}
```

---

##  Testes

A aplicação passou em **100% dos testes automáticos** fornecidos pela EBANX no processo seletivo, incluindo:

- Criação e consulta de saldo
- Transferências e saques
- Tratamento de erros e status corretos

---

##  Autor

**Anderson Henrique Gonçalves**  
LinkedIn: [linkedin.com/in/anderzilla](https://linkedin.com/in/anderzilla)  
GitHub: [github.com/anderzilla](https://github.com/anderzilla)