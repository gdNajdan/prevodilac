
engleski_srpski = {
    "watermelon" : "lubenica",
    "drawing" : "crtanje",
    "writing" : "pisanje",
    "computer" : "racunar",
    "system" : "sistem",
    "speakers" : "zvucnici",
    "image" : "slika",
    "pen" : "hemijska",
    "window" : "prozor",
    "folder" : "fascikla",
    "cat" : "macka",
    "dog" : "pas"

}

srpski_engleski = {
    "lubenica" : "watermelon",
    "crtanje" : "drawing",
    "pisanje" : "writing",
    "racunar" : "computer",
    "sistem" : "system",
    "zvucnici" : "speakers",
    "slika" : "picture",
    "hemijska" : "pen",
    "prozor" : "window",
    "fascikla" : "folder",
    "macka" : "cat",
    "pas" : "dog"
}
print("dobrodosli u prevodilac sa srpskog na engleski ili sa engleskog na srpski!")
smer = (input("unesite sa kog jezika prevodite: "))
rec = (input("unesite rec: "))
if smer == "sa srpskog na engleski":
    print("prevod vam je: ", srpski_engleski[rec])
if smer == "sa engleskog na srpski":
    print("prevod vam je: ", engleski_srpski[rec])