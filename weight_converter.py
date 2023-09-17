# weight converter program, ':' at the end of if condistion leads to indentation(block code)
weight = input("weight:")
unit = input("(K)g or (L)bs:") 
if unit.upper() == "K": 
	converted = int(weight)/0.45 #indent 4 stages
	print("weight in Lbs:" + str(converted))

else: 
	converted = int(weight) * 0.45
	print("weight in kgs:" + str(converted))
