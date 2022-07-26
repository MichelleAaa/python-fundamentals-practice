unsorted_list = [101, 49, 3, 12, 56]

# unoptimized version:
# def bubblesort(the_list):
#     high_idx = len(the_list) - 1

#     for i in range(high_idx):
#             for j in range(high_idx):
#                 item = the_list[j]
#                 next = the_list[j+1]

#                 if item > next:
#                     the_list[j] = next
#                     the_list[j+1] = item

#                 print(the_list, i, j)


def bubblesort(the_list):
    #highest index of the list passed in. 
    high_idx = len(the_list) - 1
# Start and step values are 0 and 1, respectively, and the stop value is the high_idx value.
    for i in range(high_idx):
        list_changed = False
        # We are using the high_idx for the stop value again.
        for j in range(high_idx):
            # These represent the pair being sorted.
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                # This signals that the list has changed:
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        # This means everything is already sorted and we are good to exit:
        if list_changed == False:
            break

bubblesort(unsorted_list)
