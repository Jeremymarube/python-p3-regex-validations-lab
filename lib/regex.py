import re

# Match a full name like "John Cena"
name_regex = re.compile(r"^[A-Z][a-z]+ [A-Z][a-z]+$")

# Name: allows hyphenated last names like "Taylor-Joy"
name_regex = re.compile(r"^[A-Z][a-z]+ [A-Z][a-z]+(-[A-Z][a-z]+)?$")

# Name: allows hyphens, apostrophes, single/multiple name parts
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:[-'][A-Z][a-z]*)*(?: [A-Z][a-z]*(?:[-'][A-Z][a-z]*)*)?$"
)

phone_regex = re.compile(
    r"^(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$"
)

# Email: must start with a letter, allows dots and hyphens, simple domain rules
email_regex = re.compile(
    r"^[A-Za-z][\w\.-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)
