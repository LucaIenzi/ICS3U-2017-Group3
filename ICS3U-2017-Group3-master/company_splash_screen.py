# 

# Created by: Luca
# Created on: jan 2018
# Created for: ICS3U
# This scene shows the company spash screne.

from scene import *
import ui
import time

from main_menu_scene import *

class CompanyScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     
                                     parent = self, 
                                     size = self.size)
        self.school_crest = SpriteNode('./images/companylogo.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       size = self.size)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 1.3:
            self.present_modal_scene(MainMenu())
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
