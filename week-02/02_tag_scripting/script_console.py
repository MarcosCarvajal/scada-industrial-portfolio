print("Step 1")
print "script console is working"
print system.util.getVersion()
print("\n")
print("Step 2")
tag_path = "[default]TEMP_ZONE_A"
tag_value = system.tag.readBlocking([tag_path])
print(tag_value)
print(tag_value[0].value)
print("\n")
print("Step 3")
system.tag.writeBlocking(tag_path, [29.8])
result = system.tag.readBlocking([tag_path])
print("current value: "+str(tag_value[0].value))
print("\n")

print("Step 4")
def read_tag(name):
	try:
		return float(system.tag.readBlocking(["[default]"+name])[0].value)
	except (valueError, TypeError):
		print("the tag name: "+name+" don't exists")

def write_tag(name, newValue):
	try:
		system.tag.writeBlocking("[default]"+name, [newValue])
		print("new tag vale for "+name+" set correctly")
	except (valueError, TypeError):
		print("the tag name: "+name+" don't exists")

current = read_tag("TEMP_ZONE_A")
print("Read: " + str(current))

write_tag("TEMP_ZONE_A", 31.5)

updated = read_tag("TEMP_ZONE_A")
print("After write: " + str(updated))
print("\n")

print("Step 5")
tags = ["TEMP_ZONE_A", "HUMIDITY_ZONE_A", "PH_ZONE_A"]
for tag in tags:
    value = read_tag(tag)
    print(tag + ": " + str(value))
print("\n")