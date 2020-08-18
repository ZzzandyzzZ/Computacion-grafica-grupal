import os
file = open("filename.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()