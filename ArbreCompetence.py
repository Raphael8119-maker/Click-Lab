import arcade

WINDOW = arcade.Window(title= "Compétence-Click_Lab")
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#allCompetence = {"Competence1":["competence2.1","competence2.2"],"competence2.1":["competence3.1","competence3.2"]}
#competenceDéblocable = []

class GameView(arcade.View):
    def __init__(self): 
        super().__init__()
        
        self.directions = {'left':False,'right':False,'up':False,'down':False,}
        
        self.window.set_mouse_visible(True)
        
        self.background_color = arcade.csscolor.BLACK

        
    def setup(self):
        pass

    def on_draw(self):
         self.clear() 
         
def main():
    """Main function"""
    game = GameView()
    WINDOW.show_view(game)
    arcade.run()
    
if __name__ == "__main__":
    main()