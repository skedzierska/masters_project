from fastapi import FastAPI

app = FastAPI()

inventory = {
        1: {
            "nazwa":"Mleko",
            "ilość sztuk": 20,
            "cena": 3.29,
            "marka":"Łaciate"
        },
        2: {
            "nazwa":"Jajka",
            "ilość sztuk": 150,
            "cena": 12.23,
            "marka":"Biedronka"
        },
        3: {
            "nazwa":"Mąka",
            "ilość sztuk": 10,
            "cena": 5.99,
            "marka":"Młyny"
        },
        4: {
            "nazwa":"Cukier",
            "ilość sztuk": 40,
            "cena": 7.84,
            "marka":"Diament"
        },
        5: {
            "nazwa":"Twaróg",
            "ilość sztuk": 43,
            "cena": 2.96,
            "marka":"Pilos"
        }

}

@app.get("/")
def read_root():
    return {"Jest to prosta strona API do śledzenia "
            "inwentarza sklepu - jego ilości, ceny oraz marki. "
            "Aby sprawdzić dany produkt wejdź na /nazwa_produktu?name=(wpisz nazwe produktu)"
 }

@app.get("/nazwa_produktu")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["nazwa"] == name:
            return inventory[item_id]
    return {"Nie ma takiego produktu na stanie"}






