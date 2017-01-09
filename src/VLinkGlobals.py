from vocollect_core.task.task_runner import TaskRunnerBase
from vocollect_core.dialog.functions import prompt_yes_no, prompt_only
from vocollect_core.utilities.localization import itext
from core.VehicleTask import VehicleTask

def change_vehicle():
    runner = TaskRunnerBase.get_main_runner()
    task = runner.get_current_task()
    
    if task is not None:
        from voice import globalwords
        if prompt_yes_no(itext('global.change.vehicle.confirm')):
            prompt_only(itext('global.change.vehicle'))
            globalwords.words['change vehicle'].enabled = False
            task.launch(VehicleTask(runner), task.current_state)
        