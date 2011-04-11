import lipsum

stuff = "[";
g = lipsum.Generator();

for i in range(0, 100):
    stuff += "{"
    stuff += "id : " + str(i) + ","
    stuff += "type: 'article',"
    stuff += "body: '" + g.generate_paragraph() + "',"
    stuff += "title: '" + g.generate_sentence() + "'"
    stuff += "},"
stuff += "]"

print stuff