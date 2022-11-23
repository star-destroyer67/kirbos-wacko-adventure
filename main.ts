namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby back`)
})
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
function StopSucking () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`kirby`)
    myEnemy.follow(mySprite, 5)
    suck = false
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby left`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby right`)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`kirby`)
})
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    controller.moveSprite(mySprite, 100, 100)
    StopSucking()
})
function durimg_suck () {
    controller.moveSprite(mySprite, 0, 0)
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
    scene.setBackgroundImage(assets.image`no asset name`)
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
function ran_out_of_names () {
    scene.setBackgroundImage(assets.image`kirbo home corrrupted`)
    mySprite = sprites.create(assets.image`kirby star`, SpriteKind.Player)
    mySprite.setPosition(115, 30)
    sprites.destroyAllSpritesOfKind(SpriteKind.Food)
    game.showLongText("kirbo is shocked his home is being colonized", DialogLayout.Bottom)
    info.setLife(3)
    info.setScore(0)
    game.showLongText("kirbo has to get to the bottom of this", DialogLayout.Bottom)
}
info.onScore(5, function () {
    star = sprites.create(assets.image`star`, SpriteKind.Food)
    star.setPosition(69, 54)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (suck) {
        otherSprite.setPosition(0, 0)
        info.changeScoreBy(1)
        StopSucking()
    } else {
        otherSprite.setPosition(0, 0)
        info.changeLifeBy(-1)
        scene.setBackgroundImage(assets.image`b`)
        pause(100)
        scene.setBackgroundImage(assets.image`bruh`)
    }
})
let star: Sprite = null
let Activate = 0
let suck = false
let timeCheck = false
let myEnemy: Sprite = null
let mySprite: Sprite = null
effects.confetti.startScreenEffect(2000)
pause(2000)
game.showLongText("wow you actually want to play my game? Well i did my best. Enjoy!", DialogLayout.Center)
game.showLongText("well. i prepared a story for it too", DialogLayout.Center)
scene.setBackgroundImage(assets.image`n`)
mySprite = sprites.create(assets.image`kirby`, SpriteKind.Player)
game.showLongText("kirbo wakes up in a desert without knowing how, he has amnesia", DialogLayout.Bottom)
controller.moveSprite(mySprite, 100, 100)
info.setLife(3)
myEnemy = sprites.create(assets.image`mario enemy`, SpriteKind.Enemy)
myEnemy.follow(mySprite, 50)
myEnemy.setPosition(0, 0)
mySprite.setStayInScreen(true)
myEnemy.setStayInScreen(true)
timeCheck = false
game.onUpdate(function () {
    if (timeCheck && Activate < game.runtime()) {
        timeCheck = false
        ran_out_of_names()
    }
})
forever(function () {
    if (suck) {
        myEnemy.follow(mySprite, 5)
    } else {
        myEnemy.follow(mySprite, 50)
    }
})
