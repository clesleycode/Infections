
Total Infection

When rolling out big new features, we like to enable them slowly, starting with just the KA team, then a handful of users, then some more users, and so on, until we’ve ramped up to 100%. This insulates the majority of users from bad bugs that crop up early in the life of a feature.

This strategy can cause problems somewhat unique to our user base. It’s not uncommon for a classroom of students to be using the site together, so it would be confusing to show half of them a completely different version of the site. Children are not software engineers and often have a poor understanding of deployment and a/b testing, so inconsistent colors, layout, and interactions effectively mean the site is broken.

Ideally we would like every user in any given classroom to be using the same version of the site. Enter “infections”. We can use the heuristic that each teacher-student pair should be on the same version of the site. So if A coaches B and we want to give A a new feature, then B should also get the new feature. Note that infections are transitive - if B coaches C, then C should get the new feature as well. Also, infections are transferred by both the “coaches” and “is coached by” relations.

First, model users (one attribute of a user is the version of the site they see) and the coaching relations between them. A user can coach any number of other users. You don’t need to worry about handling self-coaching relationships.

Now implement the infection algorithm. Starting from any given user, the entire connected component of the coaching graph containing that user should become infected.

Limited Infection

The problem with infection is lack of control over the number of users that eventually become infected. Starting an infection could cause only that person to become infected or at the opposite (unrealistic) extreme it could cause all users to become infected.

We would like to be able to infect close to a given number of users. Ideally we’d like a coach and all of their students to either have a feature or not. However, that might not always be possible.

Implement a procedure for limited infection. You will not be penalized for interpreting the specification as you see fit. There are many design choices and tradeoffs, so be prepared to justify your decisions.

Summary

Write total_infection and limited_infection in your preferred language. Provide tests and instructions for running them. 
 
Optionally do one of the following:
create a visualization of the relations between users and the infection’s spread
write a version of limited_infection that infects exactly the number of users specified and fails if that’s not possible (this can be (really) slow)
make up your own enhancement! 

-------------------------------------------------------------------------------------------------------------------

I designed this project so that it uses command line arguments to accept a filename with a list of users and connections between said users. The file 
should have the total number of users on its first line, followed by each user on each line. Lastly, some number of lines less than the total number 
of users should have the ID of a user, the ID's of the people that person is coached by, and the ID's of the people that person coaches; each part should 
be seperated by a semicolon. 
For example: 
	1; 2 3; 4 5 6
In this example, user 1 is coached by 2 and 3 and coaches users 4, 5, and 6.

If no file is given in the command line argument, the program prints an error message, as directed by "if not os.path.isfile(filename)". 

Assuming a file is given, however, the file is opened and iterated through via the built-in enumerate function. The first line is then 
stripped and assigned to the variable number_users, which will be used to tell when the program has iterated through the last ID, appended
to the empty list "users". Once it exits this case, it enters the else statement where each part of the line is split and added to a tuple.
In the final part of this establish_user_base function, the states and relationships are established in the tuple. This is done by methods 
of the user class.

In the class User, the __init___ function sets up the lists for storing coaches and coachees, establishes the initial infection status, 
and the (unique) ID of the user.

A separate list must be used for coaches because "infections may be transmitted via 'is coached by' relationships". Explicitly specifying 
this implies that there could be more than one coach per user because if there were only one coach per user, then the 'is coached by' 
relationship is redundant because the only way a user could be infected is by their coach (so one does not need the infection coming back 
up the coaching tree).

With that said, the main of this program is contained in the infections class. It contains three menu options: total_infection, limited_infections,
and a case where the number of infections has a cap. 




