from selection.PickPromptMultiple import PickPromptMultipleTask, SLOT_VERIFICATION
from vocollect_core.utilities import class_factory
from vocollect_core.dialog.functions import prompt_digits_required, prompt_only
from vocollect_core.utilities.localization import itext

PVID_VERIFICATION = 'pvidVerification'


class PickPromptMultipleTask_Custom(PickPromptMultipleTask):
    
    def initializeStates(self):
        super(PickPromptMultipleTask_Custom, self).initializeStates()
        self.addState(PVID_VERIFICATION, self.pvid_verifiaction, SLOT_VERIFICATION)
    
    def slot_verification(self):
        '''Multiple Prompts''' 
        result = prompt_digits_required(self._picks[0]["slot"],
                                                    itext("selection.pick.prompt.checkdigit.help"), 
                                                    [self._picks[0]["checkDigits"]], 
                                                    None, 
                                                    {'ready' : False, 'skip slot' : False})
        if result == 'skip slot':
            self.next_state = SLOT_VERIFICATION
            self._skip_slot()
        else:
            self._verify_product_slot(result, False)
            
    def pvid_verifiaction(self):
        '''
        New custom state for entering PVID
        '''
        if self._pvid != '':
            result = prompt_digits_required(itext('selection.pick.prompt.pvid'),
                                            itext('selection.pick.prompt.pvid.help'),
                                            [self._pvid],
                                            [self._picks[0]['scannedProdID']],
                                            {'skip slot': False})
            if result[0] == 'skip slot':
                self.next_state = PVID_VERIFICATION
                self._skip_slot()
    
    def _verify_product_slot(self, result, is_scanned):
        if result == 'ready' and self._picks[0]["checkDigits"] != '':
            prompt_only(itext('selection.pick.prompt.speak.check.digit'), True)
            self.next_state = SLOT_VERIFICATION

class_factory.set_override(PickPromptMultipleTask, PickPromptMultipleTask_Custom)
