#!/usr/bin/env ruby

# Define the regular expression
regex = /^h.n$/
# ^: Asserts the start of the line.
# h: Matches the character "h" literally.
# .: Matches any single character except for a newline.
# n: Matches the character "n" literally.
# $: Asserts the end of the line.
first_argument = ARGV[0]

# Check for matches from the first command line argument
matches = first_argument.scan(regex)

# Display the matches
puts matches.join
