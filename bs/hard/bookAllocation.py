"""
Given an array 'arr' of integer numbers, 'arr[i]' represents the number of pages in the 'i-th' book.



There are 'm' number of students, and the task is to allocate all the books to the students.



Allocate books in such a way that:

1. Each student gets at least one book.
2. Each book should be allocated to only one student.
3. Book allocation should be in a contiguous manner.


You have to allocate the book to 'm' students such that the maximum number of pages assigned to a student is minimum.



If the allocation of books is not possible, return -1

Input: 'n' = 4 'm' = 2 
'arr' = [12, 34, 67, 90]

Output: 113

"""
def checkCountOfStudents(arr, pages):
    # check and add
    student = 1
    assigned_pages = 0
    i = 0
    while i < len(arr):
        if (assigned_pages + arr[i] <= pages):
            assigned_pages = assigned_pages + arr[i]
        else:
            student += 1
            assigned_pages = arr[i]
        i += 1
    return student

def findPages(arr, students):
    low = max(arr) # because at least a student has to get ( length of arr = num of students)
    high = sum(arr) # if only one student

    if len(arr) < students:
        return -1
    
    while low <= high:
        mid = int((low+high)/2)
        check_students = checkCountOfStudents(arr, mid)
        # visualise to elimate which half
        if check_students > students:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans
    # return low

arr = [12, 34, 67, 90]
student = 2
print(findPages(arr, student))