#!/usr/bin/env ruby

# Define the regular expression
regex = /[A-Z]*/
# [A-Z]: Denotes a character class that matches any uppercase letter from 'A' to 'Z'.
# *: Quantifier that matches zero or more occurrences of the preceding character class.

first_argument = ARGV[0]

# Check for matches from the first command line argument
matches = first_argument.scan(regex)

# Display the matches
puts matches.join
