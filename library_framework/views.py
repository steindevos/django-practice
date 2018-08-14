from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

# Create your views here.
def show_index(request):
    return render(request, "library_framework/index.html")