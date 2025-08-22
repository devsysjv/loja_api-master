from django.shortcuts import render

def minha_view(request):
    # Esta função renderiza o template 'produtos/meu_html.html'
    return render(request, 'produtos/meu_html.html')