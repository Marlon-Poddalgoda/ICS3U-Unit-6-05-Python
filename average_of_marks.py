#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program finds the average of a list of marks


def averageOfMarks(list_of_marks):
    # This function finds the average

    total = 0
    num_of_values = len(list_of_marks)

    for loop_counter in list_of_marks:
        total += loop_counter

    average = total / num_of_values

    return average


def main():
    # This function handles input and prints the average

    print("This program accepts a list of marks and"
          " calculates the average. Enter -1 to calculate"
          " the average.")
    print("")

    list_of_marks = []
    temp_mark = 0

    # input
    while True:
        try:
            temp_mark = input("Enter a mark (%): ")
            temp_mark_int = int(temp_mark)
            list_of_marks.append(temp_mark_int)

            while temp_mark_int != -1:
                temp_mark = input("Enter a mark (%): ")
                temp_mark_int = int(temp_mark)
                list_of_marks.append(temp_mark_int)

            list_of_marks.pop()
            print("")

            average_of_list = averageOfMarks(list_of_marks)
            average_rounded = '{0:.4g}'.format(average_of_list)

            print("")
            print("The average of all the numbers is: {0}"
                  .format(average_rounded))

            break

        except Exception:
            # output
            print("Enter a number for all values, try again.")


if __name__ == "__main__":
    main()
