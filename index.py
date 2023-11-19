# Manipulando Arrays

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

lista_produtos.append('creme para mãos')
lista_produtos.append('cera para depilação')

for i in range(len(lista_produtos)):
  lista_produtos[1] = 'rimel'
  lista_produtos[4] = 'loções hidratantes'

  print(lista_produtos[i])