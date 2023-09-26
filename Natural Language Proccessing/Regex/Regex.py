#regex (regular expressions), used to match characters 

#character set / with range, can only match 1 character
[bc]at = bat / cat
[b-e]at = bat / cat / dat / eat

#alternation with groupings, both terms in the (|) are accepted
The (mother|child) likes to eat apples = The mother likes to eat apples / The child likes to eat apples

#wildcards, will match anything including special characters
. = [a-zA-Z1-9/W] 

#shorthand character
\w = [a-zA-Z]
\d = [1-9]
\W = [<>.,/'":;[]\{}-_=+()*&^%$#@!`~|]
\s = " "

#quantifiers
# fixed, indicate qty of a charater to match
roa{3}r = roaaar
ca{4,6}t = caaaat / caaaaat / caaaaaat
ba{3,}t = baaat/ baaaat/ baaaa...t
ba{,3}t = bat / baat / baaat
# optional
The (rotten)? banana was eaten = The rotten banana was eaten / The banana was eaten
# kleene star, 0 or more times
Today is a ho*t day = Today is a ht day / Today is a hot day / Today is a hooo...t day
# kleene plus, 1 or more times
co+ld = cold / coold / cooo...ld

#anchors, will ensure first and last word matches
^Monkeys are scary$ != Spider Monkeys are scary / Monkeys are friendly

#examples of regex
[\w\W\d\s]{1,} = match anything
.{3}\s This is text in html\s\W{2}p. = <p> This is text is html </p> 