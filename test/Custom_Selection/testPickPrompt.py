from BaseVLTestCase import BaseVLTestCase #@UnusedImport
import main #@UnusedImport

from voicelink_test.unit_tests.testSelection import testPickPrompt
from Custom_Selection.PickPromptMultipleCustom import PVID_VERIFICATION
from selection.PickPrompt import SLOT_VERIFICATION, ENTER_QTY,\
    QUANTITY_VERIFICATION, LOT_TRACKING, INTIALIZE_PUT, PUT_PROMPT,\
    WEIGHT_SERIAL, XMIT_PICKS, NEXT_STEP, CHECK_PARTIAL, CASE_LABEL_CD,\
    CHECK_TARGET_CONTAINER, CLOSE_TARGET_CONT, CYCLE_COUNT

class testMultiplePickPromptTaskCustom (testPickPrompt.testMultiplePickPromptTask):
    
    def test_initializeStates(self):

        #only run in main classes
        if self._obj is not None:     
            #test name
            self.assertEquals(self._obj.name, 'pickPrompt')
    
            #test states
            self.assertEquals(self._obj.states[0], CHECK_TARGET_CONTAINER)
            self.assertEquals(self._obj.states[1], SLOT_VERIFICATION)
            self.assertEquals(self._obj.states[2], PVID_VERIFICATION)
            self.assertEquals(self._obj.states[3], CASE_LABEL_CD)
            self.assertEquals(self._obj.states[4], ENTER_QTY)
            self.assertEquals(self._obj.states[5], QUANTITY_VERIFICATION)
            self.assertEquals(self._obj.states[6], LOT_TRACKING)
            self.assertEquals(self._obj.states[7], INTIALIZE_PUT)
            self.assertEquals(self._obj.states[8], PUT_PROMPT)
            self.assertEquals(self._obj.states[9], WEIGHT_SERIAL)
            self.assertEquals(self._obj.states[10], XMIT_PICKS)
            self.assertEquals(self._obj.states[11], CHECK_PARTIAL)
            self.assertEquals(self._obj.states[12], CLOSE_TARGET_CONT)
            self.assertEquals(self._obj.states[13], NEXT_STEP)
            self.assertEquals(self._obj.states[14], CYCLE_COUNT)
            
            #test dynamic vocab set properly
            self.assertTrue(self._obj.name in self._obj.dynamic_vocab.pick_tasks)
    
    def test_pvid_value_blank(self):
        self._obj._pvid = ''
        self._obj.next_state = None
        self._obj.runState(PVID_VERIFICATION)
        
        self.assertEqual(self._obj.next_state, None)
        self.validate_prompts()
        self.validate_server_requests()
        
    def test_pvid_value_populated(self):
        self._setup_put_data()
        
        self._obj._pvid = '23'
        self._obj.next_state = None
        self.post_dialog_responses('23')
        self._obj.runState(PVID_VERIFICATION)
        
        self.assertEqual(self._obj.next_state, None)
        self.validate_prompts('PVID?')
        self.validate_server_requests()
    
    def test_pvid_skip_slot(self):
        ''' just test for skip slot is not allowed '''
        self._setup_put_data()
        
        self._obj._pvid = '23'
        self._obj.next_state = None
        self.post_dialog_responses('skip slot')
        self._obj.runState(PVID_VERIFICATION)
        
        self.assertEquals(self._obj.next_state, PVID_VERIFICATION)
        self.validate_prompts('PVID?', 'Last slot, skip slot not allowed')
