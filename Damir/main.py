class Moshina:
    def __init__(self):
        self.tur = None
        self.nomi = None
        self.rang = None
        self.narx = 0
        self.turlar = {
            "1": "Sedan",
            "2": "Jip",
            "3": "Hatchback",
            "4": "Krossover"
        }
        self.nomlar = {
            "1": "Chevrolet Malibu",
            "2": "Toyota Camry",
            "3": "Kia Sportage",
            "4": "Hyundai Tucson"
        }
        self.ranglar = {
            "1": "Qora",
            "2": "Oq",
            "3": "Qizil",
            "4": "Ko'k"
        }
        self.narxlar = {
            "Sedan": 20000,
            "Jip": 30000,
            "Hatchback": 15000,
            "Krossover": 25000
        }

    def tanlash(self, tanlov_nomi, variantlar):
        while True:
            print(f"\n{tanlov_nomi}:")
            for kalit, qiymat in variantlar.items():
                print(f"{kalit}. {qiymat}")
            tanlov = input(f"{tanlov_nomi}ni tanlang (1-{len(variantlar)}): ")
            if tanlov in variantlar:
                return variantlar[tanlov]
            else:
                print(f"Xato! Faqat 1 dan {len(variantlar)} gacha son kiriting.")

    def parametrlarni_aniqlash(self):
        self.tur = self.tanlash("Moshina turi", self.turlar)
        self.nomi = self.tanlash("Moshina nomi", self.nomlar)
        self.rang = self.tanlash("Moshina rangi", self.ranglar)
        self.narx = self.narxlar.get(self.tur, 0)

    def yakuniy_malumot(self):
        print("\nSiz tanlagan moshina:")
        print(f"Tur: {self.tur}")
        print(f"Nomi: {self.nomi}")
        print(f"Rang: {self.rang}")
        print(f"Narxi: ${self.narx:,} USD")

    def boshqarish(self):
        self.parametrlarni_aniqlash()
        self.yakuniy_malumot()


if __name__ == "__main__":
    moshina = Moshina()
    moshina.boshqarish()