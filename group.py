"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

Jill = {"name":"Jill","age":26,"job":"biologist","relations":{"Zalika":"friend","John":"partner"}}
Zalika = {"name":"Zalika","age":28,"job":"artist","relations":{"Jill":"friend"}}
John = {"name":"John","age":27,"job":"writer","relations":{"Jill":"partner"}}
Nash = {"name":"Nash","age":24,"job":"chef","relations":{"John":"cousin","Zalika":"landlord"}}



my_group = {'Jill':Jill,'Zalika':Zalika,'John':John,'Nash':Nash}

def lookup_person(group, name, *othername):
	vowels = set(['a','e','i','o','u'])

	person = group[name]
	output = person["name"] + " is "
	output += person["age"]
	if "job" in person:
		if person["job"][0] in(vowels):
			output += ", an "
		else
			output += ", a"
		output += person["job"]

	if othername in person["relations"]:
		output += ", and "
		output += othername
		output += "'s "
		output += person["relations"][othername]
	else
		output += ", and they do not know "
		output += othername
	output += "."

	return output



print(lookup_person(my_group,"Zalika","John"))
print(lookup_person(my_group,"Zalika","Nash"))
print(lookup_person(my_group,"Zalika"))
		





