# Your code goes here:
def render_person(name, birthday, color, age, sex):
    return str(name) +' is a '+ str(age) + ' years old ' + str(sex) + ' born in ' + str(birthday) + ' with ' + str(color) + ' eyes'


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))