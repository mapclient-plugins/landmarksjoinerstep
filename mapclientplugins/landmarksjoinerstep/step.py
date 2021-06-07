'''
MAP Client Plugin Step
'''

from PySide2 import QtGui
from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint


class LandmarksJoinerStep(WorkflowStepMountPoint):
    '''
    Step for collating a fieldwork model into a new or existing 
    dictionary (fieldworkmodeldict).
    '''

    def __init__(self, location):
        super(LandmarksJoinerStep, self).__init__('Landmarks Joiner', location)
        self._configured = True  # A step cannot be executed until it has been configured.
        self._category = 'Anthropometry'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/landmarksjoinerstep/images/landmarksjoinericon.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#landmarks'))

        self._landmarks1 = None
        self._landmarks2 = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._landmarks1.update(self._landmarks2)
        self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self._landmarks1 = dataIn  # ju#landmarks
        else:
            self._landmarks2 = dataIn  # ju#landmarks

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._landmarks1  # ju#landmarks

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        pass

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return 'LandmarkJoiner'  # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass  # TODO: Must actually set the step's identifier here

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return ''

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        pass
