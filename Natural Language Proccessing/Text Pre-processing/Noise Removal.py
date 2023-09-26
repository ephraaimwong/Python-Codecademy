import re

headline_one = '<h1>Nation\'s Top Pseudoscientists Harness High-Energy Quartz Crystal Capable Of Reversing Effects Of Being Gemini</h1>'

headline_no_tag = re.sub(r"<.?h1>", "", headline_one) #removes <h1> and </h1>

tweet = '@fat_meats, veggies are better than you think.'

tweet_no_at = re.sub(r"@", "", tweet) #removes @