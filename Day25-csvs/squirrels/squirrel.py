import pandas

squirrels = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur = squirrels["Primary Fur Color"]

furlist = fur.to_list()

numgray = furlist.count('Gray')
numcinnamon = furlist.count('Cinnamon')
numblack = furlist.count('Black')

furcount = {
    'Color' : ['Gray', 'Cinammon', 'Black'],
    'Count' : [numgray, numcinnamon, numblack]
}

final = pandas.DataFrame(furcount)
final.to_csv('furcount.csv')