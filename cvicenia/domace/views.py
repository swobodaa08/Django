from django.shortcuts import render, HttpResponse

def meno(request):
    meno = {
        "meno_priezvisko" : "Samuel Svoboda"
    }
    return render(request, "domace/meno.html", meno)