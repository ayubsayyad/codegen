import xlrd
import argparse
from os import listdir, path, makedirs
from os.path import isfile, join, splitext
import ntpath
datatypeMapping = {"byte": 'char'}

def getDatatype(input):
    if input in datatypeMapping: return datatypeMapping[input]
    return input

def writeWithNewLine(f, str):
    f.write(str + "\n")

def createClass(cfilename, className, classFields):
    spaces = "    "

    if not path.exists("includes"):
        makedirs("includes")
    f = open("includes/" + cfilename,"w")

    guard = "_" + cfilename.replace(".", "_").upper() + "_INCLUDE_"
    writeWithNewLine(f, "#ifndef " + guard)
    writeWithNewLine(f, "#define " + guard)
    writeWithNewLine(f, "#pragma pack(1) ")
    writeWithNewLine(f, "struct sRawStruct" + className)
    writeWithNewLine(f, "{")
    for fields in classFields:
        writeWithNewLine(f, spaces + fields["datatype"] + " " + "m_" + fields["fieldName"] + ";")
    writeWithNewLine(f, "};")

    writeWithNewLine(f, "#pragma pack() ")

    writeWithNewLine(f, "class " + className)
    writeWithNewLine(f, "{")
    writeWithNewLine(f, "public:")
    membername = "m_" + className.lower()
    writeWithNewLine(f, spaces + className + "() : m_ptr(&" + membername + "){ memset(m_ptr, 0, sizeof(" + membername + ")); };")
    writeWithNewLine(f, spaces + className + "(void* ptr) : m_ptr(ptr){ };")
    for fields in classFields:
        writeWithNewLine(f, spaces + fields["datatype"] + " " + "get" + fields["fieldName"] + "(){ return " + "m_ptr->m_" + fields["fieldName"] + "; }")
        writeWithNewLine(f, spaces + "void" + " " + "set" + fields["fieldName"] + "(const " + fields["datatype"] +"& val){ m_ptr->m_" + fields["fieldName"] + " = val; }")
    writeWithNewLine(f, "protected:")
    writeWithNewLine(f, spaces + "sRawStruct" + className + "* m_ptr;")
    writeWithNewLine(f, spaces + "sRawStruct" + className + " " + membername + ";")
    writeWithNewLine(f, "};")
    writeWithNewLine(f, "#endif " + guard)

def parseNCreate(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    #print(sheet.nrows)

    cfilename = path.splitext(ntpath.basename(filename))[0] + ".hpp"
    #print("Generating: " + cfilename)

    className = sheet.cell_value(0, 1)

    #print(sheet.cell_value(9, 0))
    idx = 9
    classFields = []
    while idx < sheet.nrows:
        fields = {}
        fields["fieldName"] = sheet.cell_value(idx, 0).replace(" ", "")
        fields["datatype"] = getDatatype(sheet.cell_value(idx, 1))
        fields["offset"] = sheet.cell_value(idx, 2)
        fields["size"] = sheet.cell_value(idx, 2)
        classFields.append(fields)
        idx = idx+1

    createClass(cfilename, className, classFields)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")

    args = parser.parse_args()
    for f in listdir(args.path):
        print(join(args.path, f))
        parseNCreate(join(args.path, f))

if __name__ == "__main__":
    main()