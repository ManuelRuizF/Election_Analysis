# Election_Analysis

## Project Overview
A Colorado Board of Election employee gave me the following tasks to complete the election audit of a recent local congressional election.  

1. Calculate the total number of votes cast.
2. Get a complete list of candidares who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.
  
We wanted to get these results in order to calcultate the *potential* winner of the election and see how strong his/her political party is.  
We are going to measure the power of each candidate distributed along the counties involved in the election.

## Election Audit Results
### Outcomes:  
**-How many votes were cast in this congressional election?**  
During the congessional election the number of total votes was 369,711 along the counties.
**-Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**  
County Votes:  
Jefferson: 10.5% (38,855)  
Denver: 82.8% (306,055)  
Arapahoe: 6.7% (24,801)  
**-Which county had the largest number of votes?** 
With 82.8% of the votes which is 306,055, Denver is the county that had the largest number of votes.
**-Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**  
During the election there were 3 candidates: Charles, Diana and Raymon. The breakdown of result per candidate is the following.  
Charles Casper Stockham: 23.0% (85,213)  
Diana DeGette: 73.8% (272,892)  
Raymon Anthony Doane: 3.1% (11,606)  

**-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**  
Diana DeGette won the election with the following vote count and percentage.  
Winner: Diana DeGette  
Winning Vote Count: 272,892  
Winning Percentage: 73.8%  

## Election Audit Summary
## Code breakdown

**Along all the code we used a variety of code lines, but mainly or most important we used "if statements and loops."**  
First we loaded the .csv file we wanted to read and the text file we added out results in text.  
Afterward we intialized all the variables we knew we were going to use, such as the candidate options, votes, the counties, and the count of votes in each county. Along with the winning data.  
When everything was ready, we looped through the name of the candidates to know how many were. Also the vote count for each one with an if statement. We did the very same with the counties.  
After closing every loop we saved our results in our text file.  
## How can we modify the code?  
The script loops through the different names and counties. It will work as well if there are more or less candidates. So since the scripts brings back any number of candidates and counties, we can say that we can use it in any election.  
Now, we can modify our code in order to get more or different results depending on what we need. We are going to give 2 examples of this.  
### Example 1  
If you wanted to know which county had the least turnout of votes you have to create 3 variables to hold the results and the modify the if statement with the "and" to look for the "bigger than" statement and turn it into "less than" to look for the smallest values. 

### Example 2
If the political party wants to know the amount of votes his candidate had in each county so they know where to work more. We can loop into the counting votes and with an if statement just look for one candidate. So let´s say for example how many votes Raymon had in Araphoe? So you know if Raymon is likeable or not.




## Summary
The following pictures shows all the information in a txt file attached to our challenge code:  
![Summary_election](https://github.com/ManuelRuizF/Election_Analysis/blob/main/resources/Captura.PNG)


## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1  

