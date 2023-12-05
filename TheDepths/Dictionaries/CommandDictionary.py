#imports player class
from Class.LivingClass.PlayerClass import Player

#command keyword and callibg function
Commands = {
    'help': Player.help,
    'stats': Player.stats,
    'explore': Player.explore,
    'fight': Player.fight,
    'suicide': Player.kill,
    'use': Player.use
}