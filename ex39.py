#creating a mapping of state to abbreviation
states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#creating a basic set of state and some cities in them
cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#adding some more cities
cities['NY']='New York'
cities['OR']='Portland'


#print out some cities
print('-'*10)
print("NY states has : ",cities['NY'])
print("OR states has :",cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is :",states['Michigan'])
print("Florida's abbreviation is :",states['Florida'])
#do it by using the states then cities dict

print('-'*10)
print("Michigan has :",cities[states['Michigan']])
print("Florida has :",cities[states['Florida']])

#print every states abbreviation
print('-'*10)
for states,abbrev in list(states.items()):
    print(f"{states} abbreviation {abbrev}")

#print every city in states
print('-'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


#now do both at the same time
print('-'*10)
for states,abbrev in list(states.items()):
    print(f"{states} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
# safely get a abbreviation by states that might not be There
state=states.get('Texas')


if not state:
    print("Sorry,no Texas")

    #get a city with default Value
    city=cities.get('TX','Does NOT Exist')
    print(f"the city for the stste 'TX' is:{city}")
