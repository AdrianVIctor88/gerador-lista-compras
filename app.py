from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_compras = []

@app.route('/')
def index():
    return render_template('index.html', lista=lista_compras)

@app.route('/adicionar', methods=['POST'])
def adicionar_item():
    item = request.form.get('item', '').strip()
    quantidade_raw = request.form.get('quantidade')

    try:
        quantidade = int(quantidade_raw)
    except (ValueError, TypeError):
        quantidade = 0 
    
    if item and quantidade > 0:
        item_encontrado = False
        item_formatado = item.capitalize()

        # Varre a lista procurando duplicatas
        for elemento in lista_compras:
            if elemento['item'] == item_formatado:
                elemento['quantidade'] += quantidade
                item_encontrado = True
                break
        
        # Só adiciona o dicionário se ele realmente não existir na lista
        if not item_encontrado:
            lista_compras.append({'item': item_formatado, 'quantidade': quantidade})

    return redirect(url_for('index'))

@app.route('/limpar')
def limpar_lista():
    lista_compras.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)