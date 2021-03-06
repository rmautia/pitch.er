from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_raphael = User(username = 'raphael',password = 'ranaya', email = 'pete@smg.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="survey",user = self.user_raphael,upvotes=0,downvotes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_raphael,pitch=self.new_pitch)

  

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_raphael)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)

      # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()
