voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voter": 422829})
voting_data.append({"county":"Denver", "registered_voter": 463353})
voting_data.append({"county":"Jefferson", "registered_voter": 432438})
print(voting_data)
print("Tengo " +  str(len(voting_data)) + " en mi diccionario")

voting_data.insert(1,{"county":"El Paso", "registered_voter": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voter" : 422829})
voting_data[2]= ({"county":"Denver", "registered_voter": 463353})
voting_data[1]= ({"county":"Jefferson", "registered_voter": 432438})
voting_data.append({"county":"Arapahoe", "registered_voter": 422829})
print(voting_data)

#for county_dict in voting_data:
    #print(county_dict)

for i in voting_data:

     print(i['registered_voter'])

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")


