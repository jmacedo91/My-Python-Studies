import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.columns)

squirrel_count = data['Primary Fur Color'].value_counts()
squirrel_count = pandas.DataFrame(squirrel_count)
squirrel_count.reset_index(inplace=True)
squirrel_count.columns = ["Fur Color", "Count"]

squirrel_count.to_csv("squirrel_count.csv")

