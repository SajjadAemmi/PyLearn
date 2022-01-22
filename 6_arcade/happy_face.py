import arcade


# Open the window. Set the window title and dimensions
arcade.open_window(width=600, height=600, window_title="Happy Face Example")

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Clear screen and start render process
arcade.start_render()

yellow = arcade.color.YELLOW
black = arcade.color.BLACK

# Draw the face
arcade.draw_circle_filled(center_x=300, center_y=300, radius=200, color=yellow)

# Draw the right eye
arcade.draw_circle_filled(center_x=370, center_y=350, radius=20, color=black)

# Draw the left eye
arcade.draw_circle_filled(center_x=230, center_y=350, radius=20, color=black)

# Draw the smile
arcade.draw_arc_outline(center_x=300, center_y=280, width=120, height=100, color=black, 
                        start_angle=190, end_angle=350, border_width=10)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()