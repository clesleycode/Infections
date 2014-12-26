################################
# Lesley Cordero
# Khan Academy Project
################################

from user import User

import os.path
import sys

def total_infection(users, starting_ID):
    '''
    This function starts a total infection at the user with the given ID.
    '''
    initial_patient = None
    for user in users:
        if user.ID == starting_ID:
            initial_patient = user
    if initial_patient == None:
        print('A valid user ID was not given!')
        return
    initial_patient.infect()
    newly_infected_users = [initial_patient]
    while len(newly_infected_users) != 0:
        justadded_infected_users = []
        for newly_infected_user in newly_infected_users:
            infected_coaches = newly_infected_user.infect_coaches()
            justadded_infected_users.extend(infected_coaches)
            infected_coachees = newly_infected_user.infect_coachees()
            justadded_infected_users.extend(infected_coachees)
        newly_infected_users = justadded_infected_users

def limited_infection(users, starting_ID):
    '''
    This function starts a limited infection at the user with the given ID.
    '''
    initial_patient = None
    for user in users:
        if user.ID == starting_ID:
            initial_patient = user
    if initial_patient == None:
        print('A valid user ID was not given!')
        return
    initial_patient.infect()
    newly_infected_users = [initial_patient]
    while len(newly_infected_users) != 0:
        justadded_infected_users = []
        for newly_infected_user in newly_infected_users:
            infected_coachees = newly_infected_user.infect_coachees()
            justadded_infected_users.extend(infected_coachees)
        newly_infected_users = justadded_infected_users
    

def counted_infection(users, count):
    '''
    This function tries to start an infection at the user with the given ID
    and infect the given number of people. If that many people cannot be infected,
    the user base is restored at full health; if that many people can be infected,
    the user base is kept in the limited and counted infection state.
    '''
    for user in users:
        limited_infection(users, user.ID)
        if count_infected(users) != count:
            heal_user_base(users)
        else:
            print('The infection was successful!')
            return
    print('The infection was unsuccessful.')

def heal_user_base(users):
    '''
    This function reheals the whole user base (sets each user to be uninfected).
    '''
    for user in users:
        user.uninfect() 

def establish_user_base(filename):
    '''
    This function returns a fully defined list of users with all connections of coaching
    and being coached by established. The file should have the total number of users (say N)
    on the first line. Then, N lines with one user ID per line should follow. After that,
    some number of lines less than the total number of users should have the ID of a user,
    the ID's of the people that person is coached by, and the ID's of the people that person
    coaches; each part should be seperated by a semicolon. Example follows below:
    1; 2 3; 4 5 6
    In this example, user 1 is coached by 2 and 3 and coaches users 4, 5, and 6.
    '''
    if not os.path.isfile(filename):
        print('\"%s\" cannot be found! Please check the file name!' % filename)
        exit(1)
    users = []
    user_file = open(filename, 'r')
    number_users = -1
    for i, line in enumerate(user_file):
        if i == 0: # 1st line: strips and assigns this number to numbers_users
            number_users = int(line.strip())
        else:
            if i <= number_users: # iterates until final ID is iterated through
                users.append(User(line.strip())) # appends each ID to empty list
            else:
                (userID, coachIDs, coacheeIDs) = tuple([part.strip().split() for part in line.strip().split(';')])
                current_user = None
                for user in users:
                    if user.ID == userID[0]:
                        current_user = user
                        break
                for user in users:
                    if user.ID in coachIDs:
                        current_user.coaches.append(user)
                    if user.ID in coacheeIDs:
                        current_user.coachees.append(user)
    return users

def count_infected(users):
    '''
    This function counts and returns the number of people infected in the user base.
    '''
    return sum([int(user.is_infected()) for user in users])

def infection_information(users):
    '''
    This function prints information on the extent of the infection on the user base.
    '''
    infection_count = count_infected(users)
    result = '%d users were infected, that\'s %f%%!'
    if infection_count == 1:
        result = result.replace('users', 'user').replace('were', 'was')
    print(result % (infection_count, 100.0 * infection_count / len(users)))
    
if __name__ == '__main__':
    '''
    This function runs a total infection on some part of the user base by taking
    the ID of one user to start the infection on. The user base is then rejuvenated
    to full health. After this restoration, a limited infection is run. The user base
    is once again rejuvenated to full health. After this restoration, a counted infection
    is run with the given number of people being infected.

    It is assumed that the user base is completely uninfected before any type of
    infection is run.
    '''
    if len(sys.argv) < 2:
        print('User base file not provided!')
        exit(1)
    user_base = establish_user_base(sys.argv[1])
    total_infection(user_base, raw_input('Please enter the ID where the total infection should start: '))
    infection_information(user_base)
    heal_user_base(user_base)
    limited_infection(user_base, raw_input('Please enter the ID where the limited infection should start: '))
    infection_information(user_base)
    heal_user_base(user_base)
    counted_infection(user_base, int(raw_input('Please enter the number of people that should be infected by the counted infection: ')))
    infection_information(user_base)
    heal_user_base(user_base)

