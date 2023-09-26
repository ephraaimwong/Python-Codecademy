import re

character_1 = "Dorothy"
character_2 = "Henry"

#re.compile() turns the word pattern into a regex object, necessary before other functions like re.match() or re.search()
regular_expression = re.compile(".{7}")

#re.match() only matches at the BEGINNING of string
#compile & match can be written in 1 line - x = re.match("pattern", "y") which will match y to pattern
result_1 = regular_expression.match(character_1)


#.group() stores results in groups that can be called
match_1 = result_1.group(0)
print(match_1)

# compile a regular expression to match a 7 character string of word characters and check for a match to character_2 here
result_2 = re.compile(".{7}").match(character_2)
