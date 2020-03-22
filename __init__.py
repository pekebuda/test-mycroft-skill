from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder


class TestSkill(MycroftSkill):
    def __init__(self):
        """
        called when the Skill is first constructed. It is often used to declare
        variables or perform setup actions, however it cannot utilize other
        MycroftSkill methods as the class does not yet exist
        """
        super().__init__(self)

    def initialize():
        """
        Perform any final setup needed for the skill here. This function is
        invoked after the skill is fully constructed and registered with the
        system. Intents will be registered and Skill settings will be
        available.
        """
        pass

    def stop():
        """
        What your Skill should do if a stop intent is detected
        """
        pass

    @intent_file_handler('TellMeYourAge.intent')
    def handle_tell_me_your_age_intent(self, message):
        self.speak_dialog('tell.me.your.age')

    @intent_handler(IntentBuilder('PluckANumberIntent').require('PluckANumber.voc'))
    def handle_thank_you_intent(self, message):
        number_domain = message.data.get('domain')
        if number_domain is not None:
            self.speak_dialog('pluck.a.number')
        else:
            self.speak_dialog('pluck.a.number')


def create_skill():
    return TestSkill()
