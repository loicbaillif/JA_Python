#  ******** JetBrains Academy - Python for Beginners ********
#  ****** IF statement ******

separator = "_"*40
print(" JetBrains Academy - Python for Beginners ".center(80, "*"))
print(" IF statement: Exercise - University".center(80, "*"))
print(separator.center(80)+"\n\n")

harvard = "linguistics, physics, programming, fine arts"
stanford = "biology, classics, geophysics, music"

arts = "linguistics, fine arts, classics, music"
sciences = "physics, programming, biology, geophysics"

major = "..."  # What if major = "biology"?
if major in harvard:
    if major in arts:
        print("This is an arts program at Harvard")
    if major in sciences:
        print("This is a sciences program at Harvard")
if major in stanford:
    if major in arts:
        print("This is an arts program at Stanford")
    if major in sciences:
        print("This is a sciences program at Stanford")  # output