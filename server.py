from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurações da API do WooCommerce
wc_api_url = 'https://andarilhajm.com.br'
consumer_key = 'ck_f0b53ba25c5e53b59f8276518a0c2b24f32f4037'  # Substitua pela chave do consumidor
consumer_secret = 'cs_7023ed2dd9fe5e314745bf90fc09033324e9bf74'  # Substitua pelo segredo do consumidor

# Função para enviar notificação (aqui estamos apenas imprimindo, mas você pode enviar um email, SMS, etc.)
def send_notification(order):
    print(f'Nova venda realizada: {order}')

@app.route('/webhook', methods=['POST'])
def webhook():
    order = request.json
    print('Webhook recebido:', order)

    # Enviar notificação
    send_notification(order)

    return jsonify({'status': 'success'}), 200

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    response = requests.get(
        f'{wc_api_url}orders/{order_id}',
        auth=(consumer_key, consumer_secret)
    )
    order = response.json()
    return jsonify(order)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
