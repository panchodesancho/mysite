from django.shortcuts import render


def myself(request):
    return render(request, "hello.html")


def main(request):
    return render(request, "main.html")