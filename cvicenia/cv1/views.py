from django.shortcuts import render


def cv1_index(request):
    return render(request, "cv1_index.html", {"meno": "Samuel Svoboda"})


def cv1_obchod(request):
    produkty = [
        {"nazov": "Zošit", "cena": 1.59},
        {"nazov": "Pero", "cena": 0.99},
        {"nazov": "Kalkulačka", "cena": 12.99},
        {"nazov": "Batoh", "cena": 24.99},  
        {"nazov": "Pravítko", "cena": 5.99},
    ]

    max_cena = request.GET.get("max_cena", "").strip()
    chyba = None

    if max_cena != "":
        try:
            limit = float(max_cena.replace(",", "."))
            produkty = [p for p in produkty if p["cena"] <= limit]
        except ValueError:
            chyba = "Zadaj platné číslo."

    return render(request, "cv1_obchod.html", {
        "produkty": produkty,
        "max_cena": max_cena,
        "chyba": chyba,
    })


def cv1_body(request):
    vysledok = None
    chyba = None

    if request.method == "POST":
        try:
            body = float(request.POST.get("body", "").strip().replace(",", "."))
            maximum = float(request.POST.get("maximum", "").strip().replace(",", "."))
            if maximum <= 0 or body < 0 or body > maximum:
                raise ValueError
            percento = body / maximum * 100

            if percento >= 90:
                znamka = 1
            elif percento >= 75:
                znamka = 2
            elif percento >= 50:
                znamka = 3
            elif percento >= 30:
                znamka = 4
            else:
                znamka = 5

            perc_text = f"{percento:.1f}".replace(".", ",")
            vysledok = f"{body:g} z {maximum:g} bodov = {perc_text} % → známka {znamka}"
        except ValueError:
            chyba = "Zadaj platné čísla (maximum musí byť väčšie ako 0, bodov nemôžu byť viac ako maximum)."

    return render(request, "cv1_body.html", {
        "vysledok": vysledok,
        "chyba": chyba,
    })
