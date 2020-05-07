from app.models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_raphael = User(username = 'raphael',password = 'ranaya', email = 'ralph@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="survey",user = self.user_raphael, upvotes=0,downvotes=0)

    

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Test')
        self.assertEquals(self.new_pitch.pitch_content,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"survey")
        self.assertEquals(self.new_pitch.user,self.user_raphael)

    