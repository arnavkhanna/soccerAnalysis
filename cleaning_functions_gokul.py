# Define cleaning functions to process the data
import pandas as pd
import numpy as np

# simple clean on ['block', 'ball_recovery', 'foul_won']
def simple_clean(info):

    # Checks if data isn't null (dict) and not alr cleaned
    if (not pd.isnull(info)) and (not type(info) == str):

        # Get new value from key
        info = list(info.keys())[0]

    # Return new value
    return info

# complex clean on ['dribble']
def clean_dribble(dribble):

    # Checks if data isn't null (dict) and not alr cleaned
    if (not pd.isnull(dribble)) and (not type(dribble) == str):

        # Get overrun info
        if "overrun" in dribble.keys():

            overrun = True

        else:

            overrun = False

        # Get no touch info
        if "No Touch" in dribble.keys():

            no_touch = True

        else:

            no_touch = False

        # Get success/fail (8/9) info
        if dribble['outcome']['id'] == 8:

            outcome = "success"

        else:

            outcome = "fail"

        # Return as list
        dribble = [overrun, no_touch, outcome]

    return dribble

def clean_goalkeeper(goalkeeper):

    #gk_info = [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN]

    if (type(goalkeeper) == dict) and (not pd.isnull(goalkeeper)):

        if 'outcome' in goalkeeper.keys():

            outcome = goalkeeper['outcome']['name']

        else:

            outcome = 'null'

        if 'type' in goalkeeper.keys():

            gk_type = goalkeeper['type']['name']

        else:

            gk_type = 'null'

        if 'position' in goalkeeper.keys():

            position = goalkeeper['position']['name']

        else:

            position = 'null'

        if 'technique' in goalkeeper.keys():

            technique = goalkeeper['technique']['name']

        else:

            technique = 'null'

        if 'body_part' in goalkeeper.keys():

            body_part = goalkeeper['body_part']['name']

        else:

            body_part = 'null'

        goalkeeper = [outcome, gk_type, position, technique, body_part]

    return goalkeeper

# Functions to get specific aspects of the list from varied cleaning functions
def get_info_idx(lst, idx):
    if type(lst) == list:
        return lst[idx]
