from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class HastalikTahminiUygulamasi(App):
    def build(self):
        self.semptomlar = []

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.semptom_label = Label(text="Lütfen semptomları seçin:", size_hint=(1, 0.1))
        layout.add_widget(self.semptom_label)

        self.dropdown = DropDown()

        semptomlar = ["Ateş", "Baş Ağrısı", "Öksürük", "Nefes Darlığı", "Mide Bulantısı", "Karın Ağrısı", "Gözlerde Kızarıklık", "Kas Ağrıları", "Halsizlik", "Baş Dönmesi", "Titreme", "İştah Kaybı", "Sürekli Öksürük", "Baş Ağrısı ve Göz Kararması", "Sık İdrara Çıkma", "Kilo Kaybı", "Karın Şişkinliği", "Baş Ağrısı ve Bulantı", "Vücutta Kaşıntı", "Göğüs Ağrısı", "Baş Dönmesi ve İşitme Kaybı", "Göğüs Ağrısı ve Terleme", "Göğüs Ağrısı ve Nefes Darlığı", "Karın Ağrısı ve İshal", "Baş Dönmesi ve Göğüs Ağrısı", "Göz Kızarıklığı ve Kaşıntı", "Göğüs Ağrısı ve Bulantı", "Titreme ve İştah Kaybı", "Yorgunluk ve Hafıza Kaybı", "Baş Dönmesi ve Görme Bozukluğu", "Baş Ağrısı ve Boyun Ağrısı", "Göğüs Ağrısı ve Solunum Zorluğu", "Karın Ağrısı ve Kusma", "Sık İdrara Çıkma ve Karın Ağrısı", "Baş Ağrısı ve İşitme Kaybı", "Baş Dönmesi ve Ağız Kuruluğu", "Baş Ağrısı ve Göğüs Ağrısı", "Karın Ağrısı ve İshal", "Göğüs Ağrısı ve Terleme", "Göğüs Ağrısı ve Nefes Darlığı", "Karın Ağrısı ve Kusma", "Sık İdrara Çıkma ve Karın Ağrısı", "Baş Ağrısı ve İşitme Kaybı", "Baş Dönmesi ve Ağız Kuruluğu"]

        for semptom in semptomlar:
            btn = Button(text=semptom, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        semptom_sec_button = Button(text="Semptom Seç", size_hint=(1, 0.1))
        semptom_sec_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.on_semptom_select)
        layout.add_widget(semptom_sec_button)

        self.sonuc_label = Label(text="", size_hint=(1, 0.4))
        layout.add_widget(self.sonuc_label)

        return layout

    def on_semptom_select(self, instance, value):
        self.semptomlar.append(value)
        self.semptom_label.text = f"Seçilen Semptomlar: {', '.join(self.semptomlar)}"

        hastaliklar = self.hastalik_tahmini(self.semptomlar)
        self.sonuc_label.text = f"Muhtemelen aşağıdaki hastalıklardan biri olabilir:\n{', '.join(hastaliklar)}"

    def hastalik_tahmini(self, semptomlar):
        semptomlar = set(semptomlar)  # Tekrar eden semptomlar gerekli değil
        
        hastaliklar = set()

        # Hastalık tahmini yap
        if "Ateş" in semptomlar:
            hastaliklar.update(["Grip", "Üst solunum yolu enfeksiyonu"])
        if "Baş Ağrısı" in semptomlar:
            hastaliklar.update(["Migren", "Tansiyon yüksekliği"])
        if "Öksürük" in semptomlar:
            hastaliklar.update(["Soğuk algınlığı", "Akciğer enfeksiyonu"])
        if "Nefes Darlığı" in semptomlar:
            hastaliklar.update(["Astım", "KOAH"])
        if "Mide Bulantısı" in semptomlar:
            hastaliklar.update(["Mide virüsü", "Gastrit"])
        if "Karın Ağrısı" in semptomlar:
            hastaliklar.update(["Bağırsak enfeksiyonu", "Apandisit"])
        if "Gözlerde Kızarıklık" in semptomlar:
            hastaliklar.update(["Konjonktivit", "Göz enfeksiyonu"])
        if "Kas Ağrıları" in semptomlar:
            hastaliklar.update(["Fibromiyalji", "Kas zorlanması"])
        if "Halsizlik" in semptomlar:
            hastaliklar.update(["Demir eksikliği anemisi", "Tiroid sorunları"])
        if "Baş Dönmesi" in semptomlar:
            hastaliklar.update(["Vertigo", "İç kulak enfeksiyonu"])
        if "Titreme" in semptomlar:
            hastaliklar.update(["Parkinson hastalığı", "Stres"])
        if "İştah Kaybı" in semptomlar:
            hastaliklar.update(["Tifo", "Depresyon"])
        if "Sürekli Öksürük" in semptomlar:
            hastaliklar.update(["Sigara içme", "Bronşit"])
        if "Baş Ağrısı ve Göz Kararması" in semptomlar:
            hastaliklar.update(["Ağrılı migren", "Tansiyon düşüklüğü"])
        if "Sık İdrara Çıkma" in semptomlar:
            hastaliklar.update(["İdrar yolu enfeksiyonu", "Şeker hastalığı"])
        if "Kilo Kaybı" in semptomlar:
            hastaliklar.update(["Kanser", "Tiroid sorunları"])
        if "Karın Şişkinliği" in semptomlar:
            hastaliklar.update(["Laktoz intoleransı", "Karaciğer sorunları"])
        if "Baş Ağrısı ve Bulantı" in semptomlar:
            hastaliklar.update(["Migren", "Baş ağrısı"])
        if "Vücutta Kaşıntı" in semptomlar:
            hastaliklar.update(["ALERJİ", "Cilt enfeksiyonu"])
        if "Göğüs Ağrısı" in semptomlar:
            hastaliklar.update(["Kalp hastalığı", "Mide ekşimesi"])
        if "Baş Dönmesi ve İşitme Kaybı" in semptomlar:
            hastaliklar.update(["İç kulak sorunları", "Migren"])
        if "Göğüs Ağrısı ve Terleme" in semptomlar:
            hastaliklar.update(["Kalp krizi", "Anjina"])
        if "Göğüs Ağrısı ve Nefes Darlığı" in semptomlar:
            hastaliklar.update(["Kalp yetmezliği", "Akciğer hastalığı"])
        if "Karın Ağrısı ve İshal" in semptomlar:
            hastaliklar.update(["Gastroenterit", "Bağırsak tıkanıklığı"])
        if "Baş Dönmesi ve Göğüs Ağrısı" in semptomlar:
            hastaliklar.update(["Anksiyete", "Panik atak"])
        if "Göz Kızarıklığı ve Kaşıntı" in semptomlar:
            hastaliklar.update(["ALERJİ", "Konjonktivit"])
        if "Göğüs Ağrısı ve Bulantı" in semptomlar:
            hastaliklar.update(["Mide ülseri", "Gastrit"])
        if "Titreme ve İştah Kaybı" in semptomlar:
            hastaliklar.update(["Tiroid sorunları", "Stres"])
        if "Yorgunluk ve Hafıza Kaybı" in semptomlar:
            hastaliklar.update(["Depresyon", "Anemi"])
        if "Baş Dönmesi ve Görme Bozukluğu" in semptomlar:
            hastaliklar.update(["Migren", "Vertigo"])
        if "Baş Ağrısı ve Boyun Ağrısı" in semptomlar:
            hastaliklar.update(["Servikal migren", "Boyunda kas spazmı"])
        if "Göğüs Ağrısı ve Solunum Zorluğu" in semptomlar:
            hastaliklar.update(["Akciğer enfeksiyonu", "KOAH"])
        if "Karın Ağrısı ve Kusma" in semptomlar:
            hastaliklar.update(["Mide virüsü", "Mide ülseri"])
        if "Sık İdrara Çıkma ve Karın Ağrısı" in semptomlar:
            hastaliklar.update(["İdrar yolu enfeksiyonu", "Sistit"])
        if "Baş Ağrısı ve İşitme Kaybı" in semptomlar:
            hastaliklar.update(["İç kulak sorunları", "Migren"])
        if "Baş Dönmesi ve Ağız Kuruluğu" in semptomlar:
            hastaliklar.update(["Dehidrasyon", "Anksiyete"])

        return hastaliklar

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'q':
            App.get_running_app().stop()

if __name__ == '__main__':
    app = HastalikTahminiUygulamasi()
    app.bind(on_keyboard=app.on_key_down)
    app.run()
