def adicionar_contato(nome_contato, telefone, email, favorito, contatos):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato {nome_contato} adiconado com sucesso!")
    return

def listar_contatos():
    print("Lista de Contatos: ")
    
    for i, contato in enumerate(contatos):
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]        
        favorito = "*" if contato["favorito"] else ""
        print(f"{i}. Nome: {nome_contato:<30} | Telefone: {telefone:<15} | Email: {email:<30} | Favorito: {favorito}")
    return

contatos = []

while True:
    print("\nMenu da Agenda")
    print("1. Adicionar Novo Contato")
    print("2. Mostrar Lista de Contatos")
    print("3. Editar Contato")
    print("4. Marcar Contato como Favorito")
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

    elif escolha == "7":
        break
    
print("Programa Finalizado!")
