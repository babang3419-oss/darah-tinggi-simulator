from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DarahTinggiApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Selamat Datang di Darah Tinggi Simulator!\nKetik 'mulai' untuk bermain.")
        self.layout.add_widget(self.label)
        
        self.text_input = TextInput(multiline=False)
        self.layout.add_widget(self.text_input)
        
        self.button = Button(text="KIRIM")
        self.button.bind(on_press=self.proses_jawaban)
        self.layout.add_widget(self.button)
        
        self.step = 0
        return self.layout

    def proses_jawaban(self, instance):
        jawaban = self.text_input.text.lower().strip()
        
        if self.step == 0:
            if jawaban == "mulai":
                self.label.text = "Pertanyaan 1:\nApakah kamu suka makan garam berlebih? (ya/tidak)"
                self.step = 1
            else:
                self.label.text = "Ketik 'mulai' untuk bermain!"
                
        elif self.step == 1:
            if jawaban == "ya":
                self.label.text = "Waduh! Garam bisa bikin tekanan darah naik.\nPertanyaan 2:\nApakah kamu sering begadang? (ya/tidak)"
                self.step = 2
            elif jawaban == "tidak":
                self.label.text = "Bagus! Jaga konsumsi garamnya.\nPertanyaan 2:\nApakah kamu sering begadang? (ya/tidak)"
                self.step = 2
            else:
                self.label.text = "Mohon jawab 'ya' atau 'tidak'.\nApakah kamu suka makan garam berlebih? (ya/tidak)"

        elif self.step == 2:
            if jawaban == "ya":
                self.label.text = "🚨 RISIKO TINGGI! 🚨\nKamu suka garam dan sering begadang. Kurangi kebiasaan ini ya!"
                self.step = 3
            elif jawaban == "tidak":
                self.label.text = "👍 CUKUP AMAN 👍\nTapi tetap jaga pola makan dan olahraga teratur ya!"
                self.step = 3
            else:
                self.label.text = "Mohon jawab 'ya' atau 'tidak'.\nApakah kamu sering begadang? (ya/tidak)"

        elif self.step == 3:
            self.label.text = "Permainan selesai! Ketik 'mulai' untuk mengulang."
            self.step = 0

        self.text_input.text = ""

if __name__ == '__main__':
    DarahTinggiApp().run()
