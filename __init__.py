from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class BestAnimeSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(BestAnimeSkill, self).__init__(name="BestAnimeSkill")
        
        self.count = 0

    @intent_handler(IntentBuilder("").require("Best").require("Anime"))
    def handle_hello_world_intent(self, message):
        self.speak_dialog("best.anime")

def create_skill():
    return BestAnimeSkill()
