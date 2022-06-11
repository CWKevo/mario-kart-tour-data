from data.models import *



POWERUPS = {
    "COIN": Powerup(name='Coin', description='Slightly increases a racers speed in races.'),
    "BANANA": Powerup(name='Banana', description='This item will cause any karts that come in contact with it to spin out.'),
    "TRIPLE_BANANA": Powerup(name='Triple Banana', description='Causes any karts that touch it to spin out.', special=True, plus_description='Adds one more banana to the banana stack.'),
    "GIANT_BANANA": Powerup(name='Giant Banana', description='A grumpy banana that is triple size of a normal banana. Running into it will cause it to multiply into smaller bananas.', special=True, plus_description='One more banana drops from the giant banana on car impact.'),
    "BUBBLE": Powerup(name='Bubble', description='You float in an useless bubble that is supposed to protect you from hazards.', special=True, plus_description='The bubble lasts longer, I guess...'),
    "BOOMERANG_FLOWER": Powerup(name='Boomerang Flower', description='Whirls around and around your kart to strike nearby opponents.', special=True, plus_description='Adds another boomerang, allowing you to throw two total!'),
    "FIRE_FLOWER": Powerup(name='Fire Flower', description='A happy flower that spits 3 fireballs in your face... Sometimes 4!', special=True, plus_description='One more fireball comes from the fire flower.'),
}


DRIVERS = {
    "BABY_MARIO": Driver(name='Baby Mario', rarity=Rarity.COMMON, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "MARIO": Driver(name='Mario', rarity=Rarity.SUPER, special_powerup=POWERUPS['FIRE_FLOWER']),
}

TRACKS = {
    "MARIO_CIRCUIT_1": Track(name='Mario Circuit 1', two_item_slot_drivers=[], three_item_slot_drivers=[]),
    "T_MARIO_CIRCUIT_1": Track(name='Mario Circuit 1T', two_item_slot_drivers=[DRIVERS['MARIO']], three_item_slot_drivers=[DRIVERS['BABY_MARIO']]),
    "WALUIGI_PINBALL": Track(name='Waluigi Pinball', two_item_slot_drivers=[], three_item_slot_drivers=[DRIVERS['BABY_MARIO']]),
    "RT_VANILLA_LAKE_1": Track(name='Vanilla Lake 1R/T', two_item_slot_drivers=[], three_item_slot_drivers=[DRIVERS['BABY_MARIO'].lvl(6)]),
}

CUPS = {
    "TEST_CUP": Cup(name='Test Cup', courses=(
        Course(track=TRACKS['MARIO_CIRCUIT_1'], favored_driver=DRIVERS['MARIO']),
        Course(track=TRACKS['RT_VANILLA_LAKE_1'], favored_driver=DRIVERS['BABY_MARIO']),
        Course(track=TRACKS['WALUIGI_PINBALL'], favored_driver=DRIVERS['BABY_MARIO']),
        Course(track=TRACKS['T_MARIO_CIRCUIT_1'], favored_driver=DRIVERS['MARIO'], is_bonus=True)
    ), favored_driver=DRIVERS['MARIO']),
}
