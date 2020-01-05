import random
#import pandas
#legible conversion
def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', ' thousand', ' million', ' billion', ' trillion'][magnitude])
#measurement conversions
def lbstofloz(lbs):
	floz = lbs * 15.34
	return floz, "fluid ounces", "fluid ounces"
def lbstocups(lbs):
	cups = lbs * 1.917
	return cups, "cups", "cups"
def lbstogal(lbs):
	gal = lbs / 8.35
	return gal, "gallons", "gallons"
def cupstooz(cups):
	oz = cups * 8
	return oz, "ounces", "ounces"
def oztocups(oz):
	cups = oz / 8
	return cups, "cups", "cups"
def lbstooz(lbs):
	oz = lbs * 16
	return oz, "ounces", "ounces"
def tonstocups(tons):
	cups = tons * 1593.35
	return cups
def cupstotons(cups):
	tons = cups / 1593.35
	return tons
def lbstotons(lbs):
	tons = lbs * 2000
	return tons
#time conversions
def yearstodays(years):
	days = years * 365
	return days
#foods
def lbstopineapple(lbs):
	pine = lbs * 5
	return pine, "pineapples", "pounds"

def milklbs(lbs):
	milk = lbs * 8.6
	return milk, "milk", "pounds"

def beans(lbs):
	#beans to cups
	beanounces = lbstofloz(lbs)
	beancups = oztocups(beanounces[0])
	bean = beancups[0] *  9.03013
	return bean, "beans", "cups"
#populations 
def deathsaday(age):
	deaths = yearstodays(age) * 151600
	deaths = human_format(deaths)
	return deaths
def titanicdeaths(age):
	titanic = age * 1500
	return titanic

def titanicdew(age):
	# 1,593.35 cups = 1 ton
	#titanic is 52,310 tons
	#1 ton is 2000 lbs
	#12 oz = 1 mtn
	#32000 oz = 1 ton
	dews = age * 32000 * 52310
	#1 mtn dew is 12 oz and 32000 oz is 1 ton and the titanic is 52310 tons
	dewoz = dews/12
	# dewoz = round(dewoz, 0)
	dewoz = int(dewoz)
	dewoz = human_format(dewoz)
	return dewoz




# z = lbstofloz(1)
# print(z[1])
age = 33
# beanage = beans(1)
# print("your age, " + str(age) + " is " + str(beanage[0]) + " in " + beanage[2] + " of " + beanage[1])

fooddefs = [milklbs, lbstopineapple, beans]
randdef = random.choice(fooddefs)

randconvert = randdef(age)
print("your age, " +str(age) + ", is " + str(randconvert[0]) + " in " + randconvert[2] + " of " + randconvert[1] + ".")
print(str(deathsaday(age)) + " people have died since you were born.")
print("If there were " + str(age) + " titanics, " + str(titanicdeaths(age)) + " people would have died.")
print("But also if there were titanics for every year you've been alive, that would be " + str(titanicdew(1)) + " cans of mountain dew.")