################################
# Lesley Cordero
################################

class User:

    def __init__(self, new_ID):
        '''
        This function sets up the lists for storing coaches and coachees, establishes the
        initial infection status, and the (unique) ID of the user.

        A list must be used for coaches because "infections may be transmitted via 'is
        coached by' relationships". Explicitly specifying this implies that there could
        be more than one coach per user because if there were only one coach per user, then
        the 'is coached by' relationship is redundant because the only way a user could be
        infected is by their coach (so one does not need the infection coming back up the
        coaching tree).
        '''
        self.coaches = []
        self.coachees = []
        self.__infected = False
        self.ID = new_ID

    def add_coach(self, new_coach):
        '''
        This function adds a coach to this user's list of coaches.
        '''
        self.coaches.append(new_coach)

    def add_coachee(self, new_coachee):
        '''
        This function adds a coachee to this user's list of coachees.
        '''
        self.coachees.append(new_coachee)

    def infect(self):
        '''
        This function sets the user's infection status to True.
        '''
        self.__infected = True

    def uninfect(self):
        '''
        This function sets the user's infection status to False.
        '''
        self.__infected = False
            
    def is_infected(self):
        '''
        This function returns the user's infection status.
        '''
        return self.__infected

    def is_coached_by(self, coach_ID):
        '''
        This function checks if the user is coached by a user with the specified ID.
        '''
        for coach in self.coaches:
            if coach.ID == coach_ID:
                return True
        return False

    def is_coaching(self, coachee_ID):
        '''
        This function checks if the user is coaching a user with the specified ID.
        '''
        for coachee in self.coachees:
            if coachee.ID == coachee_ID:
                return True
        return False

    def infect_coaches(self):
        '''
        This function infects all of the coaches of this user and returns the list of those who were infected.
        '''
        newly_infected = []
        for coach in self.coaches:
            if not coach.is_infected():
                coach.infect()
                newly_infected.append(coach)
        return newly_infected
        

    def infect_coachees(self):
        '''
        This function infects all the coachees of this user and returns the list of those who were infected.
        '''
        newly_infected = []
        for coachee in self.coachees:
            if not coachee.is_infected():
                coachee.infect()
                newly_infected.append(coachee)
        return newly_infected

