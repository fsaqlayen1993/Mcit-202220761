import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

email_pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+'

email_addresses = re.findall(email_pattern, text)

print(email_addresses)