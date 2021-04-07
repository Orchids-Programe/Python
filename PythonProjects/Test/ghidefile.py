file = open("plc.txt", "w", encoding='utf-8')
file.write( "pythons");

file = open("plc.txt", "r+", encoding='utf-8')
file.write("abc")

file = open("plc.txt", "a", encoding='utf-8')
file.write("xyz")