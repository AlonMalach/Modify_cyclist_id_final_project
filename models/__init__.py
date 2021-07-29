from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .coaches import CoachModel
from .cyclist import CyclistModel
from .user import UserModel
from .workout import WorkoutModel
from .workout_cadence import WorkoutCadenceModel
from .workout_hr import WorkoutHRModel
from .workout_power import WorkoutPowerModel
from .workout_speed import WorkoutSpeedModel
from .cyclist_team import CyclistTeamModel
from .fact_workout_metrics import FactWorkoutMetricsModel
from .fact_workout_power import FactWorkoutPowerModel
from .fact_weekly_workout_metrics import FactWeeklyWorkoutMetricsModel
from .team import TeamModel
from .cyclist_stats import CyclistStatsModel
from .cyclist_nr_by_season import CyclistNrBySeasonModel
from .cyclist_stage_result import CyclistStageResultModel
from .stage import StageModel
from .team_in_stage import TeamInStageModel
from .stage_result import StageResultModel
from .team_stage_result import TeamStageResultModel
