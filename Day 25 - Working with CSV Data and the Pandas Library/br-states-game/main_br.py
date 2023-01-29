import turtle
import pandas

screen = turtle.Screen()
screen.title("Jogo dos Estados do Brasil")
image = "Brazil_Labelled_Map.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"

# estados_br = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
# "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais",
# "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
# "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]
#
# x = [-269.0, 213.0, 2.0, -177.0, 145.0, 166.0, 58.0, 159.0, 20.0, 88.0, -63.0, -50.0, 110.0,
# -12.0, 224.0, 3.0, 220.0, 115.0, 130.0, 213.0, -15.0, -155.0, -130.0, 26.0, 55.0, 200.0, 46.0]
#
# y = [71.0, 64.0, 221.0, 142.0, 19.0, 150.0, -21.0, -73.0, -44.0, 136.0, 2.0, -93.0, -38.0,
# 152.0, 104.0,-154.0, 86.0, 91.0, -115.0, 123.0, -230.0, 41.0, 233.0, -185.0, -125.0, 49.0, 48.0]

# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# df = pandas.DataFrame({
# 	"Estados": estados_br,
# 	"x": x,
# 	"y": y
# 	})
#
# df.to_csv("estados_br.csv")

dados = pandas.read_csv("estados_br.csv")
lista_estados = dados["Estados"].to_list()
estados_corretos = 0
palpites_corretos = list()

# TODO 4. Use a loop to allow the user to keep guessing
while estados_corretos < 50:
    resposta = screen.textinput(title=f"{estados_corretos}/27 Estados Corretos",
                                prompt="Diga o nome de um Estado Brasileiro?")
    # TODO 1. Convert the guess to Title Case
    resposta = resposta.title()

    # TODO 7. Create a exit
    if resposta == "Exit":
        break

    # TODO 2. Check if the guess is among the 50 states
    if resposta in lista_estados:
        x_coor = dados[dados.Estados == resposta].x.item()
        y_coor = dados[dados.Estados == resposta].y.item()

        # TODO 3. Write correct guesses onto the map
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x=x_coor, y=y_coor)
        new_state.write(resposta, font=FONT, align=ALIGNMENT)

        # TODO 5. Record the correct guesses in a list
        palpites_corretos.append(resposta)
        print(palpites_corretos)

        # TODO 6. Keep track of the score
        estados_corretos += 1
    else:
        print("False")

# states to learn.csv
estados_para_aprender = list()
for estado in lista_estados:
    if estado not in palpites_corretos:
        estados_para_aprender.append(estado)

estados_para_aprender_df = pandas.DataFrame({"Aprender": estados_para_aprender})
estados_para_aprender_df.to_csv("estados_para_aprender.csv")
