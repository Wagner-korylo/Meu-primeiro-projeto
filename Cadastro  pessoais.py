
import csv
def cadastrar_pessoa():
    # Capturar dados do usuário
    nome = input("Digite o nome completo: ")
    idade = input("Digite a idade: ")
    email = input("Digite o e-mail: ")

    # Escrever os dados em um arquivo CSV
    with open('cadastro_pessoal.csv', 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, idade, email])

    print("Cadastro realizado com sucesso!")

def main():
    print("### Cadastro Pessoal ###")
    while True:
        cadastrar_pessoa()
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
        if continuar != 's':
            break

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
