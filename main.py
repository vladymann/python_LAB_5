dict_names={"dudu":25000,"avi":30000,"itay":76000,"ortal":66000,"gal":120000}
print(dict_names)
summary=dict_names["dudu"] + dict_names["gal"]
print("the summary is: " + str(summary))
#dict_names["yoel"]=summary
#print(dict_names)
dict_names.update({"yoel":summary})
print(dict_names)
print("number of entries: " + str(len(dict_names)))
#print("idan" in dict_names)
print("yoel" in dict_names)