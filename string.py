print("String by DEveloper")
data = "Developer number {}"
info = "Syab Ahmad de "
number = 1
infoData = info + data
print(len(data))
print(type(data))
print(data[1])
print(data[2:])
print(data[2:4])
print(data[:2])
print(data.upper())
print(data.lower())
print(data.replace("developer", "Syab Ahmad de Developer"))
print(data.strip())
print(info, data)
print(infoData)
print(infoData.format(number))