import collections
# def have_common_number(list1,list2):
#     for item in list1:
#         if item in list2:
#             return True
        
    # return False

list1 = [1,2,3,4,5]  
list2 = [0,1,7,8,5]  
if collections.Counter(list1)==collections.Counter(list2):
    print("They match")
else:
    print("They dont match")

# result = have_common_number(list1,list2)  
 