#DANILO ABUDE GIGLIOTTI 3247887-9

import datetime

class Estacionamento:
    def __init__(self):
        self.tarifas = {
            'carro_pequeno': {'3h': 10, 'hora_adicional': 2},
            'carro_grande': {'3h': 15, 'hora_adicional': 3},
            'moto': {'3h': 5, 'hora_adicional': 1}
        }
        self.veiculos = []

    def cadastrar_tarifa(self, tipo_veiculo, tarifa_3h, tarifa_hora_adicional):
        self.tarifas[tipo_veiculo] = {'3h': tarifa_3h, 'hora_adicional': tarifa_hora_adicional}

    def registrar_entrada(self, placa, tipo_veiculo):
        entrada = {'placa': placa, 'tipo_veiculo': tipo_veiculo, 'hora_entrada': datetime.datetime.now()}
        self.veiculos.append(entrada)
        print("Entrada registrada com sucesso.")

    def registrar_saida(self, placa, forma_pagamento):
        for veiculo in self.veiculos:
            if veiculo['placa'] == placa:
                hora_saida = datetime.datetime.now()
                tempo_permanencia = hora_saida - veiculo['hora_entrada']
                horas = tempo_permanencia.total_seconds() / 3600
                tarifa = self.tarifas.get(veiculo['tipo_veiculo'], None)
                if tarifa:
                    valor_a_pagar = tarifa['3h'] + max(0, horas - 3) * tarifa['hora_adicional']
                    if forma_pagamento.lower() == 'pix':
                        valor_a_pagar *= 0.95  
                    print(f"Valor a pagar: R${valor_a_pagar:.2f}")
                    print(f"Tempo de permanência: {tempo_permanencia}")
                    self.veiculos.remove(veiculo)
                    return
                else:
                    print("Tarifa não encontrada para este tipo de veículo.")
                    return
        print("Veículo não encontrado.")

    def gerar_relatorio_diario(self):
        print(f"Quantidade de veículos que entraram: {len(self.veiculos)}")
        valor_total = sum(self.tarifas[veiculo['tipo_veiculo']]['3h'] for veiculo in self.veiculos)
        print(f"Valor total arrecadado: R${valor_total:.2f}")

    def gerar_relatorio_por_tipo(self):
        tipos_veiculos = {}
        for veiculo in self.veiculos:
            tipo_veiculo = veiculo['tipo_veiculo']
            if tipo_veiculo in tipos_veiculos:
                tipos_veiculos[tipo_veiculo] += 1
            else:
                tipos_veiculos[tipo_veiculo] = 1

        for tipo, quantidade in tipos_veiculos.items():
            print(f"Tipo de veículo: {tipo}, Quantidade: {quantidade}")

        tarifas_veiculos = self.tarifas
        for tipo, quantidade in tipos_veiculos.items():
            valor_total = quantidade * tarifas_veiculos[tipo]['3h']
            print(f"Tipo de veículo: {tipo}, Média de valor gasto: R${valor_total / quantidade:.2f}")

estacionamento = Estacionamento()

while True:
    print("\nOpções do Menu:")
    print("1. Cadastrar Tarifas")
    print("2. Registrar Entrada de Veículo")
    print("3. Registrar Saída de Veículo")
    print("4. Gerar Relatório diário")
    print("5. Gerar Relatório por tipo de veículo")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tipo_veiculo = input("Digite o tipo de veículo: ")
        tarifa_3h = float(input("Digite a tarifa para 3 horas: "))
        tarifa_hora_adicional = float(input("Digite a tarifa por hora adicional: "))
        estacionamento.cadastrar_tarifa(tipo_veiculo, tarifa_3h, tarifa_hora_adicional)

    elif opcao == '2':
        placa = input("Digite a placa do veículo: ")
        tipo_veiculo = input("Digite o tipo de veículo: ")
        estacionamento.registrar_entrada(placa, tipo_veiculo)

    elif opcao == '3':
        placa = input("Digite a placa do veículo: ")
        forma_pagamento = input("Digite a forma de pagamento (PIX ou outro): ")
        estacionamento.registrar_saida(placa, forma_pagamento)

    elif opcao == '4':
        estacionamento.gerar_relatorio_diario()

    elif opcao == '5':
        estacionamento.gerar_relatorio_por_tipo()

    elif opcao == '6':
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
