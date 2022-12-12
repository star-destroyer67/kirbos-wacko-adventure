@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_up_pressed():
    mySprite.set_image(assets.image("""
        kirby back
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def durimg_suck():
    controller.move_sprite(mySprite, 0, 0)

def on_b_pressed():
    global suck
    durimg_suck()
    animation.run_image_animation(mySprite,
        assets.animation("""
            kirby succ
        """),
        500,
        False)
    suck = True
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def end_of_boss_1():
    info.change_score_by(10)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    info.set_life(3)
    save_star_part_1()
def boss_1():
    global projectileTimeCheck, ProjectileDelay, projectileX, boss1
    projectileTimeCheck = 0
    ProjectileDelay = 500
    pause(2000)
    for index in range(10):
        projectileX = sprites.create(assets.image("""
            spoike boi
        """), SpriteKind.projectile)
        projectileX.set_position(randint(0, 160), randint(0, 120))
        projectileX.follow(mySprite, 5)
    info.start_countdown(10)
    boss1 = True

def on_a_pressed():
    mySprite.set_stay_in_screen(True)
    myEnemy.set_stay_in_screen(True)
    if mySprite.x > 104 and mySprite.x < 132 and (mySprite.y > 103 and mySprite.y < 117) and level == 1:
        scene.set_background_image(assets.image("""
            unobrow
        """))
        boss_1()
    elif mySprite.x > 127 and mySprite.x < 137 and (mySprite.y > 42 and mySprite.y < 51) and level == 2:
        scene.set_background_image(assets.image("""
            somewhat anger
        """))
        boss_2()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def StopSucking():
    global suck
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(assets.image("""
        kirby
    """))
    myEnemy.follow(mySprite, 5)
    suck = False
def save_star_part_1():
    global animation2, time_chek, savestar1, level
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    scene.set_background_image(assets.image("""
        B
    """))
    animation2 = sprites.create(assets.image("""
        e
    """), SpriteKind.player)
    animation2.set_position(0, 0)
    animation.run_image_animation(animation2,
        assets.animation("""
            get sploded
        """),
        500,
        False)
    time_chek = game.runtime() + 9000
    savestar1 = True
    controller.move_sprite(mySprite, 100, 100)
    level = 2

def on_left_pressed():
    mySprite.set_image(assets.image("""
        kirby left
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def boss_2():
    global projectile, boss2TimeCheck, Boss2Mines
    for index2 in range(10):
        projectile = sprites.create_projectile_from_side(assets.image("""
                dna projectile
            """),
            randint(50, 160),
            0)
        projectile.set_position(0, randint(160, 0))
    boss2TimeCheck = game.runtime() + 5000
    Boss2Mines = 1

def on_right_pressed():
    mySprite.set_image(assets.image("""
        kirby right
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global projectileTimeCheck
    if projectileTimeCheck < game.runtime():
        projectileTimeCheck = game.runtime() + ProjectileDelay
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_down_pressed():
    mySprite.set_image(assets.image("""
        kirby
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_b_released():
    controller.move_sprite(mySprite, 100, 100)
    StopSucking()
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def end_of_boss_2():
    global animation2, time_chek, level
    info.change_score_by(10)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    animation2 = sprites.create(assets.image("""
        e
    """), SpriteKind.player)
    animation2.set_position(0, 0)
    scene.set_background_image(img("""
        ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
    """))
    animation.run_image_animation(animation2,
        [img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa5555aafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff444444444444444fffffffffffffffffffffffffffffffffffa5a55a5afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44fffffffffffff444fffffffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ffff5555555fffff444fffffffffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff555ffffff55555fff44fffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f555fffffffffffff5555f444ffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffff55ff444ffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffffff55ff44fffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffff55ff44ffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffffff55f4fffffffffffffffaaaaaaaa5a55a5aaaaaaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff5ffffffffffffffffffffff55f44fffffffffffff5a55a55555aa5555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ff5ffffffffffffffffffffffff5f444fffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44f55fffffffffffffffffffffff555f44ffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5f44fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffff5ff4fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5544ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffffff54ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff445fffffffffffffffffffffffffffff5555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff4f5fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffff44fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff4ffffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff4fffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff45ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5fffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffff5ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff5fffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff55ffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffff5555555555555555555555555555455555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555545555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555a55555a55555555fffffffffffffffff
                        fffffffffffffff555555a55555a555555555555555554555555555555555555555555555a55a55555555555a55a555555555555555555555555aa55555a55555a555a555555555fffffffffffffffff
                        fffffffffffffff5555555a555a5555555555555555555445555555555555555555555555555a55555555555a555555555555555555a5555555a5555555a555555a5a5555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555554555555555555555555555555555a55555555555a555555555555555555a5555aaa5555555a55555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555555555445555555555555555555555555a55555555555a55555555555555555a555555555555555a5555a55a5a5555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555555554555555555555555555555555a55555555555a55555555555555555a555555a555a55555555aa555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555aa5555555555555555555445555555555555555555555a55555555555a5555555555555555a55555aa5555a5555555a55555555555555555fffffffffffffffff
                        ffffffffffffffffffff555aaa555aaaaa555555555555555555544455555555555555555555a55555555555a555555555555555aa5555a555555a555555555555aaa5555fffffffffffffffffffffff
                        ffffffffffffffffffff55a555a555555aaaa555555555555555555445555555555555555555a55555555555a55555555555555555555aa55555555aa5555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555aaaa555555555555555544455555555555555555a55555555555a55555555555555555555555555555a555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555aaa5555555555555555445555555555555555a55555555555a55555555555a555aa555a55aa555a5555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555aaa5555555555555544555555555555555a55555555555a55555555555a55aa5555a5aa555555555555aaaaaa555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555aa55555555555554455555555555555a55555555555a5555555555555aa5555aa555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555aaaaa55555555544455555555555555555555555555555555555555a55a5aa5555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555555555aaa55555555444555555555555555555555555555555555555555a555555555555555a5555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555555555aaaaa55555444455555555555555555555555555555555aa55a555555555a555555aaa55555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555aaa555554455555555555555555555555555555aaa5555a5555555aa5555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555aaaa55344455555555555555555555555555a55555555555aaa555555aaa555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555aaa555445555555555555555555555555555555555555555555aaa555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555aa55544555555555555555555555555555a5555aa55555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555555aa555445555555555555555555aa55555a555aa555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555555555555555555555555555555aa5554445555555555555555555555aa555555555555a55555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555555aaaaaaaaa55555555555555555555a55a55555555aa555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555a4555555555555555aa5555aa555555aa55555a555fffff455ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555555555555555555555555445555555555555a55555aa55aa5555555aaa5555ffffff4555ffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555555555555555555555555544555555555555555555555a5555555555555555fffffff4455fffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555555555555555555555555555555555555554444555555555555555555555555aa55555555ffffffff4455ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555555555555555555555555555555444555555555555aaa5555aaa5555555555fffffffff4445fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555555555555555555555555555555554455555555aaa55555555555555555555ffffffffffff45ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555544555555555555555555555555555555fffffffffffff4ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555555555555555555555555555555555545554555555a5555555555555555555fffffffffffff44fffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555555555aa5555aa55555555555555555545554555aa555555555555ffffffffffffffffffffff44ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff5555555555555555aa5555aa55555555555555555555455555555555555555555fffffffffffffffffffffff44fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555555a55555aa555555555555555555555445455555555555555555ffffffffffffffffffffffff4fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555aaa55555a55555555555555555555555544545555555555555555ffffffffffffffffffffffff45ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555a5555555a555555555555555555555555554444555555555555555ffffffffffffffffffffffff44ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555aa5555555a55555555aa555555555555555555444555555555555555fffffffffffffffffffffffff45fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555a555aa555a55555a555a555555555555555555555444455455555555555555555fffffffffffffffff455ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555a555a555555555aa5555a555555555555555555555555444445555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555a55555555a55555a5555555555555555555555555555544555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555aa55555aa5555555aa555555a5555555555555555555555555555554444555555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555a55555a555555555a555555a55555555555555555555555555555555554445555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555a555555555555555a5555555a55555555555555555555555555555555555544455555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555aa55555555555555aa555555a555555555555555555555555555555555555554444555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555a55555aa5555aa55a55555555a555555555555555555555555555555555555555554445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555aa555aaa5555aa55a555555555a555555555555555555555555555555555555555555445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555aa55aa555555aa555a55555555a5555555555555555555555555555555555555555555554555fffffffffffffff44ff5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555a55aa555555aa5555555555555a5555555555555555555555555555555555555555555555455fffffffffffffff4ff55ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555a55a555555555555555555a5555a5555555555555555555555555555555555555555555555545ffffffffffff444f55ffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55a55555555555555555a5555a555a55555555555555555555555555555555555555555555555554fffffffffff44f55ffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555aa555555a555aa55a5555555555555555555555555555555555555555555555555544fffffff444f55ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555a555555aa5555a555a555555555555555555555555555555555555555555555555555444444445555ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555a55a555555a55555a55555555555555555555555555555555555555555555555555555555ff5555555fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555aa55555555a55555a555555555555555555555555555555555555555555555555555555555ffffff444fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555aa555555555a555555a55555555555fffffffffffffff555555555555555555555555555555555555555f4444fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555aa5555555555555555a555555555555fffffffffffffff555555555555555555555555555555555555555ffff44ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555aa5555aa5555555555aa555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555a55555aa555aaa5555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55555aa555aa555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55aaa555aaa5555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555a55a5555aaa55555555a5555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555a55aa5555a555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555a55555a555a555a5555a5555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a555a555a55555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a5555555555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555aa555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a555555aa5555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555a555555a55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a5a5a5555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a55555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """),
            img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa5555aafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff444444444444444fffffffffffffffffffffffffffffffffffa5a55a5afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44fffffffffffff444fffffffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ffff5555555fffff444fffffffffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff555ffffff55555fff44fffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f555fffffffffffff5555f444ffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffff55ff444ffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffffff55ff44fffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffff55ff44ffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffffff55f4fffffffffffffffaaaaaaaa5a55a5aaaaaaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff5ffffffffffffffffffffff55f44fffffffffffff5a55a55555aa5555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ff5ffffffffffffffffffffffff5f444fffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44f55fffffffffffffffffffffff555f44ffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5f44fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffff5ff4fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5544ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffffff54ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff445fffffffffffffffffffffffffffff5555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff4f5fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffff44fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff4ffffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff4fffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff45ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5fffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffff5ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff5fffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff55ffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffff5555555555555555555555555555455555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555545555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555a55555a55555555fffffffffffffffff
                        fffffffffffffff555555a55555a555555555555555554555555555555555555555555555a55a55555555555a55a5555555555555555555555555555555555555a555a555555555fffffffffffffffff
                        fffffffffffffff5555555a555a5555555555555555555445555555555555555555555555555a55555555555a55522225555555522255555555222555555555555a5a5555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555554555555555555555555555555555a55555555555a555222255555555222555555552225555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555555555445555555555555555555555555a55555555555a55522225555555522255555555222555555555555a5a5555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555555554555555555555555555555555a55555555555a555222255555555222555555552225555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555aa5555555555555555555445555555555555555555555a55555555555a555555544442222222222244445555555555555555555555555555fffffffffffffffff
                        ffffffffffffffffffff555aaa555aaaaa555555555555555555544455555555555555555555a55555555555a55555554444222222222224444555555555555555aaa5555fffffffffffffffffffffff
                        ffffffffffffffffffff55a555a555555aaaa555555555555555555445555555555555555555a55555555555a5555555444422222222222444455555555555555a555a555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555aaaa555555555555555544455555555555555555a55555555555a55555554444222222222224444555555555555555aaa5555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555aaa5555555555555555445555555555555555a55555555555a555555522224444555444422225555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555aaa5555555555555544555555555555555a55555555555a555555522224444555444422225555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555aa55555555555554455555555555555a55555555555a555555522224444555444422225555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555aaaaa5555555554445555555555555555555555555555222244445555111555544442225555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555555555aaa55555555444555555555555555555555555555222244445555111555544442225555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555555555aaaaa5555544445555555555555555555555555222244445555111555544442225555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555aaa555554455555555555555555555555552222444455551115555444422255555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555aaaa55344455555555555555555555555555222244445554444222255555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555aaa555445555555555555555555555555222244445554444222255555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555aa55544555555555555555555555555222244445554444222255555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555555aa5554455555555555555555555555444422222222222444455555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555555555555555555555555555555aa555444555555555555555555555444422222222222444455555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555555aaaaaaaaa5555555555555555555444422222222222444455555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555a45555555555555555554444222222222224444555fffff455ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555544555555555555522225555555522255555555222ffffff4555ffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555554455555555555522225555555522255555555222fffffff4455fffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555544445555555522225555555522255555555222ffffffff4455ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555544455555555555555555555555555555555fffffffff4445fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555445555555555555555555555555555555ffffffffffff45ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555544555555555555555555555555555555fffffffffffff4ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555554555455555555555555555555555555fffffffffffff44fffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555555555aa5555aa5555555555555555554555455555555555555555ffffffffffffffffffffff44ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff5555555555555555aa5555aa55555555555555555555455555555555555555555fffffffffffffffffffffff44fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555555a55555aa555555555555555555555445455555555555555555ffffffffffffffffffffffff4fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555aaa55555a55555555555555555555555544545555555555555555ffffffffffffffffffffffff45ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555a5555555a555555555555555555555555554444555555555555555ffffffffffffffffffffffff44ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555aa5555555a55555555aa555555555555555555444555555555555555fffffffffffffffffffffffff45fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555a555aa555a55555a555a555555555555555555555444455455555555555555555fffffffffffffffff455ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555a555a555555555aa5555a555555555555555555555555444445555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555a55555555a55555a5555555555555555555555555555544555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555aa55555aa5555555aa555555a5555555555555555555555555555554444555555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555a55555a555555555a555555a55555555555555555555555555555555554445555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555a555555555555555a5555555a55555555555555555555555555555555555544455555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555aa55555555555555aa555555a555555555555555555555555555555555555554444555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555a55555aa5555aa55a55555555a555555555555555555555555555555555555555554445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555aa555aaa5555aa55a555555555a555555555555555555555555555555555555555555445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555aa55aa555555aa555a55555555a5555555555555555555555555555555555555555555554555fffffffffffffff44ff5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555a55aa555555aa5555555555555a5555555555555555555555555555555555555555555555455fffffffffffffff4ff55ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555a55a555555555555555555a5555a5555555555555555555555555555555555555555555555545ffffffffffff444f55ffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55a55555555555555555a5555a555a55555555555555555555555555555555555555555555555554fffffffffff44f55ffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555aa555555a555aa55a5555555555555555555555555555555555555555555555555544fffffff444f55ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555a555555aa5555a555a555555555555555555555555555555555555555555555555555444444445555ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555a55a555555a55555a55555555555555555555555555555555555555555555555555555555ff5555555fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555aa55555555a55555a555555555555555555555555555555555555555555555555555555555ffffff444fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555aa555555555a555555a55555555555fffffffffffffff555555555555555555555555555555555555555f4444fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555aa5555555555555555a555555555555fffffffffffffff555555555555555555555555555555555555555ffff44ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555aa5555aa5555555555aa555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555a55555aa555aaa5555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55555aa555aa555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55aaa555aaa5555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555a55a5555aaa55555555a5555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555a55aa5555a555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555a55555a555a555a5555a5555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a555a555a55555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a5555555555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555aa555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a555555aa5555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555a555555a55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a5a5a5555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a55555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """),
            img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa5555aafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff444444444444444fffffffffffffffffffffffffffffffffffa5a55a5afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44fffffffffffff444fffffffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ffff5555555fffff444fffffffffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff555ffffff55555fff44fffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f555fffffffffffff5555f444ffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffff55ff444ffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffffff55ff44fffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffff55ff44ffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffffff55f4fffffffffffffffaaaaaaaa5a55a5aaaaaaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff5ffffffffffffffffffffff55f44fffffffffffff5a55a55555aa5555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ff5ffffffffffffffffffffffff5f444fffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44f55fffffffffffffffffffffff555f44ffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5f44fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffff5ff4fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5544ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffffff54ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff445fffffffffffffffffffffffffffff5555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff4f5fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffff44fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff4ffffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff4fffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff45ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5fffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffff5ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff5fffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff55ffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffff5555555555555555555555555555455555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555545555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff555555a55555a555555555555555554555555555555555555555555555a55a55555555555a55a55555555555555555555555555555555555a55a5a55a5555555fffffffffffffffff
                        fffffffffffffff5555555a555a5555555555555555555445555555555555555555555555555a55555555555a555555555555555555555555555555555555555a24a42a55555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555554555555555555555555555555555a55555555555a555555555555555555555555555555555555555242224255555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555555555445555555555555555555555555a55555555555a55555555555555555555555555555555555555a42a5a24a5555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555555554555555555555555555555555a55555555555a555555555555555555555555555555555555555a45154a55555555fffffffffffffffff
                        fffffffffffffff5555555555555555aa5555555555555555555445555555555555555555555a55555555555a55555555555555555555555555555555555555a42a5a24a5555555fffffffffffffffff
                        ffffffffffffffffffff555aaa555aaaaa555555555555555555544455555555555555555555a55555555555a555555555555555555555555555555555555555242224255fffffffffffffffffffffff
                        ffffffffffffffffffff55a555a555555aaaa555555555555555555445555555555555555555a55555555555a555555555555555555555555555555555555555a24a42a55fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555aaaa555555555555555544455555555555555555a55555555555a55555555555555555555555555555555555555a55a5a55a5fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555aaa5555555555555555445555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555aaa5555555555555544555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555aa55555555555554455555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555aaaaa5555555554445555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555555555aaa55555555444555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555555555aaaaa5555544445555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555aaa555554455555555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555aaaa55344455555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555aaa555445555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555aa55544555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555555aa5554455555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555555555555555555555555555555aa555444555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555555aaaaaaaaa5555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555a45555555555555555555555555555555555555555fffff455ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555544555555555555555555555555555555555555555ffffff4555ffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555554455555555555555555555555555555555555555fffffff4455fffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555544445555555555555555555555555555555555ffffffff4455ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555544455555555555555555555555555555555fffffffff4445fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555445555555555555555555555555555555ffffffffffff45ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555544555555555555555555555555555555fffffffffffff4ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555554555455555555555555555555555555fffffffffffff44fffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555555555aa5555aa5555555555555555554555455555555555555555ffffffffffffffffffffff44ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff5555555555555555aa5555aa55555555555555555555455555555555555555555fffffffffffffffffffffff44fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555555a55555aa555555555555555555555445455555555555555555ffffffffffffffffffffffff4fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555aaa55555a55555555555555555555555544545555555555555555ffffffffffffffffffffffff45ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555a5555555a555555555555555555555555554444555555555555555ffffffffffffffffffffffff44ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555aa5555555a55555555aa555555555555555555444555555555555555fffffffffffffffffffffffff45fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555a555aa555a55555a555a555555555555555555555444455455555555555555555fffffffffffffffff455ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555a555a555555555aa5555a555555555555555555555555444445555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555a55555555a55555a5555555555555555555555555555544555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555aa55555aa5555555aa555555a5555555555555555555555555555554444555555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555a55555a555555555a555555a55555555555555555555555555555555554445555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555a555555555555555a5555555a55555555555555555555555555555555555544455555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555aa55555555555555aa555555a555555555555555555555555555555555555554444555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555a55555aa5555aa55a55555555a555555555555555555555555555555555555555554445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555aa555aaa5555aa55a555555555a555555555555555555555555555555555555555555445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555aa55aa555555aa555a55555555a5555555555555555555555555555555555555555555554555fffffffffffffff44ff5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555a55aa555555aa5555555555555a5555555555555555555555555555555555555555555555455fffffffffffffff4ff55ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555a55a555555555555555555a5555a5555555555555555555555555555555555555555555555545ffffffffffff444f55ffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55a55555555555555555a5555a555a55555555555555555555555555555555555555555555555554fffffffffff44f55ffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555aa555555a555aa55a5555555555555555555555555555555555555555555555555544fffffff444f55ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555a555555aa5555a555a555555555555555555555555555555555555555555555555555444444445555ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555a55a555555a55555a55555555555555555555555555555555555555555555555555555555ff5555555fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555aa55555555a55555a555555555555555555555555555555555555555555555555555555555ffffff444fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555aa555555555a555555a55555555555fffffffffffffff555555555555555555555555555555555555555f4444fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555aa5555555555555555a555555555555fffffffffffffff555555555555555555555555555555555555555ffff44ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555aa5555aa5555555555aa555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555a55555aa555aaa5555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55555aa555aa555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55aaa555aaa5555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555a55a5555aaa55555555a5555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555a55aa5555a555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555a55555a555a555a5555a5555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a555a555a55555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a5555555555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555aa555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a555555aa5555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555a555555a55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a5a5a5555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a55555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """),
            img("""
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa5555aafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff444444444444444fffffffffffffffffffffffffffffffffffa5a55a5afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44fffffffffffff444fffffffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ffff5555555fffff444fffffffffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff555ffffff55555fff44fffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f555fffffffffffff5555f444ffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffff55ff444ffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4f55fffffffffffffffffff55ff44fffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffff55ff44ffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4ff5ffffffffffffffffffffff55f4fffffffffffffffaaaaaaaa5a55a5aaaaaaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff4fff5ffffffffffffffffffffff55f44fffffffffffff5a55a55555aa5555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffff44ff5ffffffffffffffffffffffff5f444fffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffff44f55fffffffffffffffffffffff555f44ffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5f44fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffff5ff4fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5544ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffffff54ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff445fffffffffffffffffffffffffffff5555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff4f5fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffff44fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff4ffffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff4fffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff45ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5fffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffff5ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff5fffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffff55ffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffff5555555555555555555555555555455555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555545555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff555555a55555a555555555555555554555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555a555a5555555555555555555445555555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555554555555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555555555555555555555445555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff55555555a5a55555555555555555555555554555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                        fffffffffffffff5555555555555555aa5555555555555555555445555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                        ffffffffffffffffffff555aaa555aaaaa555555555555555555544455555555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55a555a555555aaaa555555555555555555445555555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555aaaa555555555555555544455555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555aaa5555555555555555445555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555aaa5555555555555544555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555aa55555555555554455555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555aaaaa5555555554445555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555555555aaa55555555444555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555555555555555aaaaa5555544445555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555aaa555554455555555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555aaaa55344455555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555aaa555445555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555aa55544555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555555555555555555555555555aa5554455555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555555555555555555555555555555aa555444555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555555555555555555555555555555aaaaaaaaa5555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555a45555555555555555555555555555555555555555fffff455ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555544555555555555555555555555555555555555555ffffff4555ffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555554455555555555555555555555555555555555555fffffff4455fffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555544445555555555555555555555555555555555ffffffff4455ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555544455555555555555555555555555555555fffffffff4445fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555445555555555555555555555555555555ffffffffffff45ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555544555555555555555555555555555555fffffffffffff4ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555554555455555555555555555555555555fffffffffffff44fffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555555555aa5555aa5555555555555555554555455555555555555555ffffffffffffffffffffff44ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff5555555555555555aa5555aa55555555555555555555455555555555555555555fffffffffffffffffffffff44fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555555a55555aa555555555555555555555445455555555555555555ffffffffffffffffffffffff4fffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555555aaa55555a55555555555555555555555544545555555555555555ffffffffffffffffffffffff45ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff55555555555a5555555a555555555555555555555555554444555555555555555ffffffffffffffffffffffff44ffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffff555555555aa5555555a55555555aa555555555555555555444555555555555555fffffffffffffffffffffffff45fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555a555aa555a55555a555a555555555555555555555444455455555555555555555fffffffffffffffff455ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555555a555a555555555aa5555a555555555555555555555555444445555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555555555a55555555a55555a5555555555555555555555555555544555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555aa55555aa5555555aa555555a5555555555555555555555555555554444555555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555a55555a555555555a555555a55555555555555555555555555555555554445555555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555a555555555555555a5555555a55555555555555555555555555555555555544455555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555aa55555555555555aa555555a555555555555555555555555555555555555554444555555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555a55555aa5555aa55a55555555a555555555555555555555555555555555555555554445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555aa555aaa5555aa55a555555555a555555555555555555555555555555555555555555445555fffffffffffffffff4ff5fffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555aa55aa555555aa555a55555555a5555555555555555555555555555555555555555555554555fffffffffffffff44ff5ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555a55aa555555aa5555555555555a5555555555555555555555555555555555555555555555455fffffffffffffff4ff55ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555a55a555555555555555555a5555a5555555555555555555555555555555555555555555555545ffffffffffff444f55ffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55a55555555555555555a5555a555a55555555555555555555555555555555555555555555555554fffffffffff44f55ffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555555555aa555555a555aa55a5555555555555555555555555555555555555555555555555544fffffff444f55ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff55555555555a555555aa5555a555a555555555555555555555555555555555555555555555555555444444445555ffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff5555555a55a555555a55555a55555555555555555555555555555555555555555555555555555555ff5555555fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffff555555aa55555555a55555a555555555555555555555555555555555555555555555555555555555ffffff444fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555555aa555555555a555555a55555555555fffffffffffffff555555555555555555555555555555555555555f4444fffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555555aa5555555555555555a555555555555fffffffffffffff555555555555555555555555555555555555555ffff44ffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff5555555555aa5555aa5555555555aa555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff555555555a55555aa555aaa5555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55555aa555aa555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff55555555a55aaa555aaa5555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555a55a5555aaa55555555a5555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555a55aa5555a555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555a55555a555a555a5555a5555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a555a555a55555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a5555555555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff55555555555555555aa555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a555555aa5555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555a555555a55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555a5a5a5555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555a5a55555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff555555555555555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            """)],
        1000,
        False)
    time_chek = game.runtime() + 2000
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa5555aafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffff444444444444444fffffffffffffffffffffffffffffffffffa5a55a5afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffff44fffffffffffff444fffffffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff44ffff5555555fffff444fffffffffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4fff555ffffff55555fff44fffffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4f555fffffffffffff5555f444ffffffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4f55fffffffffffffffff55ff444ffffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4f55fffffffffffffffffff55ff44fffffffffffffffffffffffa555555afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4ff5ffffffffffffffffffff55ff44ffffffffffffffffffffffa55aa55afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4ff5ffffffffffffffffffffff55f4fffffffffffffffaaaaaaaa5a55a5aaaaaaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff4fff5ffffffffffffffffffffff55f44fffffffffffff5a55a55555aa5555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffff44ff5ffffffffffffffffffffffff5f444fffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffff44f55fffffffffffffffffffffff555f44ffffffffff5a55a55555555555a55a5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5f44fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffff5ff4fffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff4ff5ffffffffffffffffffffffffff5544ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff44f5ffffffffffffffffffffffffffff54ffff55555a55a55555555555a55a55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffff445fffffffffffffffffffffffffffff5555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffff4f5fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffff44fffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a5555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffff45ffffffffffffffffffffffffffff555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffff4ffffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffff4fffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffff45ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffff5555555555555a55a55555555555a55a55555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff5fffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffff5ffffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff5fffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff55ffffffffff555555555555555555555a55a55555555555a55a555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffff
                fffffffffffffff5555555555555555555555555555455555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff5555555555555555555555555555545555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff555555a55555a555555555555555554555555555555555555555555555a55a55555555555a55a555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff5555555a555a5555555555555555555445555555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff55555555a5a55555555555555555555554555555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff5555555555555555555555555555555555445555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff55555555a5a55555555555555555555555554555555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                fffffffffffffff5555555555555555aa5555555555555555555445555555555555555555555a55555555555a555555555555555555555555555555555555555555555555555555fffffffffffffffff
                ffffffffffffffffffff555aaa555aaaaa555555555555555555544455555555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff55a555a555555aaaa555555555555555555445555555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555aaaa555555555555555544455555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555aaa5555555555555555445555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555aaa5555555555555544555555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555555aa55555555555554455555555555555a55555555555a555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555555555555555555555555aaaaa5555555554445555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555555555555aaa55555555444555555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555555555555555555555555555555aaaaa5555544445555555555555555555555555555555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555555555555555555555aaa555554455555555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555555555555555555555555aaaa55344455555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555555555555555555555555555aaa555445555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff55555555555555555555555555555555555aa55544555555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555555555555555555555555555555aa5554455555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff5555555555555555555555555555555555555aa555444555555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff55555555555555555555555555555555555555aaaaaaaaa5555555555555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555a45555555555555555555555555555555555555555fffff455ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555544555555555555555555555555555555555555555ffffff4555ffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555554455555555555555555555555555555555555555fffffff4455fffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555544445555555555555555555555555555555555ffffffff4455ffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555544455555555555555555555555555555555fffffffff4445fffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555445555555555555555555555555555555ffffffffffff45ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555544555555555555555555555555555555fffffffffffff4ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555555555555555555555555555555555555554555455555555555555555555555555fffffffffffff44fffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff55555555555555555aa5555aa5555555555555555554555455555555555555555ffffffffffffffffffffff44ffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff5555555555555555aa5555aa55555555555555555555455555555555555555555fffffffffffffffffffffff44fffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff555555555555555a55555aa555555555555555555555445455555555555555555ffffffffffffffffffffffff4fffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff555555555555aaa55555a55555555555555555555555544545555555555555555ffffffffffffffffffffffff45ffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff55555555555a5555555a555555555555555555555555554444555555555555555ffffffffffffffffffffffff44ffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffff555555555aa5555555a55555555aa555555555555555555444555555555555555fffffffffffffffffffffffff45fffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555555555555a555aa555a55555a555a555555555555555555555444455455555555555555555fffffffffffffffff455ffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555555a555a555555555aa5555a555555555555555555555555444445555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555555555555555a55555555a55555a5555555555555555555555555555544555555555555555fffffffffffffffff4f5ffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555555aa55555aa5555555aa555555a5555555555555555555555555555554444555555555555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555555a55555a555555555a555555a55555555555555555555555555555555554445555555555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555a555555555555555a5555555a55555555555555555555555555555555555544455555555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff5555555aa55555555555555aa555555a555555555555555555555555555555555555554444555555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555a55555aa5555aa55a55555555a555555555555555555555555555555555555555554445555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555aa555aaa5555aa55a555555555a555555555555555555555555555555555555555555445555fffffffffffffffff4ff5fffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff5555aa55aa555555aa555a55555555a5555555555555555555555555555555555555555555554555fffffffffffffff44ff5ffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff5555a55aa555555aa5555555555555a5555555555555555555555555555555555555555555555455fffffffffffffff4ff55ffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555a55a555555555555555555a5555a5555555555555555555555555555555555555555555555545ffffffffffff444f55ffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55a55555555555555555a5555a555a55555555555555555555555555555555555555555555555554fffffffffff44f55ffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555555555aa555555a555aa55a5555555555555555555555555555555555555555555555555544fffffff444f55ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff55555555555a555555aa5555a555a555555555555555555555555555555555555555555555555555444444445555ffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff5555555a55a555555a55555a55555555555555555555555555555555555555555555555555555555ff5555555fffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff555555aa55555555a55555a555555555555555555555555555555555555555555555555555555555ffffff444fffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555555aa555555555a555555a55555555555fffffffffffffff555555555555555555555555555555555555555f4444fffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff55555555555aa5555555555555555a555555555555fffffffffffffff555555555555555555555555555555555555555ffff44ffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff5555555555aa5555aa5555555555aa555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff555555555a55555aa555aaa5555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff55555555a55555aa555aa555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffff55555555a55aaa555aaa5555555a55555555555555fffffffffffffff555555555555555555555555555555555555555ffffffffffffffffffffffffffffffffff
                ffffffffffffffffffff55555555555555555a55a5555aaa55555555a5555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555a55aa5555a555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff55555a55555a555a555a5555a5555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555a555a555a55555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555a5a5555555555555a55555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff55555555555555555aa555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555a5a555555aa5555a555555555555555555555fffffffffffffffffffffffffffff55555555555555555555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555555555555a555555a55fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555a5a5a5555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555a5a55555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff555555555555555555555a555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffff5555555555555555555555555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff555555555555555555555555555fffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    controller.move_sprite(mySprite, 100, 100)
    level = 3
def ran_out_of_names():
    global mySprite, level
    scene.set_background_image(assets.image("""
        kirbo home corrrupted
    """))
    mySprite = sprites.create(assets.image("""
        kirby star
    """), SpriteKind.player)
    mySprite.set_position(115, 30)
    sprites.destroy_all_sprites_of_kind(SpriteKind.food)
    game.show_long_text("kirbo is shocked his home is being colonized",
        DialogLayout.BOTTOM)
    info.set_life(3)
    info.set_score(0)
    game.show_long_text("kirbo has to get to the bottom of this",
        DialogLayout.BOTTOM)
    controller.move_sprite(mySprite)
    level = 1

def on_on_overlap2(sprite2, otherSprite2):
    global Activate, timeCheck
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    animation.run_image_animation(otherSprite2,
        assets.animation("""
            kirbo get on star
        """),
        100,
        False)
    pause(3000)
    scene.set_background_image(assets.image("""
        no asset name
    """))
    otherSprite2.set_position(13, 14)
    Activate = game.runtime() + 7500
    timeCheck = True
    animation.run_image_animation(otherSprite2,
        assets.animation("""
            kirbo leaf
        """),
        500,
        False)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_score():
    global score, star
    if info.score() > 5:
        score = False
    elif info.score() == 5:
        score = True
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    if score == True:
        music.ba_ding.play()
        star = sprites.create(assets.image("""
            star
        """), SpriteKind.food)
        star.set_position(69, 54)
info.on_score(5, on_on_score)

def on_on_overlap3(sprite3, otherSprite3):
    if suck:
        otherSprite3.set_position(randint(0, 160), randint(0, 120))
        info.change_score_by(1)
        StopSucking()
    else:
        otherSprite3.set_position(randint(0, 160), randint(0, 120))
        info.change_life_by(-1)
        scene.set_background_image(assets.image("""
            b
        """))
        pause(100)
        scene.set_background_image(assets.image("""
            bruh
        """))
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

star: Sprite = None
score = False
Activate = 0
Boss2Mines = 0
boss2TimeCheck = 0
projectile: Sprite = None
savestar1 = False
time_chek = 0
animation2: Sprite = None
boss1 = False
projectileX: Sprite = None
ProjectileDelay = 0
projectileTimeCheck = 0
suck = False
level = 0
timeCheck = False
myEnemy: Sprite = None
mySprite: Sprite = None
effects.confetti.start_screen_effect(2000)
pause(2000)
game.show_long_text("wow you actually want to play my game? Well i did my best. Enjoy!",
    DialogLayout.CENTER)
game.show_long_text("well. i prepared a story for it too", DialogLayout.CENTER)
scene.set_background_image(assets.image("""
    n
"""))
mySprite = sprites.create(assets.image("""
    kirby
"""), SpriteKind.player)
game.show_long_text("Kirbo wakes up in a desert. He has amnesia",
    DialogLayout.BOTTOM)
controller.move_sprite(mySprite, 100, 100)
info.set_life(3)
myEnemy = sprites.create(assets.image("""
    mario enemy
"""), SpriteKind.enemy)
myEnemy.follow(mySprite, 50)
myEnemy.set_position(randint(0, 160), randint(0, 120))
mySprite.set_stay_in_screen(True)
myEnemy.set_stay_in_screen(True)
timeCheck = False
level = 0
# Boss 2 add second set of mines
# 

def on_on_update():
    global Boss2Mines, projectile, boss2TimeCheck
    if Boss2Mines == 1 and boss2TimeCheck < game.runtime():
        Boss2Mines = 2
        for index3 in range(15):
            projectile = sprites.create_projectile_from_side(assets.image("""
                    dna projectile
                """),
                randint(-160, -100),
                0)
            projectile.set_position(160, randint(0, 120))
        boss2TimeCheck = game.runtime() + 5000
    elif Boss2Mines == 2 and boss2TimeCheck < game.runtime():
        Boss2Mines = 3
        for index4 in range(15):
            projectile = sprites.create_projectile_from_side(assets.image("""
                    dna projectile
                """),
                0,
                randint(100, 160))
            projectile.set_position(randint(0, 160), 0)
        boss2TimeCheck = game.runtime() + 5000
    elif Boss2Mines == 3 and boss2TimeCheck < game.runtime():
        Boss2Mines = 0
        end_of_boss_2()
game.on_update(on_on_update)

def on_on_update2():
    global timeCheck
    if timeCheck and Activate < game.runtime():
        timeCheck = False
        ran_out_of_names()
game.on_update(on_on_update2)

def on_on_update3():
    global boss1
    if info.countdown() < 1:
        if boss1:
            boss1 = False
            info.stop_countdown()
            end_of_boss_1()
game.on_update(on_on_update3)

def on_on_update4():
    global savestar1, mySprite
    if savestar1:
        if time_chek < game.runtime():
            savestar1 = False
            animation2.destroy()
            scene.set_background_image(assets.image("""
                ur mom
            """))
            mySprite = sprites.create(assets.image("""
                kirby
            """), SpriteKind.player)
game.on_update(on_on_update4)

def on_forever():
    if suck:
        myEnemy.follow(mySprite, 5)
    else:
        myEnemy.follow(mySprite, 50)
forever(on_forever)
