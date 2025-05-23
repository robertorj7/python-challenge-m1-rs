def adicionar_contato(nome_contato, telefone, email, favorito, contatos):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato {nome_contato} adiconado com sucesso!")
    return

def listar_contatos():
    print("\nLista de Contatos: ")
    
    for i, contato in enumerate(contatos, start=1):
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]        
        favorito = "*" if contato["favorito"] else " "        
        print(f"{i}. Nome: {nome_contato:<20} | Telefone: {telefone:<15} | Email: {email:<10} | Favorito: {favorito}")
    return

def atualizar_contato(indice_contato, nome_contato, telefone, email, contatos):
    indice_ajustado = int(indice_contato) - 1
    
    contatos[indice_ajustado] ["nome"] = nome_contato
    contatos[indice_ajustado] ["telefone"] = telefone
    contatos[indice_ajustado] ["email"] = email

    print(f"Contato {indice_contato} atualizado!")
    return

def marcar_desmarcar_favorito(indice_contato, contatos):
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado] ["favorito"] = not contatos[indice_ajustado] ["favorito"]
        
    print(f"Contato {indice_contato} alterado!")
    
    return

def listar_contatos_favoritos():
    print("\nLista de Contatos Favoritos: ")
    
    for i, contato in enumerate(contatos, start=1):
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]        
        favorito = "*" if contato["favorito"] else " "        
        
        if contato["favorito"]: 
            print(f"{i}. Nome: {nome_contato:<20} | Telefone: {telefone:<15} | Email: {email:<10} | Favorito: {favorito}")
    return

def apagar_contato(indice_contato, contatos):
    indice_ajustado = int(indice_contato) - 1
    contatos.pop(indice_ajustado)
    
    print(f"Contato {indice_contato} apagado!")
    return

contatos = []

while True:
    print("\nMenu da Agenda")
    print("1. Adicionar Novo Contato")
    print("2. Mostrar Lista de Contatos")
    print("3. Editar Contato")
    print("4. Marcar Ou Desmarcar Contato como Favorito")
    print("5. Mostrar Lista de Contatos Favoritos")
    print("6. Apagar Contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(nome_contato, telefone, email, False, contatos)
    
    elif escolha == "2":
        listar_contatos()
    
    elif escolha == "3":
        listar_contatos()
        indice_contato = input("Digite o indice do contato a ser atualizado: ")
        indice_ajustado = int(indice_contato) - 1
        
        if indice_ajustado >= 0 and indice_ajustado < len(contatos):
            print("Digite as informações a serem atualizadas: ")
            nome_contato = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")

            atualizar_contato(indice_contato, nome_contato, telefone, email, contatos)
        else:            
            print("\nÍndice de Contato inválido!")

    elif escolha == "4":
        listar_contatos()
        indice_contato = input("Digite o indice do contato a ser marcado/desmarcado como favorito: ")
        indice_ajustado = int(indice_contato) - 1        

        if indice_ajustado >= 0 and indice_ajustado < len(contatos):
            marcar_desmarcar_favorito(indice_contato, contatos)            
        else:            
            print("\nÍndice de Contato inválido!")

    elif escolha == "5":
        listar_contatos_favoritos()

    elif escolha == "6":
        indice_contato = input("Digite o indice do contato a ser apagado: ")
        indice_ajustado = int(indice_contato) - 1

        if indice_ajustado >= 0 and indice_ajustado < len(contatos):
            apagar_contato(indice_contato, contatos)
        else:            
            print("\nÍndice de Contato inválido!")

    elif escolha == "7":
        break
    
print("\nPrograma Finalizado!")
