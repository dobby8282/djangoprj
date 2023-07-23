from django.shortcuts import render
from .models import IrisPrediction
import numpy as np
import joblib



# Create your views here.
def index(request):
    print('index')
    return render(request, 'index.html')


model = joblib.load('model.joblib')
def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        data = np.array([[sepal_length, sepal_width,petal_length, petal_width]])
        prediction = model.predict(data)

        species_prediction = ''
        if prediction == 0:
            species_prediction = 'setosa'
        elif prediction == 1:
            species_prediction = 'versicolor'
        elif prediction == 2:
            species_prediction = 'virginica'

        # 예측 결과를 데이터베이스에 저장
        IrisPrediction.objects.create(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
            species=species_prediction
        )

        return render(request, 'predict.html', {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
            'species_prediction': species_prediction
        })

    return render(request, 'predict.html')

def history(request):
    predictions = IrisPrediction.objects.all()
    return render(request, 'history.html', {'predictions': predictions})