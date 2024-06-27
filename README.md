# Sistema Bancário

## Versão 01

### Objetivo Geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

### Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45.

___

## Versão 02

### Objetivo Geral
Separar as funções existentes de saque, depósito e extrato em funções.
Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária (vincular com usuário).

### Função saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

### Função depósito
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

### Função extrato
A função de extrato deve receber os argumentos por posição e nome (positional only e keywoed only). Argumento posicional: saldo. Argumento nomeado: extrato.

### Função criar usuário (cliente)
O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.

### Função criar conta
O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

___

## Versão 03
Neste desafio iremos atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML. Adicionar classes para cliente e as operações bancárias: depósito e saque. 

<img src="/UML.png">

___

## Versão 04
### Decorador de Log
Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

### Gerador de relatórios
Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

### Iterador personalizado
Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).
