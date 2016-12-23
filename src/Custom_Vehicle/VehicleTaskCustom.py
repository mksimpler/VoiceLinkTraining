from vocollect_core.utilities import class_factory
from core.VehicleTask import VehicleTask, COMPLETE_SAFETYCHECK,\
    REQUEST_XMIT_VEHID, REQUEST_VEHICLEID, NEXT_SAFETY_CHECK

from voice import globalwords as gw
from vocollect_core.dialog.functions import prompt_only
from vocollect_core.utilities.localization import itext

class VehicleTask_Custom(VehicleTask):
    
    def xmit_veh_id(self):
        #send type and id back to host
        result = self._veh_id_lut.do_transmit(self.vehicle_type, self.vehicle_id)
        if result < 0:
            self.next_state = REQUEST_XMIT_VEHID
        elif result > 0:
            self.next_state = REQUEST_VEHICLEID
        else:
            #check if safety check is required
            self.next_state = ''
            gw.words['change vehicle'].enabled = True
            
            if self._veh_id_lut[0]['safetyCheck'] != '':
                self._safety_check_iter = iter(self._veh_id_lut)
                prompt_only(itext("core.startSafetyCheck.prompt"))
                self.next_state = NEXT_SAFETY_CHECK

    def complete_safety_check(self):
        ''' completed all safety checks so inform host '''
        
        #If here, then all checks passed or where fixed
        result = self._veh_safety_lut.do_transmit(-1, '', 0)
        
        if result == 0:
            gw.words['change vehicle'].enabled = True
        else:
            self.next_state = COMPLETE_SAFETYCHECK

class_factory.set_override(VehicleTask, VehicleTask_Custom)
