"""[PY-A03]Considere o seguinte dicionário em Python:

pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.

b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.

c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade."""

def maior_idade(dic):
    maior = max(dic.values())
    return maior

pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

idade_joao = pessoas['João']

pessoas['Ana'] = 31

print(pessoas)



print(idade_joao)
print(maior_idade(pessoas))
