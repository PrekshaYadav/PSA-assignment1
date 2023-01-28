import collections
import random
#The women that the men prefer
preferred_rankings_men = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The men that the women prefer
preferred_rankings_women = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake']
}

#Keep track of the people that "may" end up together
tentative_engagements 	= []

#Men who still need to propose and get accepted successfully
free_men 				= []


def init_free_men():
    '''Initialize the arrays of women and men to represent
        that they're all initially free and not engaged'''
    for man in preferred_rankings_men:
        free_men.append(man)


def begin_matching(man):
    '''Find the first free woman available to a man at
        any given time'''

    print("DEALING WITH %s" % (man))
    for woman in preferred_rankings_men[man]:

        # Boolean for whether woman is taken or not
        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if (len(taken_match) == 0):
            # tentatively engage the man and woman
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('%s is no longer a free man and is now tentatively engaged to %s' % (man, woman))
            break

        elif (len(taken_match) > 0):
            print('%s is taken already..' % (woman))

            # Check ranking of the current dude and the ranking of the 'to-be' dude
            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if (current_guy < potential_guy):
                print('She\'s satisfied with %s..' % (taken_match[0][0]))
            else:
                print('%s is better than %s' % (man, taken_match[0][0]))
                print('Making %s free again.. and tentatively engaging %s and %s' % (taken_match[0][0], man, woman))

                # The new guy is engaged
                free_men.remove(man)

                # The old guy is now single
                free_men.append(taken_match[0][0])

                # Update the fiance of the woman (tentatively)
                taken_match[0][0] = man
                break


def stable_matching():
    '''Matching algorithm until stable match terminates'''
    while (len(free_men) > 0):
        for man in free_men:
            begin_matching(man)



def stable( tentative_engagements):

    for match in tentative_engagements:

        if (preferred_rankings_women[match[1]][0] != match[0]):
            return 0

        if (preferred_rankings_men[match[0]][0] != match[1]):
            return 0

        return 1







def main():
    init_free_men()
    print(free_men)
    stable_matching()
    print(tentative_engagements)
    print(type(preferred_rankings_men))

    # Question 10.B: Shuffle 1000 times.
    sum = 0
    for i in range(0,1000):
        for key in preferred_rankings_men:
            random.shuffle(preferred_rankings_men[key])

        for key in preferred_rankings_women:
            random.shuffle(preferred_rankings_women[key])

        stable_matching()

        a = stable(tentative_engagements)
        sum = sum +a

    sum = (sum/1000)*100
    print("Percentage of stable playoff matches after 1000 random shuffling is ",sum, "%")
    print(preferred_rankings_men)
    print(preferred_rankings_women)

    stable(tentative_engagements)

main()