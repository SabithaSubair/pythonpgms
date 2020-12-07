name=["a","b","c","d","e"]
passed=["a","b","c"]
#convert to set and find no of passed
name_set=set(name)
passed_set=set(passed)
fail_set=name_set-passed_set
print(fail_set)