def check_anagram(str1="Mary", str2="Army"):
	str1_counter = {}
	str2_counter = {}

	if len(str1) != len(str2):
		print("Not anagram")
	else:
		for i in range(len(str2)):
			letter = str1[i].lower()
			if letter not in str1_counter.keys():
				str1_counter[letter] = 1
			else:
				str1_counter[letter] =+ 1

			letter = str2[i].lower()
			if letter not in str2_counter.keys():
				str2_counter[letter] = 1
			else:
				str2_counter[letter] =+ 1

		if str1_counter == str2_counter:
			print("Yes")

# str1 = "Mary"
# str2 = "Army"

str1, str2 = str(input("Enter the 2 strings space separated: ")).split()
# print(str1, str2)
check_anagram(str1, str2)
