
from veiculos import CarroPasseio, CaminhaoCarga

if __name__ == "__main__":
    carro = CarroPasseio("Fiat", "Argo", 2022, "Vermelho", 35000, 4, "Gasolina")
    caminhao = CaminhaoCarga("Volvo", "FH", 2020, "Branco", 120000, 18, 4)

    print("=== Informações do Carro ===")
    carro.exibir_informacoes(True)
    carro.registrar_manutencao("Troca de óleo", 250)
    carro.calcular_depreciacao(3, 0.02)

    print("\n=== Informações do Caminhão ===")
    caminhao.exibir_informacoes(True)
    caminhao.registrar_vistoria("Vistoria anual", 0)
