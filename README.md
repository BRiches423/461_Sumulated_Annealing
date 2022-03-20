# 461_Sumulated_Annealing

# Bryan Richlinski

### Language Chosen Python

# Notes for file structure:
Please just use the files in the SA_Project folder. Files are as follows, the final bag lists ready to be inserted into a dataframe, are in ouput1 ouput2 and ouput3.  The details of each annealing epoch are in stats(1) stats(2) and stats(3).  
1 = Geometric cooling with a .9 rate, 2 = Geometric with at .85 rate, 3 = modified linear.

In SA_Project, main.py runs the entire algoritm, it is set to use a geometric cooling of 0.9 but that can be changed by changing the comments. As well Graphs.py displays some nice graphs showing the progress from epoch to epoch in data I created.  

If you would like to see everything in a beautiful Jupyter Notebook, please use the "Simulated Annealing.ipynb" file. 

# Discussion

For my project I chose to use Python as my language, mostly because this is my first semester using it and I need the practice. For my data structure I used a numpy array. I did this because this prjoject won't be run concurrently so I didn't need to seperate the data from the binary included/not included string. As well the array format is fast enough and makes it easier for me to understand what I'm doing and perform operations.  

I created an Anneal class with the following basic functions: penalty returns the penalty based on weight, get_objective: returns the CURRENT not the recorded objective function but doesn't change the recorded objective function, get_weight: returns weight, invert: adds or removes the selected item from the bag, prob_accept: returns true if a random roll is less than the annealing probability function at the current temp/delta, load: loads data into NP array, initalize: randomly includes about 1/20 of the items in the bag, and anneal: the function that uses all of the previous to perform the meat of the annealing process.  Note the annealing functiononly performs ONE 40000 iteration epoch, the annealing schedule is controlled outside of the class. The thought behind this is that I could make a few alterations and create a generalized class that accepts as a hyperparamater a function to control the annealing schedule. 

After the anneal class I created a while loop that monitors the number of accepted changes from the anneal function every epoch, adjusts the weight according to the schedule specified, and re-runs the anneal() method, untill the stopping critera is met. 

Finially, I output the final csv with the included/excluded string to an output file and another csv with the temp, objective, weight,and percent_annealed for each epoch to a stats file. At the very bottom I created a few graphs detailing the changes for each annealing schedule I used. If you want to view the results it is a csv with a header (intended for pandas). 

I had some difficulty at first with this assignment becuase I chose to use a DataFrame instead of a Numpy Array.  That slowed progress to a crawl, it literally took over 5 hours for my first attempt, fortunately I was doing other things with my time.  After switching to the NP Array it took only a few minutes.  Another issue I faced was that my annealing probability function was triggering too often, I included an absolute value function in my numerator and that fixed it.

I chose 3 different annealing schedules to run: geometric with a 0.9 rate, geometric with a 0.85 rate, and a modified linear that decriments by 300 till it reaches 100, then decrements by 10 untill it reaches 10, then 1 till 1, then .01 till .05, then finally at .05 it switches to geometric if needed. The final objective functions and iterations of each were:
Geometric 0.9: (obj: 268, itr: 96), 
Geometric 0.85: (obj: 283, itr: 62), 
modified-linear: (obj: 265, itr: 118). 

So, while the modified linear had marginally better results (probably within a margin of error) it took much longer and even had to revert to the geometric after a time (note I only fell back on the geometric because I was unsure how to maintain a linear cooling without an excessively long if/else statement). I would say that unless the problem is incredibly large the geometric 0.9 cooling rate is a sufficient schedule as it gives good results without much more of a time committment compared to the geometric of 0.85.  When choosing the initial temperature I went with 4000 degrees as I read that you should choose a temperature that accepts > 90% of the detrimental changes, and I used guess and check to find a temperature that satifies this condition. 

I didn't have an opportunity to optimize the program other than implementing it in a NP rather than PD. If I had some extra time I would have like to use only the modified variable to determine the difference between the current weight/objective and the previous, as that would mean I wouldn't need to recalculate based upon the entire array each time a change is made. 

I'm mostly just proud that I am able to use Python with relatively little prior experience, but I am also proud that I was able to create some graphs to visualize the annealing process, to see how the different cooling schedules affect the objective and percent of bad changes accepted (which I named percent_annealed sorry if that is the wrong naming convention.)

