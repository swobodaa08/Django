from django.shortcuts import render, HttpResponse

def meno(request):
    meno = {
        "meno_priezvisko" : "Samuel Svoboda"
    }
    return render(request, "domace/meno.html", meno)

def du2_vizitka(request):
    vizitka = {
        "meno": "Samuel Svoboda",
        "trieda": "3.AT",
        "vek": 18,
        "predmety": ["Programovanie", "Matematika", "Telesná výchova"],
    }
    return render(request, "domace/du2_vizitka.html", vizitka)


def du3_teplota(request):
    vysledok = None
    chyba = None
    teplota = ""
    smer = "c_f"

    if request.method == "POST":
        teplota = request.POST.get("teplota", "").strip()
        smer = request.POST.get("smer", "c_f")
        try:
            hodnota = float(teplota.replace(",", "."))
            if smer == "f_c":
                vysledok = f"{(hodnota - 32) * 5 / 9:.1f} °C"
            else:
                vysledok = f"{hodnota * 9 / 5 + 32:.1f} °F"
        except ValueError:
            chyba = "Zadaj platné číslo."

    return render(request, "domace/du3_teplota.html", {
        "vysledok": vysledok,
        "chyba": chyba,
        "teplota": teplota,
        "smer": smer,
    })
