"""This is the "nester.py" module and it provides one function called
print_lol() which prints lists that may or may not include nested lists."""
def print_lol (the_list, want_indent=False, list_indent=0):
    """This function takes a positional argument called "the_list", which
is any Python list (of - possibly - nested lists). Each data item in the
provided list is (recursively) printed to the screen on it's own line.
The list_indent argument refers to the indentation of the lists, if need be"""
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, want_indent, list_indent+1)
        else:
            if want_indent:
                for tab_stop in range(list_indent):
                    print("\t", end='')
            print(item)
