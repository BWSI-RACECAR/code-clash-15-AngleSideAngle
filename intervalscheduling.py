"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #15 - Interval Scheduling(intervalscheduling.py)


Author: Koneshka Bandyopadhyay

Difficulty Level: 9/10

Prompt: It is the GrandPrix Week and BWSI is hosting many events on one of the days for several hours. However, 
a bunch of these events overlap and you cannot go to all of them. Each event has equal value to you so you need 
to try and figure out an algorithm that can help you identify which events you should go to, in such a way that 
you make the best out of your day and visit as many events as possible. Your input is a list of intervals with 
a start_time and a finish_time.

Example: The graph in the assignment consists of various events A to H 
happening from time 0 to time 11. Under that, we have the solution [B, E, H]
which gives us 3 events, making it the maximum number of events possible during
this given time. For reference, B has a start_time of 1 and a finish time of 4.

You are permitted to use any sorting methods.

Test Cases:
Input: [(1, 4), (2, 5), (3, 6), (4, 7)] Output: [(1, 4), (4, 7)]
Select (1,4) and (4,7) as those are compatible events and the maximum number of events

Input: [(1, 3), (2, 4), (3, 5)] Output: [(1, 3), (3, 5)]
Select (1,3) and (3,5) as those are compatible events and the maximum number of events

Input: [(1, 2), (2, 3), (3, 4)] Output: [(1, 2), (2, 3), (3, 4)]
Select all three (1, 2), (2, 3) and (3, 4) as those are all compatible events and the maximum number of events

"""

class Solution:
    def interval_scheduling(self, intervals):
            #type intervals: list of int tuples
            #return type: list of int tuples
            
            #TODO: Write code below to return an int tuples list with the solution to the prompt.
            def time(interval):
                return interval[1] - interval[0]
            
            def overlap(one, two):
                return two[0] in range(one[0], one[1]) or two[1] in range(one[0], one[1])
                 
            for i in range(len(intervals)):
                for j in range(len(intervals)):
                    if time(intervals[i]) > time(intervals[j]):
                        tmp = intervals[i]
                        intervals[i] = intervals[j]
                        intervals[j] = tmp


            res = []
            for start in range(len(intervals)):
                tmp = [start]
                for i in range(start, len(intervals)):
                    if not overlap(tmp[-1], intervals[i]):
                        tmp.append(intervals[i])
                if sum(tmp) > sum(res):
                    res = tmp

            return res
                    


    
         



def main():
    string = input()
    string = string.replace(" ", "")  # Remove any whitespace in the string
    string = string.replace("),", ")|")  # Replace the comma between tuples with a custom separator
    
    list_from_string = string.split("|")  # Split the string into individual tuple strings
    
    # Convert the tuple strings to actual tuples
    result = [eval(tuple_str) for tuple_str in list_from_string]

                
    tc1= Solution()
    ans=tc1.interval_scheduling(result)
    print(ans)
    
if __name__ == "__main__":
    main()