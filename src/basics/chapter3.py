""" Quando encontramos no output de type() o __main__, significa que o objeto está dentro do nosso código principal, 
e não foi importado de outro módulo. 


O que significa o "self"? 
Os filósofos tem tentando responder essa pergunta por milenios, seria um pouco pretensioso da minha parte explicar em algumas páginas. De qualquer forma
em python a variavel self não tem um significado especializado e claro. Note que self não é uma palavra chave, mas uma convenção, qualquer outro nome pode ser utilizado e irá funcionar normalmente, mas self é utilizado universalmente e aceito como uma das práticas em python. 


Suponha que temos escrito uma classe chamada AlgumaClasse e criamos um objeto dessa classe
oAlgumObjeto = AlgumaClasse(<argumentos_opcionais>).

O objeto oAlgumObjeto contem instâncias definidas na classe AlgumaClasse. Todos os metodos de AlgumaClasse tem uma definição parecida com isso:
def algum_metodo(self, <outros_argumentos_opcionais>):

E aqui uma forma generalista de chamar o metodo:
oAlgumObjeto.algum_metodo(<outros_argumentos_opcionais>)
"""