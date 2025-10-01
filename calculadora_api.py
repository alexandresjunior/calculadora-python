from flask import Flask, request, jsonify
from operacoes import adicionar, subtrair, multiplicar, dividir

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():
    """
    Endpoint para realizar cálculos.
    Espera um JSON no corpo da requisição com o formato:
    {
        "operando1": <numero>,
        "operando2": <numero>,
        "operacao": <"adicionar" | "subtrair" | "multiplicar" | "dividir">
    }
    """
    # 1. Obter os dados JSON da requisição
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Corpo da requisição inválido ou vazio"}), 400

    # 2. Validar se os campos necessários existem
    campos_necessarios = ["operando1", "operando2", "operacao"]
    for campo in campos_necessarios:
        if campo not in dados:
            return jsonify({"erro": f"O campo '{campo}' é obrigatório"}), 400

    # 3. Extrair os valores
    op1 = dados['operando1']
    op2 = dados['operando2']
    operacao = dados['operacao']
    
    # 4. Mapear a operação para a função correspondente
    mapa_operacoes = {
        'adicionar': adicionar,
        'subtrair': subtrair,
        'multiplicar': multiplicar,
        'dividir': dividir
    }

    if operacao not in mapa_operacoes:
        return jsonify({"erro": f"Operação '{operacao}' não suportada."}), 400

    # 5. Executar o cálculo e tratar possíveis erros
    try:
        funcao_calculo = mapa_operacoes[operacao]
        resultado = funcao_calculo(float(op1), float(op2))
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except TypeError:
        return jsonify({"erro": "Operando1 e Operando2 devem ser números."}), 400

    # 6. Retornar o resultado em formato JSON
    return jsonify({
        "resultado": resultado,
        "detalhes": f"{op1} {operacao} {op2}"
    })

if __name__ == '__main__':
    app.run(debug=True)