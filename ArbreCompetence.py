import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Compétence-Click_Lab"
allCompetence = {"Competence1":["competence2.1","competence2.2"],"competence2.1":["competence3.1","competence3.2"]}
competenceDéblocable = []

class Main(arcade):
    def __init__(self): 
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)