import os

def Classificador_chuva(QuantidadeMM):
    if QuantidadeMM <= 20:
        return "Nivel De Chuva Baixo (Verde)"
    elif 20 < QuantidadeMM <= 30:
        return "Nivel De Chuva Medio (Amarelo)" 
    else:
        return "Nivel De Chuva Alto (Vermelho)"

Chuvas = [10, 25, 55, 0, 45, 80]
chuva_total = 0
registro_usuario=[]


while True:
    nome_digitado = input("Digite Seu Nome De Registro ou Se Deseja Encerrar Sua Sessao Digite 'sair':").strip()
    if nome_digitado.lower() == 'sair':      
        print('\n Seu Registro Esta Finalizado com Sucesso!! ')
        print('\n    \t------Sua Analise------')
        break

    cpf_digitado = input('Digite Seu CPF:').strip()
    registro_usuario.append((nome_digitado.title(), cpf_digitado))


    caminho_pasta_usuario = os.path.join("dados_usuario",nome_digitado.title())

    os.makedirs(caminho_pasta_usuario, exist_ok=True)
    print(f"Pasta '{caminho_pasta_usuario}'criada com sucesso.")

    caminho_arquivo = os.path.join(caminho_pasta_usuario, "registro.txt")
 

    with open (caminho_arquivo, 'w') as aquirvo:
      aquirvo.write(f"Nome: {nome_digitado.title()}\n")
      aquirvo.write(f"CPF: {cpf_digitado}\n")



for i, chuva in enumerate(Chuvas):
    status = Classificador_chuva(chuva)
    litros = chuva 
    print(f'Registro {i+1}: {chuva} mm - {status} - {litros} litros por m²')
    chuva_total += chuva


print('\n ----- Resultados -----')
print(f'Total de chuva: {chuva_total} mm²')
print(f'Isto equivale a {chuva_total} Litros por metros quadrado')


print('\n ---Usuarios Registrados---')
for Nome, cpf in registro_usuario:
    print(f'- Nome: {Nome} | CPF: {cpf}')
    