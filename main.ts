namespace SpriteKind {
    export const NPC = SpriteKind.create()
    export const boss = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby back`)
})
function durimg_suck () {
    controller.moveSprite(mySprite, 0, 0)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    durimg_suck()
    animation.runImageAnimation(
    mySprite,
    assets.animation`kirby succ`,
    500,
    false
    )
    suck = true
})
function end_of_boss_1 () {
    level = 2
    info.changeScoreBy(10)
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
    info.setLife(3)
    save_star_part_1()
}
function boss_1 () {
    pause(2000)
    for (let index = 0; index < 25; index++) {
        projectileX = sprites.create(assets.image`spoike boi`, SpriteKind.Projectile)
        projectileX.setPosition(randint(0, 160), randint(0, 120))
        projectileX.follow(mySprite, 1)
    }
    info.startCountdown(11)
    boss1 = true
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setStayInScreen(true)
    if (mySprite.x > 104 && mySprite.x < 132 && (mySprite.y > 103 && mySprite.y < 117) && level == 1) {
        scene.setBackgroundImage(assets.image`unobrow`)
        boss_1()
    } else if (mySprite.x > 127 && mySprite.x < 137 && (mySprite.y > 42 && mySprite.y < 51) && level == 2) {
        scene.setBackgroundImage(assets.image`somewhat anger`)
        boss_2()
    } else if (mySprite.x < 26 && mySprite.x > 18 && (mySprite.y > 104 && mySprite.y < 113) && level == 3) {
        boss3 = sprites.create(assets.image`misthief`, SpriteKind.boss)
        boss3.setPosition(80, 60)
        scene.setBackgroundImage(assets.image`misthief`)
        boss_3()
    }
})
function StopSucking () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`kirby`)
    myEnemy.follow(mySprite, 5)
    suck = false
}
function save_star_part_1 () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    scene.setBackgroundImage(assets.image`blank immage`)
    animation2 = sprites.create(assets.image`kirbo home`, SpriteKind.Player)
    animation2.setPosition(75, 60)
    animation.runImageAnimation(
    animation2,
    assets.animation`get sploded`,
    500,
    false
    )
    time_chek = game.runtime() + 9000
    savestar1 = true
    controller.moveSprite(mySprite, 100, 100)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby left`)
})
function boss_2 () {
    round = 1
    if (round == 1) {
        for (let index = 0; index < 10; index++) {
            projectile = sprites.createProjectileFromSide(assets.image`dna projectile`, randint(100, 120), 0)
            projectile.setPosition(0, randint(0, 120))
        }
        pause(2000)
        round += 1
    }
    if (round == 2) {
        for (let index = 0; index < 10; index++) {
            projectile = sprites.createProjectileFromSide(assets.image`dna projectile`, randint(-100, -160), 0)
            projectile.setPosition(160, randint(0, 120))
        }
        pause(2000)
        round += 1
    }
    if (round == 3) {
        for (let index = 0; index < 10; index++) {
            projectile = sprites.createProjectileFromSide(assets.image`dna projectile`, 0, randint(100, 160))
            projectile.setPosition(randint(0, 160), 0)
        }
    }
    pause(5000)
    end_of_boss_2()
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby right`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    if (projectileTimeCheck < game.runtime()) {
        projectileTimeCheck = game.runtime() + ProjectileDelay
        info.changeLifeBy(-1)
    }
})
function set_kirbo () {
    mySprite2 = sprites.create(assets.image`kirby`, SpriteKind.Player)
    controller.moveSprite(mySprite, 100, 100)
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby`)
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    controller.moveSprite(mySprite, 100, 100)
    StopSucking()
})
function end_of_boss_2 () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    scene.setBackgroundImage(assets.image`blank immage`)
    animation2 = sprites.create(assets.image`e`, SpriteKind.Player)
    animation2.setPosition(75, 60)
    animation.runImageAnimation(
    animation2,
    assets.animation`oh no get sploded`,
    500,
    false
    )
    time_chek = game.runtime() + 2000
    level = 3
    level3Check = true
    scene.setBackgroundImage(assets.image`true anger`)
}
function ran_out_of_names () {
    scene.setBackgroundImage(assets.image`kirbo home corrrupted`)
    mySprite = sprites.create(assets.image`kirby star`, SpriteKind.Player)
    mySprite.setPosition(115, 30)
    sprites.destroyAllSpritesOfKind(SpriteKind.Food)
    game.showLongText("kirbo is shocked his home is being colonized", DialogLayout.Bottom)
    info.setLife(3)
    info.setScore(0)
    game.showLongText("kirbo has to get to the bottom of this", DialogLayout.Bottom)
    controller.moveSprite(mySprite)
    level = 1
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    animation.runImageAnimation(
    otherSprite,
    assets.animation`kirbo get on star`,
    100,
    false
    )
    pause(3000)
    scene.setBackgroundImage(assets.image`kirbo home`)
    otherSprite.setPosition(13, 14)
    Activate = game.runtime() + 7500
    timeCheck = true
    animation.runImageAnimation(
    otherSprite,
    assets.animation`kirbo leaf`,
    500,
    false
    )
})
function boss_3 () {
    animation.runImageAnimation(
    boss3,
    assets.animation`he screm`,
    500,
    false
    )
    time_chek = game.runtime() + 1500
    scene.setBackgroundImage(assets.image`say AHHHHH`)
    boss3Mouth = sprites.create(img`
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        ................................................................................
        `, SpriteKind.Player)
    boss3Mouth.setPosition(69, 37)
}
info.onScore(5, function () {
    if (info.score() > 5) {
        score = false
    } else if (info.score() == 5) {
        score = true
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    }
    if (score == true) {
        music.baDing.play()
        star = sprites.create(assets.image`star`, SpriteKind.Food)
        star.setPosition(69, 54)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (suck) {
        otherSprite.setPosition(randint(0, 160), randint(0, 120))
        info.changeScoreBy(1)
        StopSucking()
    } else {
        otherSprite.setPosition(randint(0, 160), randint(0, 120))
        info.changeLifeBy(-1)
        scene.setBackgroundImage(assets.image`b`)
        pause(100)
        scene.setBackgroundImage(assets.image`bruh`)
    }
})
let projectile2: Sprite = null
let LaunchTheProjectiles = false
let star: Sprite = null
let score = false
let boss3Mouth: Sprite = null
let Activate = 0
let level3Check = false
let mySprite2: Sprite = null
let projectile: Sprite = null
let round = 0
let savestar1 = false
let time_chek = 0
let animation2: Sprite = null
let boss3: Sprite = null
let boss1 = false
let projectileX: Sprite = null
let suck = false
let ProjectileDelay = 0
let projectileTimeCheck = 0
let level = 0
let timeCheck = false
let myEnemy: Sprite = null
let mySprite: Sprite = null
effects.confetti.startScreenEffect(2000)
pause(2000)
game.showLongText("wow you actually want to play my game? Well i did my best. Enjoy!", DialogLayout.Center)
game.showLongText("well. i prepared a story for it too", DialogLayout.Center)
scene.setBackgroundImage(assets.image`n`)
mySprite = sprites.create(assets.image`kirby`, SpriteKind.Player)
game.showLongText("Kirbo wakes up in a desert. He has amnesia", DialogLayout.Bottom)
controller.moveSprite(mySprite, 100, 100)
info.setLife(3)
myEnemy = sprites.create(assets.image`mario enemy`, SpriteKind.Enemy)
myEnemy.follow(mySprite, 50)
myEnemy.setPosition(randint(0, 160), randint(0, 120))
mySprite.setStayInScreen(true)
myEnemy.setStayInScreen(true)
timeCheck = false
level = 0
projectileTimeCheck = 0
ProjectileDelay = 500
sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
sprites.destroyAllSpritesOfKind(SpriteKind.Player)
ran_out_of_names()
game.onUpdate(function () {
    if (timeCheck && Activate < game.runtime()) {
        timeCheck = false
        ran_out_of_names()
    }
})
game.onUpdate(function () {
    if (info.countdown() < 1) {
        if (boss1) {
            boss1 = false
            info.stopCountdown()
            end_of_boss_1()
        }
    }
})
game.onUpdate(function () {
    if (savestar1) {
        if (time_chek < game.runtime()) {
            savestar1 = false
            animation2.destroy()
            scene.setBackgroundImage(assets.image`no asset name`)
            mySprite = sprites.create(assets.image`kirby`, SpriteKind.Player)
        }
    }
})
game.onUpdate(function () {
    if (time_chek < game.runtime()) {
        LaunchTheProjectiles = true
    }
})
game.onUpdate(function () {
    if (level3Check && time_chek < game.runtime()) {
        level3Check = false
        mySprite = sprites.create(assets.image`kirby`, SpriteKind.Player)
        controller.moveSprite(mySprite)
    }
})
forever(function () {
    if (suck) {
        myEnemy.follow(mySprite, 5)
    } else {
        myEnemy.follow(mySprite, 50)
    }
})
game.onUpdateInterval(500, function () {
    if (LaunchTheProjectiles) {
        projectile2 = sprites.createProjectileFromSprite(img`
            . . . . . . b b b b a a . . . . 
            . . . . b b d d d 3 3 3 a a . . 
            . . . b d d d 3 3 3 3 3 3 a a . 
            . . b d d 3 3 3 3 3 3 3 3 3 a . 
            . b 3 d 3 3 3 3 3 b 3 3 3 3 a b 
            . b 3 3 3 3 3 a a 3 3 3 3 3 a b 
            b 3 3 3 3 3 a a 3 3 3 3 d a 4 b 
            b 3 3 3 3 b a 3 3 3 3 3 d a 4 b 
            b 3 3 3 3 3 3 3 3 3 3 d a 4 4 e 
            a 3 3 3 3 3 3 3 3 3 d a 4 4 4 e 
            a 3 3 3 3 3 3 3 d d a 4 4 4 e . 
            a a 3 3 3 d d d a a 4 4 4 e e . 
            . e a a a a a a 4 4 4 4 e e . . 
            . . e e b b 4 4 4 4 b e e . . . 
            . . . e e e e e e e e . . . . . 
            . . . . . . . . . . . . . . . . 
            `, boss3Mouth, 50, 50)
    }
})
