from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GameEmosiApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text="[b]DARAH TINGGI SIMULATOR[/b]\n\nSelamat datang di ujian kesabaran!\nMasukkan nama panggilan kamu:", 
            markup=True, 
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.layout.add_widget(self.label)
        
        self.text_input = TextInput(text='', multiline=False, size_hint_y=None, height=50)
        self.layout.add_widget(self.text_input)
        
        self.btn = Button(text="LANJUT", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.8, 1))
        self.btn.bind(on_press=self.proses_game)
        self.layout.add_widget(self.btn)
        
        self.step = 1
        return self.layout

    def proses_game(self, instance):
        jawaban = self.text_input.text.strip().lower()
        
        if self.step == 1:
            if not jawaban:
                return
            self.label.text = f"Halo {jawaban}!\n\n--- LEVEL 1 ---\nKamu di depan 2 pintu:\n1. Pintu Kiri (Merah)\n2. Pintu Kanan (Biru)\n\nKetik 'kiri' atau 'kanan':"
            self.step = 2
        elif self.step == 2:
            if jawaban == "kiri":
                self.label.text = "🚪 Salah! Ini pintu kamar mandi umum.\nKamu diusir warga. GAME OVER! Wkwk."
                self.btn.text = "ULANGI DARI AWAL"
                self.step = 1
            elif jawaban == "kanan":
                self.label.text = "🎉 Mantap! Lolos ke Level 2.\n\nMatematika nyeleneh:\nJika 1+1=3, maka 3+3 = ?\n(Ketik angka):"
                self.step = 3
            else:
                self.label.text = "❌ Kelamaan mikir, atap runtuh!\nKalah telak. Coba lagi?"
                self.step = 1
        elif self.step == 3:
            if jawaban == "9":
                self.label.text = "🏆 MENANG!\nKamu berhasil menaklukkan game penuh emosi ini!"
            else:
                self.label.text = f"💥 Dijitak penjaga! Mana ada 3+3 jadi {jawaban}? Harusnya 9!"
            self.btn.text = "MAIN LAGI"
            self.step = 1
            
        self.text_input.text = ""

if __name__ == '__main__':
    GameEmosiApp().run()
