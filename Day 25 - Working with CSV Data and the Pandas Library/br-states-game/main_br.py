import turtle
import pandas

screen = turtle.Screen()
screen.title("Jogo dos Estados do Brasil")
image = "Brazil_Labelled_Map.gif"
screen.addshape(image)
turtle.shape(image)

estados_br = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
"Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais",
"Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
"Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]

x = [-269.0, 213.0, 2.0, -177.0, 145.0, 166.0, 58.0, 159.0, 20.0, 88.0, -63.0, -50.0, 110.0,
-12.0, 224.0, 3.0, 220.0, 115.0, 130.0, 213.0, -15.0, -155.0, -130.0, 26.0, 55.0, 200.0, 46.0]

y = [71.0, 64.0, 221.0, 142.0, 19.0, 150.0, -21.0, -73.0, -44.0, 136.0, 2.0, -93.0, -38.0,
152.0, 104.0,-154.0, 86.0, 91.0, -115.0, 123.0, -230.0, 41.0, 233.0, -185.0, -125.0, 49.0, 48.0]

# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

df = pandas.DataFrame({
	"Estados": estados_br,
	"x": x,
	"y": y
	})

df.to_csv("estados_br.csv")

turtle.mainloop()

