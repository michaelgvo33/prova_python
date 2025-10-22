

class Veiculo:
    def __init__(self, marca, modelo, ano, cor, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def registrar_manutencao(self, tipo, custo):
        print(f"Manutenção registrada: {tipo} - custo R$ {custo:.2f}")

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Ano: {self.ano}")
            print(f"Cor: {self.cor}")
            print(f"Quilometragem: {self.quilometragem} km")
        else:
            print(f"{self.marca} {self.modelo} - {self.quilometragem} km")


class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano, cor, quilometragem, portas, combustivel):
        super().__init__(marca, modelo, ano, cor, quilometragem)
        self.portas = portas
        self.combustivel = combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        taxa_base = 0.05  # 5% por ano
        depreciacao = (taxa_base + taxa_extra) * anos_uso
        print(f"Depreciação estimada: {depreciacao * 100:.1f}%")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Portas: {self.portas}")
            print(f"Combustível: {self.combustivel}")


class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano, cor, quilometragem, capacidade, eixos):
        super().__init__(marca, modelo, ano, cor, quilometragem)
        self.capacidade = capacidade
        self.eixos = eixos

    def registrar_vistoria(self, motivo, multa=0):
        print(f"Vistoria: {motivo} - Multa: R$ {multa:.2f}")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Capacidade: {self.capacidade} toneladas")
            print(f"Eixos: {self.eixos}")
