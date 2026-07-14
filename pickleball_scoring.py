from manim import *

class PickleballScoring(Scene):
    def construct(self):
        # ---------------------------------------------------------------------
        # Scene 1: Title Screen
        # ---------------------------------------------------------------------
        title_text = Text(
            "How to Keep Score in Pickleball",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).shift(UP * 1.5)
        
        subtitle_text = Text(
            "(Doubles Rules)",
            font_size=32,
            color=YELLOW_D
        ).next_to(title_text, DOWN, buff=0.5)
        
        intro_desc = Text(
            "Learn the logic behind the three numbers called before every serve.",
            font_size=20,
            color=GRAY_A
        ).next_to(subtitle_text, DOWN, buff=0.8)
        
        self.play(FadeIn(title_text, shift=UP), Write(subtitle_text))
        self.play(FadeIn(intro_desc))
        self.wait(2.5)
        self.play(FadeOut(title_text, subtitle_text, intro_desc))
        
        # ---------------------------------------------------------------------
        # Scene 2: The Three Numbers Explanation
        # ---------------------------------------------------------------------
        scene2_title = Text("The Three Numbers Rule", font_size=32, color=WHITE).to_edge(UP, buff=0.5)
        self.play(Write(scene2_title))
        
        # Let's show "0 - 0 - 2" in giant font with wider spacing to prevent label overlapping
        num_serving = Text("0", font_size=80, color=RED_A)
        dash1 = Text("-", font_size=80, color=WHITE)
        num_receiving = Text("0", font_size=80, color=BLUE_A)
        dash2 = Text("-", font_size=80, color=WHITE)
        num_server = Text("2", font_size=80, color=YELLOW_D)
        
        score_group = VGroup(num_serving, dash1, num_receiving, dash2, num_server).arrange(RIGHT, buff=1.1).shift(UP * 0.5)
        self.play(FadeIn(score_group, shift=UP))
        self.wait(1)
        
        # Labels for each number
        label_serving = Text("Serving Team's\nScore", font_size=15, color=RED_A, line_spacing=1.2).next_to(num_serving, DOWN, buff=1.0)
        arrow_serving = Arrow(start=label_serving.get_top(), end=num_serving.get_bottom(), color=RED_A, stroke_width=2)
        
        label_receiving = Text("Receiving Team's\nScore", font_size=15, color=BLUE_A, line_spacing=1.2).next_to(num_receiving, DOWN, buff=1.0)
        arrow_receiving = Arrow(start=label_receiving.get_top(), end=num_receiving.get_bottom(), color=BLUE_A, stroke_width=2)
        
        label_server = Text("Server Number\n(1 or 2)", font_size=15, color=YELLOW_D, line_spacing=1.2).next_to(num_server, DOWN, buff=1.0)
        arrow_server = Arrow(start=label_server.get_top(), end=num_server.get_bottom(), color=YELLOW_D, stroke_width=2)
        
        self.play(Write(label_serving), GrowArrow(arrow_serving))
        self.wait(1.5)
        self.play(Write(label_receiving), GrowArrow(arrow_receiving))
        self.wait(1.5)
        self.play(Write(label_server), GrowArrow(arrow_server))
        self.wait(2.5)
        
        # Explanation of the Starting Exception (0-0-2)
        exp_box = RoundedRectangle(width=10.0, height=1.5, corner_radius=0.1, fill_color=DARK_GRAY, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1).shift(DOWN * 2.5)
        exp_text = Text(
            "Starting Exception: The first serving team only gets ONE server.\nTo denote this, they start the game as Server 2 (0 - 0 - 2).",
            font_size=18,
            color=WHITE,
            line_spacing=1.3
        ).move_to(exp_box.get_center())
        
        self.play(FadeIn(exp_box), Write(exp_text))
        self.wait(4.5)
        
        # Clear explanations
        self.play(
            FadeOut(score_group, label_serving, arrow_serving, label_receiving, arrow_receiving, label_server, arrow_server, exp_box, exp_text, scene2_title)
        )
        
        # ---------------------------------------------------------------------
        # Scene 3: The Court and Players Layout
        # ---------------------------------------------------------------------
        # Let's draw the court centered at Y = -0.5
        court_center = np.array([0, -0.6, 0])
        
        # Court background colors
        service_bg_left = Rectangle(width=3.3, height=3.0, fill_color="#2e8b57", fill_opacity=0.7, stroke_width=0).shift(court_center + LEFT * 1.65)
        service_bg_right = Rectangle(width=3.3, height=3.0, fill_color="#2e8b57", fill_opacity=0.7, stroke_width=0).shift(court_center + RIGHT * 1.65)
        
        nvz_bg_left = Rectangle(width=1.05, height=3.0, fill_color="#1e4d2b", fill_opacity=0.7, stroke_width=0).shift(court_center + LEFT * 0.525)
        nvz_bg_right = Rectangle(width=1.05, height=3.0, fill_color="#1e4d2b", fill_opacity=0.7, stroke_width=0).shift(court_center + RIGHT * 0.525)
        
        court_bg = VGroup(service_bg_left, service_bg_right, nvz_bg_left, nvz_bg_right)
        
        # Court lines
        outer_box = Rectangle(width=6.6, height=3.0, stroke_color=WHITE, stroke_width=3).shift(court_center)
        net_line = Line(start=court_center + UP * 1.6, end=court_center + DOWN * 1.6, color=LIGHT_GRAY, stroke_width=5)
        
        nvz_line_left = Line(start=court_center + np.array([-1.05, 1.5, 0]), end=court_center + np.array([-1.05, -1.5, 0]), color=WHITE, stroke_width=3)
        nvz_line_right = Line(start=court_center + np.array([1.05, 1.5, 0]), end=court_center + np.array([1.05, -1.5, 0]), color=WHITE, stroke_width=3)
        
        center_line_left = Line(start=court_center + np.array([-3.3, 0, 0]), end=court_center + np.array([-1.05, 0, 0]), color=WHITE, stroke_width=3)
        center_line_right = Line(start=court_center + np.array([3.3, 0, 0]), end=court_center + np.array([1.05, 0, 0]), color=WHITE, stroke_width=3)
        
        court_lines = VGroup(outer_box, net_line, nvz_line_left, nvz_line_right, center_line_left, center_line_right)
        court = VGroup(court_bg, court_lines)
        
        # Beautiful labels for zones
        kitchen_label_left = Text("NVZ (Kitchen)", font_size=12, color=WHITE).rotate(PI/2).move_to(court_center + LEFT * 0.525)
        kitchen_label_right = Text("NVZ (Kitchen)", font_size=12, color=WHITE).rotate(-PI/2).move_to(court_center + RIGHT * 0.525)
        
        # Create broadcast-style Scoreboard HUD at top (Y = 2.6)
        hud_bg = RoundedRectangle(width=8.5, height=1.0, corner_radius=0.1, fill_color="#1E1E1E", fill_opacity=0.9, stroke_color=GRAY_D, stroke_width=2).shift(UP * 2.7)
        
        def make_hud_score(serving_score, receiving_score, server_num, serv_color=RED_A, recv_color=BLUE_A):
            hud_serving_label = Text("SERVING", font_size=12, color=GRAY_A)
            hud_serving_score = Text(str(serving_score), font_size=28, color=serv_color, weight=BOLD)
            hud_serving_group = VGroup(hud_serving_label, hud_serving_score).arrange(DOWN, buff=0.1).shift(LEFT * 2.8 + UP * 2.7)
            
            hud_receiving_label = Text("RECEIVING", font_size=12, color=GRAY_A)
            hud_receiving_score = Text(str(receiving_score), font_size=28, color=recv_color, weight=BOLD)
            hud_receiving_group = VGroup(hud_receiving_label, hud_receiving_score).arrange(DOWN, buff=0.1).shift(UP * 2.7)
            
            hud_server_label = Text("SERVER", font_size=12, color=GRAY_A)
            hud_server_num = Text(str(server_num), font_size=28, color=YELLOW_D, weight=BOLD)
            hud_server_group = VGroup(hud_server_label, hud_server_num).arrange(DOWN, buff=0.1).shift(RIGHT * 2.8 + UP * 2.7)
            
            dash_l = Text("-", font_size=24, color=WHITE).move_to(LEFT * 1.4 + UP * 2.7)
            dash_r = Text("-", font_size=24, color=WHITE).move_to(RIGHT * 1.4 + UP * 2.7)
            
            return VGroup(hud_serving_group, dash_l, hud_receiving_group, dash_r, hud_server_group)
        
        hud_scores = make_hud_score(0, 0, 2)
        
        self.play(FadeIn(court), Write(kitchen_label_left), Write(kitchen_label_right))
        self.play(FadeIn(hud_bg), FadeIn(hud_scores))
        self.wait(1.5)
        
        # Let's create the players
        # Team A (Red) on Left: Player A1 starts as Server 2 (bottom-left), Player A2 is Teammate (top-left)
        # Coordinates: Even court (bottom) center: y = -1.35. Odd court (top) center: y = 0.15.
        pos_A1 = court_center + np.array([-2.2, -0.75, 0])
        pos_A2 = court_center + np.array([-2.2, 0.75, 0])
        
        # Team B (Blue) on Right: Player B1 is Receiver (top-right), Player B2 is Teammate (bottom-right)
        # For Team B, facing net (looking left), Right-Even court is top (y = 0.75), Left-Odd court is bottom (y = -0.75)
        pos_B1 = court_center + np.array([2.2, 0.75, 0])
        pos_B2 = court_center + np.array([2.2, -0.75, 0])
        
        player_A1 = VGroup(
            Circle(radius=0.28, fill_color=RED_C, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2),
            Text("A1", font_size=16, color=WHITE, weight=BOLD)
        ).move_to(pos_A1)
        
        player_A2 = VGroup(
            Circle(radius=0.28, fill_color=RED_E, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2),
            Text("A2", font_size=16, color=WHITE, weight=BOLD)
        ).move_to(pos_A2)
        
        player_B1 = VGroup(
            Circle(radius=0.28, fill_color=BLUE_C, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2),
            Text("B1", font_size=16, color=WHITE, weight=BOLD)
        ).move_to(pos_B1)
        
        player_B2 = VGroup(
            Circle(radius=0.28, fill_color=BLUE_E, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2),
            Text("B2", font_size=16, color=WHITE, weight=BOLD)
        ).move_to(pos_B2)
        
        self.play(
            FadeIn(player_A1, shift=RIGHT),
            FadeIn(player_A2, shift=RIGHT),
            FadeIn(player_B1, shift=LEFT),
            FadeIn(player_B2, shift=LEFT)
        )
        self.wait(1.5)
        
        # ---------------------------------------------------------------------
        # Scene 4: Starting Serve 0-0-2 representation
        # ---------------------------------------------------------------------
        # Highlight active server with glowing ring
        server_ring = Circle(radius=0.38, stroke_color=YELLOW_D, stroke_width=3).move_to(player_A1.get_center())
        ball = Circle(radius=0.08, fill_color=YELLOW, fill_opacity=1.0, stroke_color=BLACK, stroke_width=1).move_to(player_A1.get_center() + RIGHT * 0.35 + UP * 0.1)
        
        # Explanation bubble or text below
        action_text = Text(
            "Game Starts: A1 serves from the Right service court (0 - 0 - 2)",
            font_size=18,
            color=WHITE
        ).shift(DOWN * 3.1)
        
        self.play(Create(server_ring), FadeIn(ball), Write(action_text))
        self.wait(2.5)
        
        # Animate serve diagonally to B1 (top-right)
        serve_path = ArcBetweenPoints(start=ball.get_center(), end=player_B1.get_center() + LEFT * 0.35, angle=-PI/4)
        self.play(MoveAlongPath(ball, serve_path), run_time=1.5)
        self.wait(0.5)
        
        # Return ball and then fault on B's side
        return_path = ArcBetweenPoints(start=ball.get_center(), end=player_A1.get_center() + RIGHT * 0.35, angle=-PI/4)
        self.play(MoveAlongPath(ball, return_path), run_time=1.2)
        
        out_path = ArcBetweenPoints(start=ball.get_center(), end=court_center + np.array([3.8, 1.2, 0]), angle=PI/4)
        self.play(MoveAlongPath(ball, out_path), run_time=1.0)
        
        fault_indicator = Text("FAULT! (Out of Bounds)", font_size=20, color=RED_A, weight=BOLD).move_to(court_center + np.array([3.8, 1.7, 0]))
        self.play(Write(fault_indicator))
        self.wait(1.5)
        self.play(FadeOut(fault_indicator))
        
        # ---------------------------------------------------------------------
        # Scene 5: Team A Wins Point, Shifts Sides, Score becomes 1-0-2
        # ---------------------------------------------------------------------
        point_text = Text("Serving Team Wins the Point!", font_size=22, color=GREEN_C, weight=BOLD).shift(DOWN * 3.1)
        self.play(Transform(action_text, point_text))
        self.wait(2.0)
        
        rule_text = Text(
            "Rule: When the serving team wins a point, they score and switch sides.",
            font_size=18,
            color=YELLOW_C
        ).shift(DOWN * 3.1)
        self.play(Transform(action_text, rule_text))
        self.wait(2.5)
        
        # Move ball back to server
        self.play(ball.animate.move_to(player_A1.get_center() + RIGHT * 0.35 + UP * 0.1))
        
        # Swapping positions for A1 and A2
        # We need the ring to follow A1 as well
        self.play(
            player_A1.animate.move_to(pos_A2),
            player_A2.animate.move_to(pos_A1),
            server_ring.animate.move_to(pos_A2),
            ball.animate.move_to(pos_A2 + RIGHT * 0.35 + DOWN * 0.1),
            run_time=2.0
        )
        self.wait(1.5)
        
        # Update Score HUD to 1-0-2
        hud_scores_new = make_hud_score(1, 0, 2)
        self.play(ReplacementTransform(hud_scores, hud_scores_new))
        hud_scores = hud_scores_new
        
        # Server calls the new score: 1-0-2
        score_call = Text("Score is now: 1 - 0 - 2", font_size=20, color=WHITE).shift(DOWN * 3.1)
        self.play(Transform(action_text, score_call))
        self.wait(3.0)
        
        # ---------------------------------------------------------------------
        # Scene 6: Serve and Loss of Rally (Side-Out)
        # ---------------------------------------------------------------------
        serving_left_text = Text(
            "A1 (Server 2) now serves diagonally from the left court.",
            font_size=18,
            color=WHITE
        ).shift(DOWN * 3.1)
        self.play(Transform(action_text, serving_left_text))
        self.wait(2.5)
        
        # Serve diagonally from top-left (A1) to bottom-right (B2)
        serve_path_2 = ArcBetweenPoints(start=ball.get_center(), end=player_B2.get_center() + LEFT * 0.35, angle=PI/4)
        self.play(MoveAlongPath(ball, serve_path_2), run_time=1.5)
        self.wait(0.5)
        
        # Fault on Serving Team (A) side
        fault_path_2 = ArcBetweenPoints(start=ball.get_center(), end=court_center + np.array([-3.8, -1.2, 0]), angle=PI/4)
        self.play(MoveAlongPath(ball, fault_path_2), run_time=1.2)
        
        fault_indicator_2 = Text("FAULT! (Net or Out)", font_size=20, color=RED_A, weight=BOLD).move_to(court_center + np.array([-3.8, -1.7, 0]))
        self.play(Write(fault_indicator_2))
        self.wait(1.5)
        self.play(FadeOut(fault_indicator_2))
        
        # Side-out explanation
        sideout_text = Text(
            "Serving team loses rally. Since they were on Server 2: SIDE-OUT!",
            font_size=20, color=ORANGE, weight=BOLD
        ).shift(DOWN * 3.1)
        self.play(Transform(action_text, sideout_text))
        self.wait(3.0)
        
        sideout_rule = Text(
            "Serve moves to Team B. The player in the Right court always serves first.",
            font_size=18, color=YELLOW_C
        ).shift(DOWN * 3.1)
        self.play(Transform(action_text, sideout_rule))
        self.wait(3.5)
        
        # Team B's Right court is top-right (occupied by B1)
        # So B1 becomes Server 1!
        # Highlight B1 and move the ball
        self.play(
            FadeOut(server_ring),
            ball.animate.move_to(player_B1.get_center() + LEFT * 0.35 + DOWN * 0.1),
            run_time=1.5
        )
        server_ring_B = Circle(radius=0.38, stroke_color=YELLOW_D, stroke_width=3).move_to(player_B1.get_center())
        self.play(Create(server_ring_B))
        self.wait(1.5)
        
        # New score call. Remember: Serving team is now Team B (Blue), who has 0. Receiving team is A (Red), who has 1.
        # It's Server 1. So score is called: 0 - 1 - 1
        # In HUD, we'll swap the serving/receiving colors to match the active serving team (Blue) and receiving team (Red).
        hud_scores_sideout = make_hud_score(0, 1, 1, serv_color=BLUE_A, recv_color=RED_A)
        self.play(ReplacementTransform(hud_scores, hud_scores_sideout))
        hud_scores = hud_scores_sideout
        
        score_call_sideout = Text(
            "Team B's score is 0, Team A is 1. The score is called: 0 - 1 - 1",
            font_size=20, color=WHITE
        ).shift(DOWN * 3.1)
        self.play(Transform(action_text, score_call_sideout))
        self.wait(4.5)
        
        # Fade out all court-related assets
        self.play(
            FadeOut(court),
            FadeOut(kitchen_label_left),
            FadeOut(kitchen_label_right),
            FadeOut(hud_bg),
            FadeOut(hud_scores),
            FadeOut(player_A1),
            FadeOut(player_A2),
            FadeOut(player_B1),
            FadeOut(player_B2),
            FadeOut(ball),
            FadeOut(server_ring_B),
            FadeOut(action_text)
        )
        
        # ---------------------------------------------------------------------
        # Scene 7: Summary and Outro
        # ---------------------------------------------------------------------
        summary_title = Text("Key Takeaways", font_size=32, color=YELLOW_D, weight=BOLD).to_edge(UP, buff=0.8)
        self.play(Write(summary_title))
        self.wait(1)
        
        bullet1 = Text("1. Call 3 numbers before serving: Serve Score - Receive Score - Server #", font_size=18, color=WHITE)
        bullet2 = Text("2. Exception: First serve of the game is always called 0 - 0 - 2", font_size=18, color=WHITE)
        bullet3 = Text("3. Only switch sides with your teammate when your team wins a point on serve", font_size=18, color=WHITE)
        bullet4 = Text("4. When you lose a serve on Server 2, a Side-out occurs, and the other team serves", font_size=18, color=WHITE)
        
        bullets = VGroup(bullet1, bullet2, bullet3, bullet4).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(DOWN * 0.2)
        
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT))
            self.wait(2.0)
            
        self.wait(2.5)
        
        outro_text = Text("Now get out there and play some Pickleball!", font_size=24, color=GREEN_C, weight=BOLD).shift(DOWN * 2.8)
        self.play(FadeIn(outro_text, shift=UP))
        self.wait(3.5)
        
        self.play(FadeOut(summary_title, bullets, outro_text))
        self.wait(1)
