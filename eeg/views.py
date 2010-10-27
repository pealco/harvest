# Create your views here.

def load_data(request):
    if request.method == 'POST':
        form = DataLoadForm(request.POST)
        if form.is_valid():
            
            data_path = form.cleaned_data['data_path']
        