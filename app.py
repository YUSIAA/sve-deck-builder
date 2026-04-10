from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

MASTER_DATA_FILE = "master_card_data.json"
TRIBES_FILE = "tribes.json" # 追加

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cards')
def get_cards():
    if os.path.exists(MASTER_DATA_FILE):
        with open(MASTER_DATA_FILE, "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    return jsonify({})

# 種族リストを返すAPIを追加
@app.route('/api/tribes')
def get_tribes():
    if os.path.exists(TRIBES_FILE):
        with open(TRIBES_FILE, "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True, port=5000)