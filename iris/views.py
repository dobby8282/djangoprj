from django.shortcuts import render

# Create your views here.
def index(request):
    print('index')

    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        print(sepal_length)
        print(sepal_width)
        print(petal_length)
        print(petal_width)

        species_perdiction = 1
        return render(request, 'predict.html', {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
            'species_prediction': species_perdiction

        })

    return render(request, 'predict.html')
