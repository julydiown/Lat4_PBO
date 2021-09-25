class Cetacea:
    def __init__(self, sub_ordo, famili, panjang, habitat):
        self.sub_ordo = sub_ordo
        self.famili = famili
        self.panjang = panjang
        self.habitat = habitat

    def printname(self):
        print(self.sub_ordo)
        print(self.famili)
        print(self.panjang)
        print(self.habitat)

class Lumba_lumba(Cetacea):
     def __init__(self, sub_ordo, famili, panjang, habitat):
          Cetacea.__init__(self, sub_ordo, famili, panjang, habitat)
          self.nama_umum = "Lumba-lumba"

     def Lumba_lumba(Self):
        print("Nama Umum       : ", Self.nama_umum)
        print("Sub Ordo        : ", Self.sub_ordo)
        print("Famili          : ", Self.famili)
        print("Panjang Tubuh   : ", Self.panjang)
        print("Habitat         : ", Self.habitat)
        print("-------------------------------------------------")

class Pesut(Cetacea):
    def __init__(self, sub_ordo, famili, panjang, habitat):
          Cetacea.__init__(self, sub_ordo, famili, panjang, habitat)
          self.nama_umum = "Pesut"

    def Pesut(Self):
        print("Nama Umum       : ", Self.nama_umum)
        print("Sub Ordo        : ", Self.sub_ordo)
        print("Famili          : ", Self.famili)
        print("Panjang Tubuh   : ", Self.panjang)
        print("Habitat         : ", Self.habitat)
        print("-------------------------------------------------")

class Paus(Cetacea):
    def __init__(self, sub_ordo, famili, panjang, habitat):
          Cetacea.__init__(self, sub_ordo, famili, panjang, habitat)
          self.nama_umum = "Paus Biru"

    def Paus(Self):
        print("Nama Umum       : ", Self.nama_umum)
        print("Sub Ordo        : ", Self.sub_ordo)
        print("Famili          : ", Self.famili)
        print("Panjang Tubuh   : ", Self.panjang)
        print("Habitat         : ", Self.habitat)
        print("-------------------------------------------------")

x = Lumba_lumba("Odontoceti", "Delphinidae", "2-4 meter", "Laut")
y = Pesut("Odontoceti", "Delphinidae", "Max 2,75 meter", "Sungai dan Pesisir")
z = Paus("Mysticeti ", "Balaenopteridae", "Mencapai 30 meter", "laut")

x.Lumba_lumba()
y.Pesut()
z.Paus()