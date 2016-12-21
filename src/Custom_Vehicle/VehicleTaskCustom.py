from vocollect_core.utilities import class_factory
from core.VehicleTask import VehicleTask, COMPLETE_SAFETYCHECK

from voice import globalwords as gw

class VehicleTask_Custom(VehicleTask):

    def complete_safety_check(self):
        ''' completed all safety checks so inform host '''
        
        #If here, then all checks passed or where fixed
        result = self._veh_safety_lut.do_transmit(-1, '', 0)
        
        if result == 0:
            gw.words['change vehicle'].enabled = True
        else:
            self.next_state = COMPLETE_SAFETYCHECK

class_factory.set_override(VehicleTask, VehicleTask_Custom)