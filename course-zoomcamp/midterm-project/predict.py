from flask import Flask, request, jsonify
import pickle

def load_model(model_file):
    with open(model_file, 'rb') as f_in:
        dv, model = pickle.load(f_in)
        return dv, model

def predict_single(customer, dv, model):
  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[:, 1]
  return y_pred[0]

app = Flask('midterm')
model_file = 'model_C=1.0.bin'

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    dv, model = load_model(model_file)
    prediction = predict_single(customer, dv, model)
    
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)