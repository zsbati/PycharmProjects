fav_flowers = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'}
fav_flowers['Alice'] = 'orchid'
print(fav_flowers)
children = {'Emily': {'profession': 'artist', 'age': 5}, 'Adam': {'profession': 'astronaut', 'age': 9},
            'Nancy': {'profession': 'programmer', 'age': 14}}
print(children)
Belov = ["Physics", "Math", "Russian"]
Smith = ["Math", "Geometry", "English"]
Sarada = ["Japanese", "Math", "Physics"]
print(len(set(Belov).union(set(Smith)).union(set(Sarada))))

n = (tuple([0, 1, 1, 2, 3, 5, 8, 13, 21])[0],)
print(type(n))
print(n)

text = "Nobody !expects, the .Spanish flue. And you?"
text = text.replace("!", "").replace("?", "").replace(".", "").replace(",", "").lower()
print(text)


i = 1
while i >= 20:
    print(i)
    i += 1