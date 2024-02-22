#!/usr/bin/env ruby

# Define the regular expression
regex = /School/
first_argument = ARGV[0]

# Check for matches from the first command line argument
matches = first_argument.scan(regex)

# Display the matches
puts matches.join
