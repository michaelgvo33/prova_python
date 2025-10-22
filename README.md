#  Sistema de Gerenciamento de Veículos

Este projeto é um sistema simples em Python voltado para o gerenciamento de veículos. Ele permite:

- Registrar manutenções e vistorias,
- Exibir informações básicas ou detalhadas dos veículos,
- Calcular depreciação de carros de passeio.

Foi desenvolvido com foco em práticas de programação orientada a objetos, utilizando herança e polimorfismo para especializar os tipos de veículos.

---

##  Estrutura do Projeto

- `main.py` – Arquivo principal para execução e testes.
- `veiculos.py` – Contém as classes `Veiculo`, `CarroPasseio` e `CaminhaoCarga`.

---

## Descrição das Classes

### Classe `Veiculo`

Classe base para todos os veículos.

**Atributos:**
- `marca` (str): Marca do veículo
- `modelo` (str): Modelo do veículo
- `ano` (int): Ano de fabricação
- `cor` (str): Cor do veículo
- `quilometragem` (int): Quilometragem atual

**Métodos:**
- `registrar_manutencao(tipo, custo)`: Registra e exibe uma manutenção.
- `exibir_informacoes(detalhado=False)`: Exibe informações básicas ou completas.

---

### Classe `CarroPasseio` (herda de `Veiculo`)

Representa carros de passeio, com atributos adicionais.

**Atributos adicionais:**
- `portas` (int): Número de portas
- `combustivel` (str): Tipo de combustível

**Métodos adicionais:**
- `calcular_depreciacao(anos_uso, taxa_extra)`: Calcula e exibe a depreciação estimada com base nos anos de uso e taxa extra.

---

### Classe `CaminhaoCarga` (herda de `Veiculo`)

Representa caminhões de carga.

**Atributos adicionais:**
- `capacidade` (int): Capacidade de carga (em toneladas)
- `eixos` (int): Número de eixos

**Métodos adicionais:**
- `registrar_vistoria(motivo, multa=0)`: Registra e exibe uma vistoria realizada, com possível multa.

---

## Exemplo de Execução (`main.py`)

```python
from veiculos import CarroPasseio, CaminhaoCarga

carro = CarroPasseio("Fiat", "Argo", 2022, "Vermelho", 35000, 4, "Gasolina")
caminhao = CaminhaoCarga("Volvo", "FH", 2020, "Branco", 120000, 18, 4)

print("=== Informações do Carro ===")
carro.exibir_informacoes(True)
carro.registrar_manutencao("Troca de óleo", 250)
carro.calcular_depreciacao(3, 0.02)

print("\n=== Informações do Caminhão ===")
caminhao.exibir_informacoes(True)
caminhao.registrar_vistoria("Vistoria anual", 0)
