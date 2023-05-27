# Template de História de Usuário em Markdown

Este template de história de usuário em Markdown foi criado para guiar os analistas de requisitos na criação de histórias de usuário consistentes e eficientes, usando a metodologia BDD.

Os prototipos devem ser construídos usando o figma (https://www.figma.com/login)

# Estrutura básica

Uma história de usuário deve conter os seguintes elementos:

* Título
* Descrição
* Critérios de aceitação (Cenários BDD)
* Testes Unitários (TDD)

Vamos detalhar cada um deles.

## Título

O título deve ser breve e descrever a funcionalidade ou a necessidade do usuário.

Exemplo:
```
# Cadastro de usuário
```

## Descrição

A descrição deve seguir o formato "**Como** [ator], **eu quero** [ação], **para que** [benefício]". Isso ajuda a esclarecer quem é o usuário, o que ele deseja fazer e por que ele deseja fazer isso.

Exemplo:
```
**Como um** administrador, **eu quero** cadastrar novos usuários no sistema, **para que** eles possam acessar as funcionalidades de acordo com seu perfil.
```

### Critérios de aceitação (Cenários BDD)

Os critérios de aceitação são cenários BDD que descrevem o comportamento esperado da funcionalidade. Cada cenário deve seguir o formato "**Dado** [contexto], **Quando** [evento], **Então** [resultado esperado]". Pode haver vários cenários para uma história de usuário.

Normalmente colocamos no critério de aceitação uma imagem (um prototipo) ao final do cenário.

Exemplo:

```
**Cenário 1: Cadastro de usuário com sucesso**
**Dado que** o administrador está na tela de cadastro de usuários
**E** preenche todos os campos obrigatórios corretamente
**Quando** o administrador clicar no botão "Cadastrar"
**Então** o usuário deve ser cadastrado no sistema
**E** uma mensagem de sucesso deve ser exibida

![Protótipo da tela de cadastro de usuário](https://exemplo.com/imagens/tela_cadastro_usuario.png "Tela de cadastro de usuário")

**Cenário 2: Cadastro de usuário com email duplicado**
**Dado que** o administrador está na tela de cadastro de usuários
**E** preenche todos os campos obrigatórios corretamente
**Mas** o email informado já existe no sistema
**Quando** o administrador clicar no botão "Cadastrar"
**Então** o usuário não deve ser cadastrado no sistema
**E** uma mensagem de erro informando a duplicidade do email deve ser exibida

![Protótipo da tela de Cadastro de usuário com email duplicado](https://exemplo.com/imagens/tela_cadastro_usuario.png "Tela de cadastro de usuário")
```

### Testes Unitários (TDD)

Essa seção deve listar os testes unitários que serão implementados para garantir que a funcionalidade esteja funcionando corretamente.

Você pode listar os testes unitários relevantes para cada cenário, descrevendo o objetivo de cada teste e garantindo que a implementação esteja correta e livre de erros.

Cada teste proposto deve ter uma tabela informando os dados de entrada e o resultado esperado na saída.

Exemplo:

```
## Testes Unitários (TDD)

### Testar a função `cadastrarUsuario`

| Nome         | Email               | Senha  | Email já existe? | Resultado Esperado              |
|--------------|---------------------|--------|------------------|---------------------------------|
| João Silva   | joao.silva@teste.com| 123456 | Não              | Sucesso: Usuário cadastrado     |
| Maria Santos | maria@teste.com     | abcdef | Sim              | Erro: Email já cadastrado       |
| José Pereira | jose@teste.com      | 654321 | Não              | Sucesso: Usuário cadastrado     |

### Testar a função `validarCamposObrigatorios`

| Nome         | Email               | Senha  | Resultado Esperado                  |
|--------------|---------------------|--------|-------------------------------------|
| João Silva   | joao.silva@teste.com| 123456 | Sucesso: Todos os campos preenchidos |
| Maria Santos |                     | abcdef | Erro: Email não preenchido          |
| José Pereira | jose@teste.com      |        | Erro: Senha não preenchida          |
```

# Exemplo completo

```
# Cadastro de usuário

**Como um** administrador, **eu quero** cadastrar novos usuários no sistema, **para que** eles possam acessar as funcionalidades de acordo com seu perfil.

**Cenário 1: Cadastro de usuário com sucesso**
**Dado que** o administrador está na tela de cadastro de usuários
**E** preenche todos os campos obrigatórios corretamente
**Quando** o administrador clicar no botão "Cadastrar"
**Então** o usuário deve ser cadastrado no sistema
**E** uma mensagem de sucesso deve ser exibida

![Protótipo da tela de cadastro de usuário](https://exemplo.com/imagens/tela_cadastro_usuario.png "Tela de cadastro de usuário")

**Cenário 2: Cadastro de usuário com email duplicado**
**Dado que** o administrador está na tela de cadastro de usuários
**E** preenche todos os campos obrigatórios corretamente
**Mas** o email informado já existe no sistema
**Quando** o administrador clicar no botão "Cadastrar"
**Então** o usuário não deve ser cadastrado no sistema
**E** uma mensagem de erro informando a duplicidade do email deve ser exibida

![Protótipo da tela de Cadastro de usuário com email duplicado](https://exemplo.com/imagens/tela_cadastro_usuario.png "Tela de cadastro de usuário")

## Testes Unitários (TDD)

### Testar a função `cadastrarUsuario`

| Nome         | Email               | Senha  | Email já existe? | Resultado Esperado              |
|--------------|---------------------|--------|------------------|---------------------------------|
| João Silva   | joao.silva@teste.com| 123456 | Não              | Sucesso: Usuário cadastrado     |
| Maria Santos | maria@teste.com     | abcdef | Sim              | Erro: Email já cadastrado       |
| José Pereira | jose@teste.com      | 654321 | Não              | Sucesso: Usuário cadastrado     |

### Testar a função `validarCamposObrigatorios`

| Nome         | Email               | Senha  | Resultado Esperado                  |
|--------------|---------------------|--------|-------------------------------------|
| João Silva   | joao.silva@teste.com| 123456 | Sucesso: Todos os campos preenchidos |
| Maria Santos |                     | abcdef | Erro: Email não preenchido          |
| José Pereira | jose@teste.com      |        | Erro: Senha não preenchida          |


## Controle de Versão

| Versão | Data       | Autor            | Descrição das Mudanças       |
|--------|------------|------------------|------------------------------|
| 1.0    | 2023-04-30 | Fulano de Tal    | Criação da história de usuário|
| 1.1    | 2023-05-02 | Ciclano da Silva | Adição de critérios TDD      |
| 1.2    | 2023-05-05 | Beltrano Souza   | Atualização dos cenários BDD |
```