from turtle import Turtle, Screen
import random
import time

class TurtleRace:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 500)
        self.screen.title("🐢 Turtle Race Championship 🏆")
        self.screen.bgcolor("light cyan")
        
        self.race = False
        self.y_coordinates = [-120, -80, -40, 0, 40, 80, 120]
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']
        self.all_turtles = []
        self.user_turtle = None
        self.wins = 0
        self.losses = 0
        
        self.setup_race_track()
        self.create_score_board()
        
    def setup_race_track(self):
        """Draw start and finish lines"""
        # Start line
        start_line = Turtle()
        start_line.hideturtle()
        start_line.penup()
        start_line.goto(-240, 180)
        start_line.pendown()
        start_line.pensize(3)
        start_line.color("green")
        start_line.right(90)
        start_line.forward(360)
        
        # Start label
        start_line.penup()
        start_line.goto(-260, 190)
        start_line.write("START", font=("Arial", 12, "bold"))
        
        # Finish line (checkered pattern)
        finish_line = Turtle()
        finish_line.hideturtle()
        finish_line.speed(0)
        finish_line.penup()
        
        # Draw checkered finish line
        for y in range(-180, 181, 20):
            finish_line.goto(230, y)
            if y % 40 == 0:
                finish_line.color("black")
            else:
                finish_line.color("white")
            finish_line.pendown()
            finish_line.begin_fill()
            for _ in range(2):
                finish_line.forward(10)
                finish_line.left(90)
                finish_line.forward(20)
                finish_line.left(90)
            finish_line.end_fill()
            finish_line.penup()
        
        # Finish label
        finish_line.color("red")
        finish_line.goto(210, 190)
        finish_line.write("FINISH", font=("Arial", 12, "bold"))
        
    def create_score_board(self):
        """Create score display"""
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("black")
        self.update_score_display()
        
    def update_score_display(self):
        """Update the score on screen"""
        self.score_display.clear()
        self.score_display.goto(-280, 210)
        self.score_display.write(f"Wins: {self.wins} | Losses: {self.losses}", 
                                font=("Arial", 14, "bold"))
        
    def display_bet(self, color):
        """Display user's bet on screen"""
        bet_display = Turtle()
        bet_display.hideturtle()
        bet_display.penup()
        bet_display.goto(0, 210)
        bet_display.color(color)
        bet_display.write(f"Your Bet: {color.upper()}", 
                         align="center", font=("Arial", 14, "bold"))
        
    def create_turtles(self):
        """Create racing turtles"""
        self.all_turtles = []  # Reset the list
        for index in range(7):
            tt = Turtle()
            tt.shape('turtle')
            tt.penup()
            tt.color(self.colors[index])
            tt.goto(-230, self.y_coordinates[index])
            tt.speed(0)
            self.all_turtles.append(tt)  # ✅ FIXED: Changed from all_turtles to self.all_turtles
        
    def get_user_bet(self):
        """Get user's turtle color choice"""
        colors_str = ", ".join(self.colors)
        user_input = self.screen.textinput(
            '🎯 Make Your Bet', 
            f'Which turtle will win?\nChoose from: {colors_str}'
        )
        
        if user_input:
            user_input = user_input.lower()
            if user_input in self.colors:
                return user_input
            else:
                # Invalid color, ask again
                self.screen.textinput(
                    '❌ Invalid Color', 
                    'Please enter a valid color and click OK to try again'
                )
                return self.get_user_bet()
        return None
        
    def show_countdown(self):
        """Show countdown before race starts"""
        countdown = Turtle()
        countdown.hideturtle()
        countdown.penup()
        countdown.goto(0, 0)
        
        for i in range(3, 0, -1):
            countdown.clear()
            countdown.write(i, align="center", font=("Arial", 48, "bold"))
            time.sleep(0.8)
        
        countdown.clear()
        countdown.color("green")
        countdown.write("GO!", align="center", font=("Arial", 48, "bold"))
        time.sleep(0.5)
        countdown.clear()
        
    def show_popup(self, won, winner_color):
        """Show winning/losing pop-up with animation"""
        # Create semi-transparent background
        popup_bg = Turtle()
        popup_bg.hideturtle()
        popup_bg.penup()
        popup_bg.goto(-150, 100)
        popup_bg.color("white")
        popup_bg.pendown()
        popup_bg.begin_fill()
        for _ in range(4):
            popup_bg.forward(300)
            popup_bg.left(90)
        popup_bg.end_fill()
        
        # Border
        popup_bg.pensize(5)
        popup_bg.color("gold" if won else "gray")
        for _ in range(4):
            popup_bg.forward(300)
            popup_bg.left(90)
        popup_bg.penup()
        
        # Result text
        result = Turtle()
        result.hideturtle()
        result.penup()
        
        if won:
            result.goto(0, 50)
            result.color("green")
            result.write("🎉 YOU WON! 🎉", align="center", 
                        font=("Arial", 24, "bold"))
            result.goto(0, 10)
            result.color("black")
            result.write(f"The {winner_color.upper()} turtle won!", 
                        align="center", font=("Arial", 16, "normal"))
        else:
            result.goto(0, 50)
            result.color("red")
            result.write("😢 YOU LOST! 😢", align="center", 
                        font=("Arial", 24, "bold"))
            result.goto(0, 10)
            result.color("black")
            result.write(f"The {winner_color.upper()} turtle won!", 
                        align="center", font=("Arial", 16, "normal"))
        
        # Trophy or sad emoji
        emoji = Turtle()
        emoji.hideturtle()
        emoji.penup()
        emoji.goto(0, -50)
        emoji.write("🏆" if won else "💔", align="center", 
                   font=("Arial", 36, "normal"))
        
    def run_race(self):
        """Main race loop"""
        self.race = True
        winner_color = None
        
        while self.race:
            for turtle in self.all_turtles:
                random_speed = random.randint(0, 10)
                turtle.forward(random_speed)
                
                if turtle.xcor() >= 230:
                    self.race = False
                    winner_color = turtle.pencolor()
                    break
        
        # Determine if user won
        won = (winner_color == self.user_turtle)
        if won:
            self.wins += 1
        else:
            self.losses += 1
            
        self.update_score_display()
        time.sleep(0.5)
        self.show_popup(won, winner_color)
        
        return won
        
    def ask_replay(self):
        """Ask if user wants to play again"""
        time.sleep(1)
        replay = self.screen.textinput(
            "🔄 Play Again?", 
            "Do you want to race again? (yes/no)"
        )
        return replay and replay.lower() in ['yes', 'y']
        
    def reset_race(self):
        """Reset turtles for new race"""
        self.screen.clear()
        self.screen.bgcolor("light cyan")
        self.setup_race_track()
        self.create_score_board()
        
    def start(self):
        """Start the game"""
        play_again = True
        
        while play_again:
            # Get user bet
            self.user_turtle = self.get_user_bet()
            
            if not self.user_turtle:
                break
                
            # Display bet
            self.display_bet(self.user_turtle)
            
            # Create turtles
            self.create_turtles()
            
            # Countdown
            self.show_countdown()
            
            # Run race
            self.run_race()
            
            # Ask for replay
            play_again = self.ask_replay()
            
            if play_again:
                self.reset_race()
        
        # Show final score
        final_score = Turtle()
        final_score.hideturtle()
        final_score.penup()
        final_score.goto(0, -100)
        final_score.write(
            f"Final Score - Wins: {self.wins} | Losses: {self.losses}\nThanks for playing!", 
            align="center", font=("Arial", 16, "bold")
        )
        
        time.sleep(3)
        self.screen.bye()


# Run the game
if __name__ == "__main__":
    game = TurtleRace()
    game.start()