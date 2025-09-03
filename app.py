from flask import Flask, request, jsonify

app = Flask(__name__)

def leon_chat(pesan: str) -> str:
    # Untuk sementara balasan sederhana
    if "halo" in pesan.lower():
        return "Halo! Aku siap membantu 🚀"
    else:
        return f"Leon AI menerima pesan: {pesan}"

@app.route("/")
def home():
    return "✅ Leon AI is running on Render 24/7!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pesan = data.get("message", "")
    balasan = leon_chat(pesan)
    return jsonify({"reply": balasan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
