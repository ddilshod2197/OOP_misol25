class ObHavo:
    def __init__(self, shahar, harorat, holat):
        self.shahar = shahar
        self.harorat = harorat
        self.holat = holat
    
    def malumot(self):
        print(f"🌤  {self.shahar} shahri")
        print(f"Harorat: {self.harorat}°C")
        print(f"Holat: {self.holat}")
    
    def harorat_yangila(self, yangi_harorat):
        self.harorat = yangi_harorat
        print(f"✅ {self.shahar}da harorat yangilandi: {yangi_harorat}°C")

# Test
ob = ObHavo("Toshkent", 28, "Quyoshli")
ob.malumot()
ob.harorat_yangila(32)
