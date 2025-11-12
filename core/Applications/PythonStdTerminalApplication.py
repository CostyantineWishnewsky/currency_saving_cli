import sys

from core.Application import Application
from core.EventObserver import EventObserver
from core.ControllersCreator import ControllersCreator

from core.Events.Controller.RunControllerEvent import RunControllerEvent
from core.Events.ControllerCreator.CreateHomeControllerEvent import CreateHomeControllerEvent
from core.Events.Controller.CreateHelpController import CreateHelpControllerEvent


class PythonStdTerminalApplication(Application):
    def __init__(self,command_line_parameters:list[str]):
        self._command_line_parameters=command_line_parameters

        self._routes={}

    def setup(self):
        event_observer=EventObserver()
        

        event_observer.setup()

        id=event_observer.get_last_event_subscriber_id()

        controllers_creater=ControllersCreator(id)
        controllers_creater.setup()

        did_got_name=event_observer.add_subscriber_name('controllers_creator',controllers_creater)
        self._routes={
            "today":{'name':'home','event':CreateHomeControllerEvent(id=id)},
            "help":{'name':'help','event':CreateHelpControllerEvent(id=id,command_name=None)},
        }

    def stop(self):
        pass

    def run(self):
        event_observer=EventObserver()
        controllers_creator_id=event_observer.get_id_by_name('controllers_creator')
        if len(self._command_line_parameters) != 1:
            
            if self._command_line_parameters[1] in self._routes.keys():
                event_observer.notify(self._routes[self._command_line_parameters[1]]['event']) 
                controller_id=event_observer.get_id_by_name(self._routes[self._command_line_parameters[1]]['name'])
                event_observer.notify(RunControllerEvent(id=controller_id,data={}))

                return
        event_observer.notify(CreateHelpControllerEvent(id=controllers_creator_id,command_name=None))
        help_controller_id=event_observer.get_id_by_name("help") 
        event_observer.notify(RunControllerEvent(id=help_controller_id,data={}))
        return
