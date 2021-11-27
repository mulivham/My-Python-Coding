def earth(continent= "World", it_is_hot=True): 
    if not it_is_hot:
        return "Its freezing out there, so cold"
    return "Welcome to, " + continent + " i hope you enjoy your stay"

continent = input("enter location: ")
it_is_hot = False

check = [continent, it_is_hot]

print(earth(*check))

