from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


try:
    creds = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('DatosCafeteria').sheet1
except Exception as e:
    print(e)


Builder.load_file('interfaz.kv')

class Interfaz(BoxLayout):
    def on_button_press(self):
        # Retrieve the last row of data from the sheet
        data = sheet.get_all_values()[-1]

        # Update the labels with the new data
        self.ids.mesas_disponibles.text = f'Mesas disponibles: {data[0]}'
        self.ids.mesas_ocupadas.text = f'Mesas ocupadas: {data[1]}'
        self.ids.fecha.text = f'Fecha/hora: {data[2]}'

class MyApp(App):
    def build(self):
        return Interfaz()

if __name__ == '__main__':
    MyApp().run()
