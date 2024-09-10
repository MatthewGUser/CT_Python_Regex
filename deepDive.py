# [ Task 1 ]

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@exclude.com"


# Regular expression to extract emails but exclude the ones from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Find all email addresses in the text, excluding 'exclude.com'
emails = re.findall(pattern, text)


# Print the extracted emails
print("Extracted Emails (excluding 'exclude.com'):", emails)
