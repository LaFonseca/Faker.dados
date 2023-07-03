from faker import Faker
import pandas as pd

# Provedor BR
fake = Faker('pt_BR')

# Lista Clientes
clientes = []

# Criação de 100 clientes fictícios
for i in range(100):
    nome = fake.name()
    endereco = fake.address()
    telefone = fake.phone_number()
    email = fake.email()
    clientes.append([nome, endereco, telefone, email])

# Lista Produtos
produtos = []

# Criação de 100 produtos fictícios
for i in range(100):
    nome = fake.word()
    preco = fake.random_number(digits=2)
    categoria = fake.word()
    produtos.append([nome, preco, categoria])

# Dataframe clientes
df_clientes = pd.DataFrame(clientes, columns=['Nome', 'Endereço', 'Telefone', 'E-mail'])

# Dataframe produtos
df_produtos = pd.DataFrame(produtos, columns=['Nome', 'Preço', 'Categoria'])

# Lista Vendas
vendas = []

# Criação de vendas fictícias
for i in range(100):
    cliente = df_clientes.sample(1).iloc[0]
    produto = df_produtos.sample(1).iloc[0]
    quantidade = fake.random_int(min=1, max=10)
    valor_total = quantidade * produto['Preço']
    vendas.append([cliente['Nome'], produto['Nome'], quantidade, valor_total])

# Dataframe Vendas
df_vendas = pd.DataFrame(vendas, columns=['Cliente', 'Produto', 'Quantidade', 'Valor Total'])

# Exibição dos DataFrames
print(df_clientes)
print(df_produtos)
print(df_vendas)