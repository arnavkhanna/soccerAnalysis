#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
import json
import numpy as np
#url = "https://github.com/statsbomb/open-data/blob/master/data/events/16010.json"
#df = pd.read_json(url)


# In[20]:


def clean_duel(duel):
    
    if(not pd.isnull(duel) and (not type(duel) == str)):
        
        if "counterpress" in duel.keys():
            
            counterpress = True 
        else: 
            counterpress = False 
        if duel['outcome']['id'] == 1 :
            
            outcome = 'Lost'
        elif duel['outcome']['id'] == 4 :
            
            outcome = "Won"
        elif duel['outcome']['id'] == 13 :
            outcome = 'Lost in play'
        elif duel['outcome']['id'] == 14 :
            
            outcome = "Lost Out" 
        elif duel['outcome']['id'] == 15 :
            
            outcome = "Success"
        elif duel['outcome']['id'] == 16 :
            
            outcome = 'Success in Play'
        else : 
            outcome = "Success Out"
            
        if duel['type']['id'] == 10 :
            
            ttype = "Aerial Lost"
        else :
            ttype = "Tackle"
        duel = [counterpress,type,outcome]
        
    return duel 


# 

# 

# In[21]:


def clean_interception(interception):
    if(not pd.isnull(interception) and (not type(interception) == str)):
        if interception['outcome']['id'] == 1 :
            
              outcome = 'Lost'
        elif interception['outcome']['id'] == 4 :
            
            outcome = "Won"
        elif interception['outcome']['id'] == 13 :
            outcome = 'Lost in play'
        elif interception['outcome']['id'] == 14 :
            
            outcome = "Lost Out" 
        elif interception['outcome']['id'] == 15 :
            
            outcome = "Success"
        elif interception['outcome']['id'] == 16 :
            
            outcome = 'Success in Play'
        else : 
            outcome = "Success Out"
        interception = [outcome]
    return interception 


# In[24]:


def clean_foul(foul_comm):
        if(not pd.isnull(foul_comm) and (not type(foul_comm) == str)):
            if 'counterpress' in foul_comm.keys():
                counterpress = True; 
            if "offensive" in foul_comm.keys():
                offensive = True; 
            if "advantage" in foul_comm.keys():
                advantage = True; 
            if "penalty" in foul_comm.keys():
                pentalty = True; 
            if foul_comm['type']['id'] == 19 :
                ttype = "6 Seconds"
            elif foul_comm['type']['id'] == 20:
                ttype = "Backpass Pick"
            elif foul_comm['type']['id'] == 21:
                ttype = 'Dangerous Play' 
            elif foul_comm['type']['id'] == 22:
                ttype = 'Dive'
            elif foul-comm['type']['id'] == 23:
                ttype =  'Foul Out'  
            else :
                ttype = "HandBall"
            if foul_comm['card']['id'] == 5:
                card = "Yellow Card"
            elif foul-comm['card']['id'] == 6:
                card = "Second Yellow"
            else:
                card = "Red Card"
        clean_foul = [counterpress,offensive,ttype,advantage,pentalty,card]
        return clean_foul


# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




