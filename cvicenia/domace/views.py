from django.shortcuts import render, HttpResponse

def meno(request):
    meno = {
        "meno_priezvisko" : "Samuel Svoboda"
    }
    return render(request, "domace/meno.html", meno)

def du2_vizitka(request):
    vizitka = {
        "meno": "Samuel Svoboda",
        "trieda": "3.A",
        "vek": 18,
        "predmety": ["Programovanie", "Matematika", "Telesná výchova"],
    }
    return render(request, "domace/du2_vizitka.html", vizitka)
