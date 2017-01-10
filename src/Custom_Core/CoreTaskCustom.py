from vocollect_core.utilities import class_factory
from core.CoreTask import CoreTask, REQUEST_CONFIG
from voice import globalwords as gw
from vocollect_core.utilities.localization import itext
from vocollect_core.dialog.functions import prompt_yes_no, prompt_only

class CoreTask_Custom(CoreTask):
    
#    def __init__(self, taskRunner=None, callingTask=None):
#        CoreTask.__init__(self, taskRunner=taskRunner, callingTask=callingTask)
#        self.name = "coreTaskCustom"
    
    def request_configurations(self):
        self.sign_off_allowed = True
        gw.words['sign off'].enabled = False
        #gw.words['take a break'].enabled = False
        if not self._transmit_configuration():
            self.next_state = REQUEST_CONFIG
            
        gw.words['change vehicle'].enabled = False
    
    def request_breaks(self):
        pass
    
    def request_signon(self):
        self.password = None
        gw.words['sign off'].enabled = True
        
    def sign_off_confirm(self, allowed = False):
        ''' sign off with confirm '''
        if allowed or self.sign_off_allowed:
            if prompt_yes_no(itext('core.signoff.confirm'), False):
                self.sign_off()
        else:
            prompt_only(itext('core.signoff.not.allowed'))
            
#    def change_vehicle(self):
#        if prompt_yes_no(itext('global.change.vehicle.confirm')):
#            prompt_only(itext('global.change.vehicle'))
#            self.return_to(self.name, REQUEST_VEHICLES)
#        else:
#            gw.words['sign off'].enabled = True

class_factory.set_override(CoreTask, CoreTask_Custom)
