# import the random library
import random

# Function to convert into spongemock
def spongemock(input_text):
	
	# variable declaration for the output text
	output_text = ""
	
	# check the cases for every individual character
	for char in input_text:
		
		# check if the character is an alphabet
		if char.isalpha():
			
			# convert to upper case
			if random.random() > 0.5:
				output_text += char.upper()
				
			# convert to lower case
			else:
				output_text += char.lower()
		
		# if character is not and alphabet
		# add it as it is
		else:
			output_text += char
	
	# return the output_text
	return output_text
	
# Driver code
if __name__=="__main__":
	input_text1 = "The quick brown fox jumps over the lazy dog."
	input_text2 = "This sentence is to test the function."
	print(spongemock(input_text1))
	print(spongemock(input_text2))
