#!/usr/bin/env ruby

# Define the regular expression
regex = /^\d{10,10}$/
# ^: Asserts the start of the line.
# \d: Represents any digit (0-9).
# {10,10}: Quantifier that specifies exactly 10 occurrences of the preceding \d (digit).
# $: Asserts the end of the line.

first_argument = ARGV[0]

# Check for matches from the first command line argument
matches = first_argument.scan(regex)

# Display the matches
puts matches.join
