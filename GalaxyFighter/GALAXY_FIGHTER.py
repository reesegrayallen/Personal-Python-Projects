# Omar Borai  onb3ra
# Reese Allen  rga2uz


                                               #_GALAXY_FIGHTER_#


"""

The images in this game are publicly available for download and for use.

We would like to give credit to the following sites for making them available to us:

* www.uihere.com
* opengameart.org
* www.pixshark.com
* millionthvector.blogspot.com

"""

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# Opening Screen Text
title_space = gamebox.from_text(-300, 250, "GALAXY", 100, "green", bold=True)
title_fighter = gamebox.from_text(1130, 250, "FIGHTER", 100, "green", bold=True)

begin_red = gamebox.from_text(400, 400, "Press Space Bar to Begin...", 50, "red")
begin_other = gamebox.from_text(400, 400, "Press Space Bar to Begin...", 50, "white")

reese_name = gamebox.from_text(90, 610, "REESE ALLEN", 30, "deeppink1")
omar_name = gamebox.from_text(710, 610, "OMAR BORAI", 30, "deeppink")

# Fighter selection text/images
choose_your_fighter = gamebox.from_text(400, 60, "Choose Your Fighter", 65, "deepskyblue3", bold=True)

first_ship = gamebox.from_image(400, 320, "Picture1.png")
first_name = gamebox.from_text(400, 160, "DRAGONFLY", 40, "gold1", italic=True)
first_ship_level_one = gamebox.from_image(400, 535, "Picture1.png")

second_ship = gamebox.from_image(400, 320, "Picture2.png")
second_name = gamebox.from_text(400, 160, "NIGHT HERON", 40, "gold1", italic=True)
second_ship_level_one = gamebox.from_image(400, 535, "Picture2.png")

third_ship = gamebox.from_image(400, 320, "Picture3.png")
third_name = gamebox.from_text(400, 160, "MANTIS", 40, "gold1", italic=True)
third_ship_level_one = gamebox.from_image(400, 535, "Picture3.png")

press_right = gamebox.from_text(645, 580, "Press Right Arrow Key to Scroll ->", 24, "green", italic=True)
press_left = gamebox.from_text(155, 580, "<- Press Left Arrow Key to Scroll", 24, "green", italic=True)
press_select_fighter = gamebox.from_text(400, 485, "Press Space Bar to Select This Fighter", 30, "red")

press_for_level_one = gamebox.from_text(400, 530, "< Press Space Bar to Continue >", 27, "green", italic=True)

you_chose = gamebox.from_text(400, 60, "You've Chosen...", 65, "green", bold=True)

# The scale, adjusted for the size of the user screen
scale_x = 1280.0/1600
scale_y = 720.0/900

# This scales the images to the appropriate size for when we need them
first_ship.width = 300 * scale_x
first_ship.height = 300 * scale_y
first_ship_level_one.width = 100 * scale_x
first_ship_level_one.height = 100 * scale_y

second_ship.width = 300 * scale_x
second_ship.height = 300 * scale_y
second_ship_level_one.width = 100 * scale_x
second_ship_level_one.height = 100 * scale_y

third_ship.width = 300 * scale_x
third_ship.height = 300 * scale_y
third_ship_level_one.width = 100 * scale_x
third_ship_level_one.height = 100 * scale_y

play_game = False
home_screen = True

home_screen_stars = []
home_screen_stars2 = []
home_counter = 0

choice1 = False
choice2 = False
choice3 = False

ship_selected = False
selected_counter = 0
selected_stars = []

play_one1 = False
play_one2 = False
begin_one = False
play_one_countdown = 0

one_instructions1 = gamebox.from_text(400, 50, "Game Instructions", 50, "green", bold=True)
one_instructions2 = gamebox.from_text(400, 50, "Game Instructions Cont.", 50, "green", bold=True)

play_one_right = gamebox.from_text(645, 580, "Press Right Arrow Key to Continue ->", 24, "green", italic=True)
play_one_left = gamebox.from_text(155, 580, "<- Press Left Arrow Key To Go Back", 24, "green", italic=True)
play_one_begin = gamebox.from_text(645, 580, "Press Space Bar to Begin ->", 30, "red", italic=True)

game_starting_in = gamebox.from_text(400, 150, "Game Starting In", 50, "red", italic=True)
level_one_counter = 0
time_until_start = 5
level_one_begin = False

level_one_play = False
level_one_move = False

level_one_in_display = gamebox.from_text(400, 200, "Level One", 40, "deeppink1")
level_two_in_display = gamebox.from_text(400, 200, "Level Two", 40, "deeppink1")
level_three_in_display = gamebox.from_text(400, 200, "Level Three", 40, "deeppink1")
boss_level_in_display = gamebox.from_text(400, 200, "Level Four: Boss Level", 40, "deeppink1")

# Instructions Text (most)
instruct1_line1 = gamebox.from_text(400, 200,  "Now it is time to fight!", 30, "white")
instruct1_line2 = gamebox.from_text(400, 240, " There will be four levels of increasing difficulty.", 25, "white")
instruct1_line3 = gamebox.from_text(400, 280, "The fourth and final level is a Boss Level.", 25, "white")
instruct1_line4 = gamebox.from_text(400, 320, "You will need to destroy as many enemy ships as possible to stay alive.", 25, "white")
instruct1_line5 = gamebox.from_text(400, 360, "Enemy ships will become harder to defeat as the game progresses.", 25, "white")
instruct1_line6 = gamebox.from_text(400, 400, "Your score is a function of how long you survive and the number of ships you destroy.", 25, "white")
instruct1_line7 = gamebox.from_text(400, 440, "Use the Arrow Keys to control the movement of your fighter.", 25, "white")

instruct2_line1 = gamebox.from_text(400, 140, "Your fighter is equipped with 3 weapons to help you destroy the enemy ships.", 25, "white")
instruct2_line2 = gamebox.from_text(400, 180, "Press 'Z' to fire the fast but weak LIGHT GUN.", 25, "white", italic=True)
instruct2_line3 = gamebox.from_text(400, 220, "Press 'X' to fire the slow but piercing DARK GUN.", 25, "white",italic=True)
instruct2_line4 = gamebox.from_text(400, 260, "Press 'Space Bar' to fire the deadly GALAXY LASER.", 25, "white", italic=True)
instruct2_line5 = gamebox.from_text(400, 300, "Your laser is very powerful, but it will take some time to recharge between uses.", 25, "white")
instruct2_line6 = gamebox.from_text(400, 340, "Your Health bar and your Shield bar will be displayed.", 25, "white")
instruct2_line7 = gamebox.from_text(400, 380, "Your fighter will take damage from enemy projectiles.", 25, "white")
instruct2_line8 = gamebox.from_text(400, 420, "If your Health bar is depleted, you will die, and the game will be over.", 25, "white")
instruct2_line9 = gamebox.from_text(400, 460, "Replenish your Shield by collecting the 'S'-shaped power ups.", 25, "white")


# Text for game over screen (if boss not defeated)
game_over_text = gamebox.from_text(400, 290, "GAME OVER", 120, "red", bold=True)
press_to_exit = gamebox.from_text(400, 550, "< Press ' F ' Key to Exit >", 24, "white", italic = True)

# Text for game win screen (if boss defeated)
game_win_text = gamebox.from_text(400, 225, "YOU WIN!", 150, "GREEN", bold=True)

game_stars = []

blink_counter = 0

score = 0
level = 1
level_timer = 0

weak_projectile_counter = 5
weak_player_projectiles = []
strong_projectile_counter = 20
strong_player_projectiles = []
laser_counter = 0
laser_ready = False

health_text = gamebox.from_text(675, 25, "HEALTH", 20, "white")
shield_text = gamebox.from_text(675, 75, "SHIELD", 20, "white")
laser_text = gamebox.from_text(675, 125, "LASER", 20, "white")
ready_text = gamebox.from_text(675, 150, "READY!", 20, "white")
health = 100
shield = 100

shield_powerups = []

# handle game win or game over display
game_over = False
game_won = False

shield_down = False

# in-game ship appearance/scaling
Enemy_2 = gamebox.from_image(random.randint(50, 750), 50, "Enemy_2.png")
Enemy_2.width = 100 * scale_x
Enemy_2.height = 100 * scale_y
Enemy_3 = gamebox.from_image(random.randint(50, 750), 50, "Enemy_3.png")
Enemy_3.width = 100 * scale_x
Enemy_3.height = 100 * scale_y
Boss = gamebox.from_image(400, -250, "Boss.png")
Boss.width = 500 * scale_x
Boss.height = 500 * scale_y

current_enemies = 0
enemy_counter = 0
enemy_list = []
enemy_info = []
enemy_health_bars = []

Enemy_1_projectiles = []
boss_special_counter = 0
boss_special_projectiles = []


def tick (keys):

    # The code pretty much follows the flow of the screens and the game

    global home_screen, home_counter, play_game, title_space, title_fighter, boss_special_projectiles
    global choice1, choice2, choice3, ship_selected, myfighter, myname, selected_counter
    global play_one1, play_one_countdown, begin_one, one_instructions1, one_instructions2, play_one2
    global level_one_counter, level_one_begin, time_down, time_until_start, game_starting_in
    global level_one_play, scale_x, scale_y, level_one_move, boss_special_counter
    global first_ship_level_one, second_ship_level_one, third_ship_level_one, myfighterplay
    global weak_projectile_counter, weak_player_projectiles, health_text, shield_text, health, shield, health_bar, shield_bar
    global game_over, game_won, shield_down, game_stars, strong_projectile_counter, strong_player_projectiles, laser_counter
    global laser_ready, ready_text, blink_counter, score, Enemy_1, Enemy_2, Enemy_3, Boss, current_enemies, enemy_counter
    global enemy_list, enemy_info, enemy_health_bars, Enemy_1_projectiles, shield_powerups, level, level_timer
    global level_one_in_display, level_two_in_display, level_three_in_display, boss_level_in_display
    global instruct1_line1, instruct1_line2, instruct1_line3, instruct1_line4, instruct1_line5, instruct1_line6, instruct1_line7
    global instruct2_line1, instruct2_line2, instruct2_line3, instruct2_line4, instruct2_line4, instruct2_line6, instruct2_line7, instruct2_line8, instruct2_line9

    if home_screen:
        home_counter += 1
        camera.clear("gray11")
        if home_counter > 20:
            if home_counter % 10:
                num_stars = random.randint(0, 10)  # The number of stars is random
                star_size = random.randint(1, 5)  # The size of the stars is random
                for i in range(num_stars):  # This is what creates the stars
                    home_screen_stars.append(gamebox.from_color(random.randint(0, 800), 0, "white", star_size, star_size))
                    home_screen_stars2.append(gamebox.from_color(random.randint(0, 800), 600, "purple", star_size, star_size))
                    # There is a list for both the purple stars that move up and the white stars that move down

            # This is what causes them to move
            for element in home_screen_stars:
                element.y += 3
                if element.y > 600:
                    home_screen_stars.remove(element)
                camera.draw(element)

            for element in home_screen_stars2:
                element.y -= 3
                if element.y < 0:
                    home_screen_stars2.remove(element)
                camera.draw(element)

        # This is what causes the word "FIGHTER" to move across and to the left
        if home_counter > 50:
            if title_fighter.x > 570:
                title_fighter.x += (-4)
            camera.draw(title_fighter)

        # This is what causes the word "GALAXY" to move across and to the right
        if home_counter > 50:
            if title_space.x < 210:
                title_space.x += 4
            camera.draw(title_space)

        # This draws our names and moves them upwards on the title screen
        if home_counter > 170:
            if reese_name.y > 565:
                reese_name.y -= 2
            if omar_name.y > 565:
                omar_name.y -= 2
            camera.draw(reese_name)
            camera.draw(omar_name)

        # This is what causes the 'Press to Space Bar to Begin' to flash red and white
        if home_counter > 230:
            camera.draw(begin_red)
            camera.draw(reese_name)
            camera.draw(omar_name)
        if home_counter > 260:
            camera.draw(begin_other)
        if home_counter > 290:
            camera.draw(begin_red)
        if home_counter > 320:
            camera.draw(begin_other)
        if home_counter > 350:
            camera.draw(begin_red)
        if home_counter > 380:
            camera.draw(begin_other)
        if home_counter > 410:
            camera.draw(begin_red)

        if home_counter > 230:
            if pygame.K_SPACE in keys:
                choice1 = True
            keys.clear()

    # This causes the first ship to be displayed in the selection menu
    if choice1:
        home_screen = False
        choice3 = False
        choice2 = False
        camera.clear("gray11")
        camera.draw(choose_your_fighter)
        camera.draw(first_ship)
        camera.draw(press_right)
        camera.draw(press_select_fighter)
        camera.draw(first_name)

        if pygame.K_RIGHT in keys:
            choice2 = True

        if pygame.K_SPACE in keys:
            myfighter = first_ship
            myname = first_name
            myfighterplay = first_ship_level_one
            ship_selected = True
        keys.clear()

    # This causes the second ship to be displayed in the selection menu
    if choice2:
        choice1 = False
        choice3 = False
        camera.clear("gray11")
        camera.draw(choose_your_fighter)
        camera.draw(press_right)
        camera.draw(press_left)
        camera.draw(press_select_fighter)
        camera.draw(second_ship)
        camera.draw(second_name)

        if pygame.K_LEFT in keys:
            choice1 = True
            choice2 = False

        if pygame.K_RIGHT in keys:
            choice3 = True
            choice2 = False

        if pygame.K_SPACE in keys:
            myfighter = second_ship
            myname = second_name
            myfighterplay = second_ship_level_one
            ship_selected = True
        keys.clear()

    # This causes the third ship to be displayed in the selection menu
    if choice3:
        choice1 = False
        choice2 = False

        if pygame.K_LEFT in keys:
            choice2 = True
            choice3 = False

        if pygame.K_SPACE in keys:
            myfighter = third_ship
            myname = third_name
            myfighterplay = third_ship_level_one
            ship_selected = True

        keys.clear()
        camera.clear("gray11")
        camera.draw(choose_your_fighter)
        camera.draw(press_left)
        camera.draw(press_select_fighter)
        camera.draw(third_ship)
        camera.draw(third_name)

    # Once the user presses the space bar to choose a ship, this becomes true
    if ship_selected:
        selected_counter += 1
        choice1 = False
        choice2 = False
        choice3 = False
        camera.clear("black")

        # This creates and moves the stars for the "You've Chosen" screen
        if selected_counter % 5:
            num_stars = random.randint(0, 10)
            star_size = random.randint(1, 5)
            for i in range(num_stars):
                selected_stars.append(gamebox.from_color(random.randint(0, 800), 0, "cadetblue1", star_size, star_size))

        for element in selected_stars:
            element.y += 12
            if element.y > 600:
                selected_stars.remove(element)
            camera.draw(element)
        camera.draw(myfighter)
        camera.draw(you_chose)
        camera.draw(myname)
        camera.draw(press_for_level_one)

        if pygame.K_SPACE in keys:
            play_one1 = True

    # This is for the first Instructions Screen
    if play_one1:
        ship_selected = False
        play_one2 = False
        camera.clear("black")
        camera.draw(instruct1_line1)
        camera.draw(instruct1_line2)
        camera.draw(instruct1_line3)
        camera.draw(instruct1_line4)
        camera.draw(instruct1_line5)
        camera.draw(instruct1_line6)
        camera.draw(instruct1_line7)
        camera.draw(one_instructions1)
        camera.draw(play_one_right)

        if pygame.K_RIGHT in keys:
            play_one2 = True

    # This is for the second instructions Instructions Screen
    if play_one2:
        play_one1 = False
        ship_selected = False
        camera.clear("black")
        camera.draw(one_instructions2)
        camera.draw(play_one_left)
        camera.draw(play_one_begin)
        camera.draw(instruct2_line1)
        camera.draw(instruct2_line2)
        camera.draw(instruct2_line3)
        camera.draw(instruct2_line4)
        camera.draw(instruct2_line5)
        camera.draw(instruct2_line6)
        camera.draw(instruct2_line7)
        camera.draw(instruct2_line8)
        camera.draw(instruct2_line9)
        if pygame.K_LEFT in keys:
            play_one1 = True

        if pygame.K_SPACE in keys:
            level_one_begin = True

    # This is for the countdown screen before level one begins
    if level_one_begin:
        level_one_counter += 1
        if level_one_counter % 30 == 0:
            time_until_start -= 1
        time_down = gamebox.from_text(400, 320, str(time_until_start), 220, "red", bold=True)
        camera.clear("gray11")
        camera.draw(time_down)
        camera.draw(game_starting_in)

        if time_until_start == 0:
            level_one_play = True

    if level_one_play:
        camera.clear("gray11")
        level_one_move = True

    # This creates a new version of the ship the user chose, resizes and displays it, and allows the user to move it
    if level_one_move:

        # Adds stars to the game screen
        num_stars = random.randint(0, 3)  # The number of stars is random
        star_size = random.randint(1, 3)  # The size of the stars is random
        for i in range(num_stars):  # This is what creates the stars
            game_stars.append(gamebox.from_color(random.randint(0, 800), 0, "white", star_size, star_size))
        for star in game_stars:
            star.y += 15
            camera.draw(star)
            if star.y > 605:
                game_stars.remove(star)

        # Momentum-based movement system with movement in all directions
        if pygame.K_RIGHT in keys:
            myfighterplay.speedx += 1.1

        if pygame.K_LEFT in keys:
            myfighterplay.speedx -= 1.1

        if pygame.K_UP in keys:
            myfighterplay.speedy -= 1.1

        if pygame.K_DOWN in keys:
            myfighterplay.speedy += 1.1

        # adjusts speed when a defined maximum is reached
        if myfighterplay.speedy > 11:
            myfighterplay.speedy = 11

        if myfighterplay.speedy < -11:
            myfighterplay.speedy = -11

        if myfighterplay.speedx > 11:
            myfighterplay.speedx = 11

        if myfighterplay.speedx < -11:
            myfighterplay.speedx = -11

        # Moving the player's ship
        myfighterplay.move_speed()

        # System adds boundaries
        if myfighterplay.x > 780:
            myfighterplay.x = 780
            myfighterplay.speedx = 0

        if myfighterplay.x < 20:
            myfighterplay.x = 20
            myfighterplay.speedx = 0

        if myfighterplay.y > 568:
            myfighterplay.y = 568
            myfighterplay.speedy=0

        if myfighterplay.y < 32:
            myfighterplay.y = 32
            myfighterplay.speedy = 0

        # The algorithm to shoot weak projectiles
        if pygame.K_z in keys and weak_projectile_counter > 5:
            weak_player_projectiles.append(gamebox.from_color(myfighterplay.x+1,myfighterplay.y-25, "red", 5, 15))
            weak_projectile_counter = 0
        for projectile in weak_player_projectiles:
            projectile.y -= 18
            camera.draw(projectile)
            if projectile.y < -10:
                weak_player_projectiles.remove(projectile)
        weak_projectile_counter += 1

        # The algorithm to shoot strong projectiles
        if pygame.K_x in keys and strong_projectile_counter > 50:
            strong_player_projectiles.append(gamebox.from_color(myfighterplay.x+1,myfighterplay.y-25, "purple", 8, 20))
            strong_projectile_counter = 0
        for projectile in strong_player_projectiles:
            projectile.y -= 8
            camera.draw(projectile)
            if projectile.y < -10:
                strong_player_projectiles.remove(projectile)
        strong_projectile_counter += 1

        # The algorithm to shoot laser
        if laser_counter >= 120:
            laser_counter = 120
        if pygame.K_SPACE in keys and laser_counter >= 120:
            laser_ready = True
        if laser_ready:
            if laser_counter > 20:
                laser_counter = 0
            if laser_counter < 20:
                laser_red = gamebox.from_color(myfighterplay.x,myfighterplay.y-425, "red", 15, 800)
                laser_orange = gamebox.from_color(myfighterplay.x,myfighterplay.y-425, "orange", 10, 800)
                laser_yellow = gamebox.from_color(myfighterplay.x,myfighterplay.y-425, "yellow", 4, 800)
                camera.draw(laser_red)
                camera.draw(laser_orange)
                camera.draw(laser_yellow)

        if 20 <= laser_counter < 120:
            laser_ready = False
        if not laser_counter == 120:
            laser_counter += 1

        # The algorithm for the health bar and shield bars
        if health > 100:
            health = 100
        if shield > 100:
            shield = 100
        if health < 0:
            health = 0
        if shield < 0:
            shield = 0
        if health <= 0:
            game_over = True
        if shield <= 0:
            shield_down = True
        if shield > 0:
            shield_down = False

        health_bar = gamebox.from_color(675 - (100 - health), 50, "green", health * 2, 25)
        shield_bar = gamebox.from_color(675 - (100 - shield), 100, "blue", shield * 2, 25)
        laser_bar = gamebox.from_color(675 - (100 - (laser_counter - 20)), 150, "red", (laser_counter - 20) * 2, 25)

        # This creates enemies
        enemy_counter += 1

        if level_timer < 3500:
            random_enemy = random.randint(1, level)
            # (info = (health,max_health,attack speed,shot_counter,speed,moving down,projectile speed,direction,scaling,#,burst,burstcount)
            if random_enemy == 1 and current_enemies < 15 and enemy_counter >= 60:
                Enemy_1 = gamebox.from_image(random.randint(50, 750), -75, "Enemy_1.png")
                Enemy_1.width = 100 * scale_x
                Enemy_1.height = 100 * scale_y
                current_enemies += 1
                enemy_list.append(Enemy_1)
                enemy_info.append([7+level, 7+level, 32-2*level, 15, 2+level, 0, 9+level, -1, 4/3, 1.75, 1, 0])
                enemy_counter = 0

            # (info = (health,max_health,attack speed,shot_counter,speed,moving down,projectile speed,direction,scaling,#,burst,burstcount)
            if random_enemy == 2 and current_enemies < 15 and enemy_counter >= 60:
                Enemy_1 = gamebox.from_image(random.randint(50, 750), -75, "Enemy_2.png")
                Enemy_1.width = 100 * scale_x
                Enemy_1.height = 100 * scale_y
                current_enemies += 1
                enemy_list.append(Enemy_1)
                enemy_info.append([2+level, 2+level, 24-2*level, 10, 6+level, 0, 13+level, -1, 2/3, 1, 10, 0])
                enemy_counter = 0

            # (info = (health,max_health,attack speed,shot_counter,speed,moving down,projectile speed,direction,scaling,#,burst,burstcount)
            if random_enemy == 3 and current_enemies < 15 and enemy_counter >= 60:
                Enemy_1 = gamebox.from_image(random.randint(50, 750), -75, "Enemy_3.png")
                Enemy_1.width = 100 * scale_x
                Enemy_1.height = 100 * scale_y
                current_enemies += 1
                enemy_list.append(Enemy_1)
                enemy_info.append([20, 20, 15, 15, 1, 0, 8, -1, 2, 2.5, 5, 0])
                enemy_counter = 0

        # handles boss ship appearance for Level Four
        if level_timer == 3600:
            enemy_list.clear()
            enemy_info.clear()
            enemy_health_bars.clear()
            current_enemies = 0

        if level_timer == 3700:
            Boss = gamebox.from_image(400, -75, "Boss_ship.png")
            Boss.width = 200 * scale_x
            Boss.height = 200 * scale_y
            current_enemies += 1
            enemy_list.append(Boss)
            enemy_info.append([120, 120, 10, 20, 8, 0, 15, -1, 4.5, 1.5, 10, 0])
            enemy_counter = 0

        # This manages enemies

        for enemy in enemy_list:
            index = enemy_list.index(enemy)
            try:
                enemy_health_bars[index] = enemy_health_bars[index]
            except IndexError:
                if level_timer < 3600:
                    enemy_health_bars.insert(index,gamebox.from_color(enemy.x - 10 * (enemy_info[index][1]-enemy_info[index][0])/enemy_info[index][8],enemy.y-50,"green", enemy_info[index][0]/enemy_info[index][8]*20, 5))
                elif level_timer > 3600:
                    enemy_health_bars.insert(index, gamebox.from_color(400 - 10 * (enemy_info[index][1] - enemy_info[index][0]) / enemy_info[index][8],enemy.y - 140, "green", enemy_info[index][0] / enemy_info[index][8] * 20, 15))

            # Enemy Health
            if level_timer < 3600:
                enemy_health_bars[index] = gamebox.from_color(enemy.x - 10 * ((enemy_info[index][1] - enemy_info[index][0])/enemy_info[index][8]), enemy.y - 50,"green", enemy_info[index][0]/enemy_info[index][8] * 20, 5)
            elif level_timer > 3600:
                enemy_health_bars[index] = gamebox.from_color(400 - 10 * (enemy_info[index][1] - enemy_info[index][0]) / enemy_info[index][8], enemy.y - 140,"green", enemy_info[index][0] / enemy_info[index][8] * 20, 15)
            for projectile in weak_player_projectiles:
                if enemy.touches(projectile) and level_timer < 3600:
                    enemy_info[index][0] -= 1
                    weak_player_projectiles.remove(projectile)
                if enemy.touches(projectile) and level_timer > 3600:
                    enemy_info[index][0] -= .3
                    weak_player_projectiles.remove(projectile)
            for projectile in strong_player_projectiles:
                if enemy.touches(projectile) and level_timer < 3600:
                    enemy_info[index][0] -= 1
                if enemy.touches(projectile) and level_timer > 3600:
                    enemy_info[index][0] -= .5
            if laser_counter < 20:
                if enemy.touches(laser_red) and level_timer < 3600:
                    enemy_info[index][0] -= 1
                if enemy.touches(laser_red) and level_timer > 3600:
                    enemy_info[index][0] -= .5

            # Enemy attacks (special conditions for non-boss ships and boss ship)
            if enemy_info[index][3] >= enemy_info[index][2]:
                if enemy_info[index][11] <= enemy_info[index][10] and level_timer < 3600:
                    Enemy_1_projectiles.append(gamebox.from_color(enemy.x, enemy.y + 25, "yellow", 5, 10))
                    enemy_info[index][11] += 1
                    if enemy_info[index][11] >= enemy_info[index][10]:
                        enemy_info[index][3] = 0
                        enemy_info[index][11] = 0
                if enemy_info[index][11] <= enemy_info[index][10] and level_timer > 3600:
                    Enemy_1_projectiles.append(gamebox.from_color(enemy.x, enemy.y + 25, "lightcoral", 7, 15))
                    enemy_info[index][11] += 1
                    if enemy_info[index][11] >= enemy_info[index][10]:
                        enemy_info[index][3] = 0
                        enemy_info[index][11] = 0
                enemy_info[index][3] = 0
            else:
                enemy_info[index][3] += 1

            for projectile in Enemy_1_projectiles:
                projectile.y += enemy_info[index][6]/len(enemy_list)
                camera.draw(projectile)
                if projectile.y > 650:
                    Enemy_1_projectiles.remove(projectile)
                if myfighterplay.touches(projectile) and level_timer < 3600:
                    if shield_down:
                        health -= 5
                    else:
                        shield -= 5
                    Enemy_1_projectiles.remove(projectile)
                if myfighterplay.touches(projectile) and level_timer > 3600:
                    if shield_down:
                        health -= 8
                    else:
                        shield -= 8
                    Enemy_1_projectiles.remove(projectile)

                boss_special_counter += 1
                if level_timer >= 3600 and boss_special_counter >= 60:
                    boss_special_counter = 0
                    boss_special_projectiles.append((gamebox.from_color(random.randint(10, 790), -10, "brown", 25, 25)))
                for projectile in boss_special_projectiles:
                    if projectile.y >= 650:
                        boss_special_projectiles.remove(projectile)
                    if myfighterplay.touches(projectile):
                        if shield_down:
                            health -= 10
                        else:
                            shield -= 15
                        boss_special_projectiles.remove(projectile)
                    projectile.y += 1
                    camera.draw(projectile)

            if myfighterplay.touches(enemy):
                if shield_down:
                    health -= 1
                else:
                    shield -= 1

            # Moving Enemies
            if enemy_info[index][5] < 30 * enemy_info[index][9]:
                enemy.y += 5
                enemy_info[index][5] += 1
            if enemy_info[index][5] >= 30 * enemy_info[index][9]:
                if enemy.x <= 50:
                    enemy_info[index][7] = 1
                if enemy.x >= 750:
                    enemy_info[index][7] = -1
                enemy.x += enemy_info[index][7] * enemy_info[index][4]

            # Killing Enemies
            if enemy_info[index][0] <= 0:
                if random.randint(0, 5) == 0:
                    shield_powerups.append(gamebox.from_text(enemy.x, enemy.y+25, "S", 50, "pink"))
                enemy_list.pop(index)
                enemy_info.pop(index)
                enemy_health_bars.pop(index)
                current_enemies -= 1
                score += 100

        # Manages shield power ups
        for powerup in shield_powerups:
            camera.draw(powerup)
            powerup.y += 6
            if myfighterplay.touches(powerup):
                shield += 20
                shield_powerups.remove(powerup)

        # Increase score per tick and score_box / level
        level_timer += 1
        if level_timer % 2 == 0 and not game_over and not game_won:
            score += 1
        score_box = gamebox.from_text(75, 25, "Score:  " + str(score), 20, "white")
        level_box = gamebox.from_text(75, 50, "Level:  " + str(level), 20, "white")

        if level_timer == 1200:
            level += 1
        if level_timer == 2400:
            level += 1
        if level_timer == 3600:
            level += 1

        camera.draw(myfighterplay)

        # handles win screen appearance if boss defeated
        if level_timer > 3800 and len(enemy_list) == 0 and not game_won:
            score += 2500
            game_won = True

        for enemy in enemy_list:
            camera.draw(enemy)
        for bar in enemy_health_bars:
            camera.draw(bar)
        camera.draw(shield_text)
        camera.draw(health_text)
        camera.draw(laser_text)
        camera.draw(health_bar)
        camera.draw(shield_bar)
        camera.draw(laser_bar)
        camera.draw(score_box)
        camera.draw(level_box)
        if 15 < level_timer < 85:
            camera.draw(level_one_in_display)
        if 1210 < level_timer < 1280:
            camera.draw(level_two_in_display)
        if 2410 < level_timer < 2480:
            camera.draw(level_three_in_display)
        if 3610 < level_timer < 3680:
            camera.draw(boss_level_in_display)
        if laser_counter == 120:
            blink_counter += 1
            if blink_counter < 15:
                camera.draw(ready_text)
            if blink_counter >= 30:
                blink_counter = 0

    # manages game over screen and score display
    if game_over:
        level_one_move = False
        camera.clear("black")
        camera.draw(game_over_text)
        final_score_text = gamebox.from_text(400, 370, "SCORE: " + str(score), 50, "green")
        camera.draw(final_score_text)
        camera.draw(press_to_exit)
        if pygame.K_f in keys:
            exit()

    # manages game win screen and score display
    if game_won:
        level_one_move = False
        camera.clear("black")
        camera.draw(game_win_text)
        defeated_boss_win_text = gamebox.from_text(400, 300, "You Successfully Defeated the Boss", 30, "green")
        final_score_win_text = gamebox.from_text(400, 350, "SCORE: " + str(score), 50, "red")
        camera.draw(defeated_boss_win_text)
        camera.draw(final_score_win_text)
        camera.draw(press_to_exit)
        if pygame.K_f in keys:
            exit()

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
