import requests
import ttkbootstrap as tb
from tkinter import StringVar, messagebox

# Sua chave de API (cadastre-se no OpenWeatherMap para obter uma)
API_KEY = "7fe37c98b1334bf26718061a3615d41b"

def buscar_clima():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showwarning("Erro", "Digite o nome da cidade!")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if dados["cod"] != 200:
            messagebox.showerror("Erro", f"Cidade não encontrada: {cidade}")
            return

        clima = dados["weather"][0]["description"].capitalize()
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]

        resultado.set(f"🌤 Clima: {clima}\n🌡 Temperatura: {temperatura}°C\n💧 Umidade: {umidade}%")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao obter os dados: {str(e)}")

# Criando a interface com ttkbootstrap
app = tb.Window(themename="solar")  # Tema moderno
app.title("🌎 App de Clima")
app.geometry("400x450")

# Frame principal
frame = tb.Frame(app, padding=20)
frame.pack(expand=True, fill="both")

# Título
tb.Label(frame, text="🌤 Consulta de Clima", font=("Helvetica", 18, "bold")).pack(pady=10)

# Campo de entrada com estilo
entrada_cidade = tb.Entry(frame, font=("Helvetica", 14), width=25, bootstyle="info")
entrada_cidade.pack(pady=10)

# Botão de buscar com ícone
btn_buscar = tb.Button(frame, text="🔍 Buscar Clima", bootstyle="success-outline", command=buscar_clima)
btn_buscar.pack(pady=10)

# Área de resultado dentro de um frame estilizado
resultado = StringVar()
frame_resultado = tb.LabelFrame(frame, text="📋 Resultado", padding=10)
frame_resultado.pack(pady=10, fill="both", expand=True)
tb.Label(frame_resultado, textvariable=resultado, font=("Helvetica", 14), justify="center").pack()

# Rodapé com o nome do criador
rodape = tb.Label(app, text="Criado por Domingos João", font=("Helvetica", 10, "italic"), bootstyle="dark")
rodape.pack(side="bottom", fill="x", pady=5)

# Rodar o app
app.mainloop()
