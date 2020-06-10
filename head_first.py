import nested_list

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

nested_list.print_lol(movies, True, 0)

# indented for loops
# for each_item in movies:
#     if isinstance(each_item, list):
#         print("cast")
#         for each_subitem in each_item:
#             if isinstance(each_subitem, list):
#                 print("supporting")
#                 for each_sub_sub in each_subitem:
#                     print(each_sub_sub)
#             else:
#                 print(each_subitem)
#     else:
#         print(each_item)



#how to check for smething
# names = ['Michael', 'Terry']
# if isinstance(names, list) == True:
#     print("yay!")
