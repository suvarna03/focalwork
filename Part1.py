#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# Write a function to calculate a score for a candidate’s response for an essay type question based on how
# closely it matches the correct answer.
# Assume that the function takes two string arguments:
# Candidate’s response (Response)
# Correct Answer (CorrectAnswer)
# The function needs to identify each word in the Candidate’s response that matches with a word in the Correct
# Answer and assign points based on the following rule:
#     Numbers - 4 points
#     Words with more than 7 characters - 3 points
#     Words with less than 5 characters - 0 points
#     All other words - 1 point
# Calculate “Maximum Possible Score” as Sum of points for each word in the Correct Response String
# Calculate “Points Scored” as Sum of points for each word in the “Candidate Response” that has a match with
# a word in the Correct Answer string.
# After calculating both “Maximum Possible Score” and “Points Scored”, the function should return the
# percentage ratio of the “Points Score” and the “Maximum Possible Score”

# In[1]:


global corre ## Variable Declaration

def cor(list_of_words):##Function to Identify the value of each words and numbers
    #declare default values of 'num','great_7','less_great' is 0
    num = 0 #Variable to count value of numbers present in string
    great_7 = 0 #Variable to count value of characters(length is greater than 7)
    less_great = 0 # VAriable to count value of characters(length is between 5-7)
    for i in list_of_words: #Itreate over the list
            if(i.isdigit()== True):#Check is character belongs to number
                num += 4 # if yes then assign 4
            else: #If not then
                if len(i) > 7: #check length of words are greater than 7 
                    great_7 += 3 # if yes then assign value as 3
                else: #if no 
                    if len(i) >= 5 and len(i) <= 7: # check length of words between 5-7
                        less_great += 1 #if yes then assign value as 1
    corre = num+great_7+less_great #Calculate the total score
    return(corre)
    


# In[6]:


str1 = "There are twenty-four hours in a day, 30 days in a month, and 12 months in the calendar year."
# There = 1 (len is between 5-7)
#are = 0 (len less than 5)
#twenty-four = 3 (len greater than 7)
#hours = 1 (len is between 5-7)
#in =0 (len less than 5)
#a=0 (len less than 5)
#day=0 (len less than 5)
#30 = 4 (hold number)
#days=0 (len less than 5)
#in=0 (len less than 5)
#a=0 (len less than 5)
#month=1 (len is between 5-7)
#and=0 (len less than 5)
#12 =4 (hold number)
#months =1 (len is between 5-7)
#in = 0 (len less than 5) 
#the=0 (len less than 5)
#calender =3 (len greater than 7)
#year = 0 (len less than 5)

# 1+3+1+4+1+4+1+3 = 18
str2 = "There are Twenty-Four hours in a day. A year has 14 months." #Candidate Response
# ******************Match Words***************************************
# There =1 (len is between 5-7)
# are =0 (len less than 5)
# twenty_four=3 (len greater than 7)
# hours =1(len is between 5-7)
# in =0 (len less than 5)
# a=0 (len less than 5)
# day=0 (len less than 5)
# year=0 (len less than 5)
# months=1 (len is between 5-7)

# 1+3+1+1 = 6
#  split() will convert string into list of words
# strip() will remove ',','.' from string
list1 = [s.strip(',.').lower() for s in str1.split()]
list2 = [s.strip(',.').lower() for s in str2.split()]
val1=(cor(list1))
match = [s for s in list2 if s in list1]
val2 = cor(match)

print("Maximum Possible Scoring", val1)
if (val2/ val1)*100 > 50:
    print("The Pinted Score (A) is {}.The Precentage Score(B/A %)is {}%".format(val2,(val2/ val1)*100) )
else:
    print("The Pinted Score (B) is {}.The Precentage Score(B/A %)is {}%".format(val2,(val2/ val1)*100) )
    
    

