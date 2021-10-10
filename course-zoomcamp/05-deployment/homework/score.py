import pickle


def load_modules():
    with open('model1.bin', 'rb') as f_in:
        model = pickle.load(f_in)
    with open('dv.bin', 'rb') as f_in:
        dv = pickle.load(f_in)
    return dv, model


def predict_single(customer, dv, model):
    print(dv)
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

if __name__ == '__main__':
    dv, model = load_modules()
    print(predict_single(customer, dv, model))
