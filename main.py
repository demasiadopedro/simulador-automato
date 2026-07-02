import  json
from pathlib import Path
from automato import Automato


def carregar_automatos():
    path_data = Path('./data')
    automatos = []

    for arquivo in path_data.glob('*.json'):
        with open(arquivo) as json_file:
            try:
                dados = json.load(json_file)
                automatos.append((arquivo.name, dados))
                print(f"Lido com sucesso: {arquivo.name}")
            except json.JSONDecodeError:
                print(f"Erro de formatação no arquivo: {arquivo.name}")

    print("[*] Tudo lido")
    return automatos

def escolher_automato(automatos):
    print("\n--- Automatos disponíveis ---")
    for i, (nome, _, _) in enumerate(automatos, 1):
        print(f"  {i}. {nome}")

    try:
        num = int(input("Digite o número do automato: "))
        if 1 <= num <= len(automatos):
            return automatos[num - 1]
        print(f"[-] Digite um número entre 1 e {len(automatos)}.")
    except ValueError:
        print("[-] Entrada inválida, digite um número.")
    return None

def menu():
    automatos = [
        (nome, Automato(dados), dados)
        for nome, dados in carregar_automatos()
    ]
    if not automatos:
        print("[-] Nenhum automato encontrado em ./data")
        return

    while True:
        print("\n========= MENU =========")
        print("1. Rodar automato")
        print("2. Testar todos os automatos")
        print("3. Testar uma palavra")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            escolha = escolher_automato(automatos)
            if escolha:
                nome, automato, dados = escolha
                print(f"\n[*] Rodando testes de: {nome}")
                automato.rodar_testes(dados.get("palavras_teste", []))

        elif opcao == '2':
            for nome, automato, dados in automatos:
                print(f"\n[*] === {nome} ===")
                automato.rodar_testes(dados.get("palavras_teste", []))

        elif opcao == '3':
            escolha = escolher_automato(automatos)
            if escolha:
                nome, automato, _ = escolha
                palavra = input("Digite a palavra a ser testada: ")
                resultado = automato.processar_palavra(palavra)
                status = "ACEITA" if resultado else "REJEITADA"
                print(f"\n[*] Palavra '{palavra}' foi {status} pelo automato {nome}")

        elif opcao == '4':
            print("[*] Saindo...")
            break

        else:
            print("[-] Opção inválida.")

menu()
