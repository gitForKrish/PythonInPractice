students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"

print(students_count, rating, is_published, course_name)
print(type(students_count), type(rating),
      type(is_published), type(course_name))

# String in details
course_name = "Python Programming"
print(len(course_name))
multiline_string = """
Hi John,
This is Scott.
What will you do tomorrow?
"""
print(multiline_string)

print(course_name[0])
print(course_name[-1])
print(course_name[0:6])
print(course_name[7:])
print(course_name[:6])
print(course_name[:])

# Escape Sequences
# \' \" \\ \n \t
course_name = "Python \'Programming\'"
print(course_name)

# Formatted String
first = "Krish"
last = "Mandal"
full = first + " " + last
print(full)

full = f"{first} {last}"
print(full)

print(f"{len(first)} {2*3}")
