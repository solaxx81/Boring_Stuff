import re

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

phone_num_pattern_obj = re.compile(r"\d{3}-\d{3}-\d{4}")
if match_obj := phone_num_pattern_obj.findall(message):
    print(match_obj)


pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
print(pattern.findall("Cell: 415-555-9999 Work: 212-555-0000"))
pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
print(pattern.findall("Cell: 415-555-9999 Work: 212-555-0000"))
