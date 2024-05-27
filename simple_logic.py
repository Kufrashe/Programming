question = "What is the day today?"
if question:
    print("Wednesday")
else:
    print("No Date Specified")

def inp(data):
    data = input("Enter Your Data Here : ")
    if data is int:
        print("Entered Data is of Integer type")
    else:
        print("Entered Data is not of Integer type")
    if "+" or "-" or "*" in data:
        print("Mathematical Operators In The Input Data")
    else:
        print("No Mathematical Operators found in input Data")
    if data is str:
        print("String Data is present in input data")
    else:
        print("No Input_Data of a known type was specified")
    return 0, "Program Ran Successfully"

inp(("My Name is Kufrashe and l am",14,"years old"))