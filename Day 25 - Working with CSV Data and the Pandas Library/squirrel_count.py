import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.columns)

squirrel_count = data['Primary Fur Color'].value_counts()
squirrel_count = pandas.DataFrame(squirrel_count)
squirrel_count.reset_index(inplace=True)
squirrel_count.columns = ["Fur Color", "Count"]

squirrel_count.to_csv("squirrel_count.csv")

# Angela's Way
#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_angela.csv")

