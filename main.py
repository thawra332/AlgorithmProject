import random
import time
import matplotlib.pyplot as plt
import quicksort
import mergesort
import selectionsort
import bubblesort
import insertionsort
import concurrent.futures
selection_comparisons = []
bubble_comparisons = []
insertion_comparisons = []
merge_comparisons = []
quick_comparisons = []
quicktime = []
selectiontime = []
mergetime = []
insertiontime = []
bubbletime = []
print("This program is made by Amenh Rabayaa")
print("information about this program:\n1-The number of elements in the array is 10 - 1000 element \n2-The time taken to sort the array is provided\n3- am using Matplot libarary in python to draw the graph\n"+
      "4-there is three different way using random,Sorting,Reverce input\n \n \n" )
input_arr_sorted=[]
for i in range(0,1001,10):
    input_arr_sorted.append(i)
input_arr_reversed=[]
nr=1000
while nr>0:
    input_arr_reversed.append(nr)
    nr-=10
print("Enter 1 for random input \nEnter 2 for Sorting input\nEnter 3 for Reversing input\nEnter 4 for Exit")
data=int(input('Enter your choice: '))
match data:
        case 1:
                start = time.time()
                for n in range(0,1001,10):
                    with concurrent.futures.ThreadPoolExecutor() as exec:
                        input_arr = [random.randint(0, 100) for i in range(n)]
                        quicksort.i = n
                        selection_comps = exec.submit(selectionsort.selection_sort, input_arr)
                        bubble_comps = exec.submit(bubblesort.bubble_sort, input_arr)
                        insertion_comps = exec.submit(insertionsort.insertion_sort, input_arr)
                        quick_comps = exec.submit(quicksort.quick, input_arr)
                        merge_comps = exec.submit(mergesort.mergee, input_arr)

                        # Selection Sort
                        selection_sort=selection_comps.result()
                        selection_time =selection_sort[1]
                        selectiontime.append(selection_time)
                        selection_comparisons.append(selection_sort[0])

                        # Bubble Sort
                        bubble_sort =bubble_comps.result()
                        bubble_time = bubble_sort[1]
                        bubbletime.append(bubble_time)
                        bubble_comparisons.append(bubble_sort[0])

                        # Insertion Sort
                        insertion_sort = insertion_comps.result()
                        insertiontime.append(insertion_sort[1])
                        insertion_comparisons.append(insertion_sort[0])

                        # Merge Sort
                        merge_sort = merge_comps.result()
                        mergetime.append(merge_sort[1])
                        merge_comparisons.append(merge_sort[0])

                        # Quick Sort
                        quick_sort = quick_comps.result()
                        quicktime.append(quick_sort[1])
                        quick_comparisons.append(quick_sort[0])


                        selection_comp,selection_t = selection_comps.result()
                        bubble_comp,bubble_t = bubble_comps.result()
                        insertion_comp,insertion_t = insertion_comps.result()
                        quick_comp,quick_t = quick_comps.result()
                        merge_comp,merge_t = merge_comps.result()


                        print(
                        f"n = {n}, Selection Comparisons and Time = ({selection_comp},{selection_t:.7f}),| \nBubble Comparisons and Time = ({bubble_comp},{bubble_t:.7f}), |\n "

                        f"Insertion Comparisons and Time = ({insertion_comp},{insertion_t:.7f}),| \nMerge Comparisons and Time = ({merge_comp},{merge_t:.7f}), |\n "

                        f"Quick Comparisons and Time = ({quick_comp},{quick_t:.7f}),\n"
                        )
                end = time.time()
                print(end-start)       
        case 2:
                start = time.time()
                for n in range(0,1001,10):
                    with concurrent.futures.ThreadPoolExecutor() as exec:
                        input_arr = input_arr_sorted
                        quicksort.i = n
                        selection_comps = exec.submit(selectionsort.selection_sort, input_arr)
                        bubble_comps = exec.submit(bubblesort.bubble_sort, input_arr)
                        insertion_comps = exec.submit(insertionsort.insertion_sort, input_arr)
                        quick_comps = exec.submit(quicksort.quick, input_arr)
                        merge_comps = exec.submit(mergesort.mergee, input_arr)

                        # Selection Sort
                        selection_sort=selection_comps.result()
                        selection_time =selection_sort[1]
                        selectiontime.append(selection_time)
                        selection_comparisons.append(selection_sort[0])

                        # Bubble Sort
                        bubble_sort =bubble_comps.result()
                        bubble_time = bubble_sort[1]
                        bubbletime.append(bubble_time)
                        bubble_comparisons.append(bubble_sort[0])

                        # Insertion Sort
                        insertion_sort = insertion_comps.result()
                        insertiontime.append(insertion_sort[1])
                        insertion_comparisons.append(insertion_sort[0])

                        # Merge Sort
                        merge_sort = merge_comps.result()
                        mergetime.append(merge_sort[1])
                        merge_comparisons.append(merge_sort[0])

                        # Quick Sort
                        quick_sort = quick_comps.result()
                        quicktime.append(quick_sort[1])
                        quick_comparisons.append(quick_sort[0])

                        
                        selection_comp,selection_t = selection_comps.result()
                        bubble_comp,bubble_t = bubble_comps.result()
                        insertion_comp,insertion_t = insertion_comps.result()
                        quick_comp,quick_t = quick_comps.result()
                        merge_comp,merge_t = merge_comps.result()


                        print(
                        f"n = {n}, Selection Comparisons and Time = ({selection_comp},{selection_t:.7f}),| \nBubble Comparisons and Time = ({bubble_comp},{bubble_t:.7f}), |\n "

                        f"Insertion Comparisons and Time = ({insertion_comp},{insertion_t:.7f}),| \nMerge Comparisons and Time = ({merge_comp},{merge_t:.7f}), |\n "

                        f"Quick Comparisons and Time = ({quick_comp},{quick_t:.7f}),\n"
                        )
                end = time.time()
                print(end-start)   
        case 3:
                start = time.time()
                for n in range(0,1001,10):
                    with concurrent.futures.ThreadPoolExecutor() as exec:
                        input_arr = input_arr_reversed
                        quicksort.i = n
                        selection_comps = exec.submit(selectionsort.selection_sort, input_arr)
                        bubble_comps = exec.submit(bubblesort.bubble_sort, input_arr)
                        insertion_comps = exec.submit(insertionsort.insertion_sort, input_arr)
                        quick_comps = exec.submit(quicksort.quick, input_arr)
                        merge_comps = exec.submit(mergesort.mergee, input_arr)

                        # Selection Sort
                        selection_sort=selection_comps.result()
                        selection_time =selection_sort[1]
                        selectiontime.append(selection_time)
                        selection_comparisons.append(selection_sort[0])

                        # Bubble Sort
                        bubble_sort =bubble_comps.result()
                        bubble_time = bubble_sort[1]
                        bubbletime.append(bubble_time)
                        bubble_comparisons.append(bubble_sort[0])

                        # Insertion Sort
                        insertion_sort = insertion_comps.result()
                        insertiontime.append(insertion_sort[1])
                        insertion_comparisons.append(insertion_sort[0])

                        # Merge Sort
                        merge_sort = merge_comps.result()
                        mergetime.append(merge_sort[1])
                        merge_comparisons.append(merge_sort[0])

                        # Quick Sort
                        quick_sort = quick_comps.result()
                        quicktime.append(quick_sort[1])
                        quick_comparisons.append(quick_sort[0])
                        selection_t,selection_comp = selection_comps.result()

                        
                        selection_comp,selection_t = selection_comps.result()
                        bubble_comp,bubble_t = bubble_comps.result()
                        insertion_comp,insertion_t = insertion_comps.result()
                        quick_comp,quick_t = quick_comps.result()
                        merge_comp,merge_t = merge_comps.result()


                        print(
                        f"n = {n}, Selection Comparisons and Time = ({selection_comp},{selection_t:.7f}),| \nBubble Comparisons and Time = ({bubble_comp},{bubble_t:.7f}), |\n "

                        f"Insertion Comparisons and Time = ({insertion_comp},{insertion_t:.7f}),| \nMerge Comparisons and Time = ({merge_comp},{merge_t:.7f}), |\n "

                        f"Quick Comparisons and Time = ({quick_comp},{quick_t:.7f}),\n"
                        )
                end = time.time()
                print(end-start)   
        case 4:
          exit()
# Plot the results
n_values = [i for i in range(0, 1001,10)]
plt.figure("Amneh: Project Algorithm")

plt.plot(n_values, bubble_comparisons, label='Bubble Sort')
plt.plot(n_values, insertion_comparisons, label='Insertion Sort')
plt.plot(n_values, merge_comparisons, label='Merge Sort')
plt.plot(n_values, quick_comparisons, label='Quick Sort')
plt.plot(n_values, selection_comparisons, label='Selection Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Total Number of Element Comparisons')
plt.title('Sorting Algorithm Comparison')
plt.legend()
plt.show()
plt.figure("Amneh: Project Algorithm")
plt.plot(n_values, selectiontime, label='Selection Sort')
plt.plot(n_values, bubbletime, label='Bubble Sort')
plt.plot(n_values, insertiontime, label='Insertion Sort')
plt.plot(n_values, mergetime, label='Merge Sort')
plt.plot(n_values, quicktime, label='Quick Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time')
plt.title('Sorting Algorithm Comparison')
plt.legend()
plt.show()
