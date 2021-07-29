
##### ------- take the cyclists and workouts from the final project db and change the cyclists id to the correct id.

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unidecode import unidecode
import pandas as pd
from models.cyclist import CyclistModel
from models.maor_cyclist import MaorCyclist

#Get cyclists from Maor's db - velodromeDB1
# SQLALCHEMY_DATABASE_URI = *DB login details*
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
#make cyclists data frame
df_Maor_cyclists = pd.read_sql(session.query(MaorCyclist).statement, session.bind)
df_Maor_cyclists['full_name'] = df_Maor_cyclists['first_name'] + " " + df_Maor_cyclists['last_name']
df_Maor_cyclists['full_name'] = df_Maor_cyclists['full_name'].apply(lambda x :unidecode(x.lower()))

#Get data base from final project db - velodromeDB
# SQLALCHEMY_DATABASE_URI = *DB login details*
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
#make cyclists data frame
df_final_project_cyclists = pd.read_sql(session.query(CyclistModel).statement, session.bind)
df_final_project_cyclists['full_name'] = (df_final_project_cyclists['first_name'] + " " + df_final_project_cyclists['last_name'])
df_final_project_cyclists['full_name'] = df_final_project_cyclists['full_name'].apply(lambda x :unidecode(x.lower()))
#modify Patrick Bevin's name
bevin_index = df_final_project_cyclists.loc[df_final_project_cyclists['full_name'] == 'paddy bevin'].index
df_final_project_cyclists.loc[bevin_index , ['full_name']]= 'patrick bevin'
print(df_final_project_cyclists)

def get_correct_id_from_name(cyclists_name):
    # input - cyclists full name (from final project)
    # output - the correct cyclists_id (taken from Maor's db)
    if cyclists_name not in ['roches roses']:
        row = df_Maor_cyclists.loc[df_Maor_cyclists['full_name'] == cyclists_name]
        correct_id = row.iloc[-1]['cyclist_id']
        return correct_id
    else:
        return 0


#modify cyclist id to be correct for each cyclist using the function get_correct_id()
df_final_project_cyclists['old_id'] = df_final_project_cyclists['cyclist_id'] #save the old (incorrect) id.
df_final_project_cyclists['cyclist_id'] = df_final_project_cyclists['full_name'].apply(get_correct_id_from_name)
df_final_project_cyclists.to_csv (r'C:\Users\Alon Malach\Desktop\lab\final_project_cyclists.csv', index = None, header=True)

#make workouts data frame
df_workouts = pd.read_sql(session.query(WorkoutModel).statement, session.bind)

def get_correct_id_from_id(incorrect_id):
    # input - cyclists incorrect_id (cyclist_id from final project)
    # output - the correct cyclists_id (taken from Maor's db)
    row = df_final_project_cyclists.loc[df_final_project_cyclists['cyclist_id'] == incorrect_id]
    correct_id = row.iloc[-1]['correct_id']
    return correct_id

df_workouts['cyclist_id'] = df_workouts['cyclist_id'].apply(get_correct_id_from_id) #change the cyclists_id to be correct (as in Maor's table)
df_workouts.to_csv (r'C:\Users\Alon Malach\Desktop\lab\Workouts.csv', index = None, header=True)

df_workouts_cadences = pd.read_sql(session.query(WorkoutCadenceModel).statement, session.bind)
df_workouts_cadences.to_csv (r'C:\Users\Alon Malach\Desktop\lab\Workouts_Cadence.csv', index = None, header=True)

df_workouts_hrs = pd.read_sql(session.query(WorkoutHRModel).statement, session.bind)
df_workouts_hrs.to_csv (r'C:\Users\Alon Malach\Desktop\lab\Workouts_HR.csv', index = None, header=True)

df_workouts_powers = pd.read_sql(session.query(WorkoutPowerModel).statement, session.bind)
df_workouts_hrs.to_csv (r'C:\Users\Alon Malach\Desktop\lab\Workouts_Power.csv', index = None, header=True)

df_workouts_speeds = pd.read_sql(session.query(WorkoutSpeedModel).statement, session.bind)
df_workouts_hrs.to_csv (r'C:\Users\Alon Malach\Desktop\lab\Workout_Speed.csv', index = None, header=True)
