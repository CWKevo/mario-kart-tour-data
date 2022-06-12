from data.models import *



POWERUPS = {
    "COIN": Powerup(name='Coin', description="This gives you two Coins. It's used automatically once you pick it up."),
    "BANANA": Powerup(name='Banana', description="Don't let this one give you the slip! Your kart will spin out if you hit one. You can carry one behind your kart to protect yourself from a single attack."),
    "TRIPLE_BANANA": Powerup(name='Triple Banana', description="Three bananas revolve around your kart. Tap the screen to throw them all at once and they'll land all lined up in a nice, tidy row!", special=True, plus_description='Increases your chances of getting Triple Bananas. Plus, the bananas revolve faster!'),
    "GIANT_BANANA": Powerup(name='Giant Banana', description="Not only does this big banana spin out karts that hit it, but after being struck it breaks into three regular-sized Bananas. The only banana split you'll be sad to see!", special=True, plus_description='Boosts your chances to get a Giant Banana. And when you do, it splits into even more bananas!'),
    "GREEN_SHELL": Powerup(name='Green Shell', description='Flies straight and crashes any kart it hits. Keep it behind your kart to protect yourself from a single attack.'),
    "TRIPLE_GREEN_SHELLS": Powerup(name='Triple Green Shells', description="Three Green Shells revolve around your kart. Tap the screen to throw all of them at once and they'll fly in a straight line.", special=True, plus_description='Increases your chances of getting Triple Green Shells. The shells will revolve faster.'),
    "RED_SHELL": Powerup(name='Red Shell', description='Homes in on a kart in front of you and crashes whatever it hits. Keep it behind your kart to protect yourself from a single attack.'),
    "SPINY_SHELL": Powerup(name='Spiny Shell', description='Chases down the kart in 1st place, crashing through anyone it hits before reaching its target. This will make you regret being in 1st place! Or even near the kart in 1st place...'),
    "BOWSER_SHELL": Powerup(name="Bowser's Shell", description="This big ol' shell on loan from Bowser will crash any karts it hits and keep on going. It can only be thrown forward.", special=True, plus_description="Bowser's Shell is bigger and a little better at tracking opponents."),
    "BOBOMB": Powerup(name='Bob-omb', description='This will walk towards opponents who get too close, and then explode when it touches a kart or when some time has passed. Karts caught in its blast will crash.'),
    "DOUBLE_BOBOMBS": Powerup(name='Double Bob-ombs', description='Two Bob-ombs will revolve around your kart. Tap the screen to throw them both at once. Two is better than one, right?', special=True, plus_description='Adds a Bob-omb so you can attack with 3 Bob-ombs.'),
    "MUSHROOM": Powerup(name='Mushroom', description="This classic item gives your kart a speed boost. Doesn't get much simpler than that!"),
    "TRIPLE_MUSHROOMS": Powerup(name='Triple Mushrooms', description='Why use just one Mushroom when you can use three? Tap the screen to use them all at once for a longer-lasting speed boost.', special=True, plus_description='Increases your chances of getting Triple Mushrooms and extends the dash time by a little.'),
    "MEGA_MUSHROOM": Powerup(name='Mega Mushroom', description="Increases your kart's size, allowing you to crash any opponents you hit. You'll return to regular size after some time or when you're hit by an item."),
    "BULLET_BILL": Powerup(name='Bullet Bill', description="Transforms you into a Bullet Bill for a set amount of time. You'll dash forward with all the power of a Bullet Bill and crash any opponents that you hit."),
    "BLOOPER": Powerup(name='Blooper', description='Squirts ink onto the karts in a higher position than yours, blinding the other drivers for a set amount of time. You can wipe the ink off by swiping the screen.'),
    "LIGHTNING": Powerup(name='Lightning', description='Calls down lightning to spin out your opponents and destroy the items they hold. Those struck will be smaller and slower for a set amount of time.'),
    "FIRE_FLOWER": Powerup(name='Fire Flower', description="Three fireballs will revolve around your kart. Tap the screen to throw them all at once, spinning out any kart they hit. You're really burning up the track now!", special=True, plus_description='Adds another fireball, allowing you to throw four total.'),
    "ICE_FLOWER": Powerup(name='Ice Flower', description="Three balls of ice will revolve around your kart. Tap the screen to throw them all at once and they'll freeze any kart they hit, causing them to slide.", special=True, plus_description='Adds another iceball, allowing you to throw four total!'),
    "BOOMERANG_FLOWER": Powerup(name='Boomerang Flower', description='Tap the screen to throw a boomerang. Not only will it spin out any karts it hits, but it will collect any surrounding Coins for you, too.', special=True, plus_description='Adds another boomerang, allowing you to throw two total!'),
    "SUPER_HORN": Powerup(name='Super Horn', description='The loudness of this horn will blow away any surrounding items and karts. It can repel Bloopers, and even Spiny Shells!'),
    "HEART": Powerup(name='Heart', description='This protective Heart revolves around your kart for a set amount of time, shielding you from attacks. It will vanish upon taking damage. You can stack up to five at once.', special=True, plus_description='You get 1 additional Heart! The additional Heart runs out quickly so make it count!'),
    "YOSHI_EGG": Powerup(name="Yoshi's Egg", description="Homes in on the kart in front of you and crashes once it hits. Three more items will fly out when it breaks. It's the item that keeps on giving!", special=True, plus_description="Yoshi's Egg is bigger and it releases an additional item."),
    "BIRDO_EGG": Powerup(name="Birdo's Egg", description="Homes in on the kart in front of you and crashes once it hits. Three more items will fly out when it breaks. It's the item that keeps on giving!", special=True, plus_description="Birdo's Egg is bigger and it releases an additional item."),
    "BUBBLE": Powerup(name='Bubble', description='Briefly envelops your kart and protects you from damage for a set time. While in the bubble, you will get a speed boost and float in the air. Watch out, because it will vanish upon taking damage!', special=True, plus_description="Increases the Bubble's movement speed."),
    "BANANA_BARRELS": Powerup(name='Banana Barrels', description='Arm your kart with two fully-loaded barrels of Bananas! Continually shoots out Bananas in front of your kart for a set time.', special=True, plus_description='The barrels will sometimes fire Giant Bananas.'),
    "MUSHROOM_CANNON": Powerup(name='Mushroom Cannon', description='A cannon designed to resemble a Mushroom. Continually shoots out Mushrooms in front of your kart for a set time.', special=True, plus_description="Fires a larger payload of Mushrooms in three directions."),
    "LUCKY_SEVEN": Powerup(name='Lucky Seven', description='Seven items (Red Shell, Banana, Green Shell, Bob-omb, Super Horn, Mushroom, and Blooper) revolve around your kart. Tap the screen to use all seven items at once.', special=True, plus_description='3 coins are added to the items that appear.'),
    "COIN_BOX": Powerup(name='Coin Box', description='A box with a golden sheen. Generates a large amount of Coins in front of your kart for a set time.', special=True, plus_description='This will sometimes spit out red coins.'),
    "DASH_RING": Powerup(name='Dash Ring', description='Tosses out three rings in front of you along the track. Pass through them for a speed boost!', special=True, plus_description='Gives you two more rings for five total, increasing your total boost potential.'),
    "BOBOMB_CANNON": Powerup(name='Bob-omb Cannon', description='A dangerous cannon fueled by red-hot coals! Continually shoots out Bob-ombs in front of your kart for a set time.', special=True, plus_description='Adds another Bob-omb Cannon, allowing you to fire even more Bob-ombs.'),
    "SUPER_STAR": Powerup(name='Super Star', description='Turns you invincible for a time. Your kart will be faster and any karts you hit will crash.'),
    "HAMMER": Powerup(name='Hammer', description='Throws multiple Hammers in an arc aimed at karts in front of yours.', special=True, plus_description="You'll get two extra hammers to throw, widening the strike zone."),
    "GIGA_BOBOMB": Powerup(name='Giga Bob-omb', description='This giga-sized Bob-omb can only be thrown forward. after being thrown, it will explode after hitting a kart or bouncing 3 times. It has a larger blast radius than a standard Bob-omb.', special=True, plus_description='Giga Bob-omb is bigger and its blast radius is a bit wider!'),
    "SUPER_BELL": Powerup(name='Super Bell', description='A bell rings above the driver, knocking away nearby karts and items. The bell rings three consecutive times.', special=True, plus_description='As if 3 rings were not enough, the developers were like "Ah, okay, let\'s-a-go!" and throwed in an additional 4th ring that is rumored to be capable of destroying your sanity completely if you get struck by it... If you get it, congratulations! You are an Ascended® Being™ in the Mario Kart: Tour™ (mobile game for Android/iOS).'),
    "CAPSULE": Powerup(name='Capsule', description='Three colorful capsules bounce at opponents when thrown.', special=True, plus_description='Adds another capsule and increases their size.'),
}


DRIVERS = {
    # Common:
    "BABY_MARIO": Driver(name='Baby Mario', rarity=Rarity.COMMON, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "BABY_PEACH": Driver(name='Baby Peach', rarity=Rarity.COMMON, special_powerup=POWERUPS['BUBBLE']),
    "BABY_DAISY": Driver(name='Baby Daisy', rarity=Rarity.COMMON, special_powerup=POWERUPS['BUBBLE']),
    "BABY_ROSALINA": Driver(name='Baby Rosalina', rarity=Rarity.COMMON, special_powerup=POWERUPS['BUBBLE']),
    "BABY_LUIGI": Driver(name='Baby Luigi', rarity=Rarity.COMMON, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "KOOPA_TROOPA": Driver(name='Koopa Troopa', rarity=Rarity.COMMON, special_powerup=POWERUPS['TRIPLE_GREEN_SHELLS']),
    "SHY_GUY": Driver(name='Shy Guy', rarity=Rarity.COMMON, special_powerup=POWERUPS['DOUBLE_BOBOMBS']),
    "DRY_BONES": Driver(name='Dry Bones', rarity=Rarity.COMMON, special_powerup=POWERUPS['TRIPLE_GREEN_SHELLS']),
    "IGGY": Driver(name='Iggy', rarity=Rarity.COMMON, special_powerup=POWERUPS['TRIPLE_GREEN_SHELLS']),
    "LARRY": Driver(name='Larry', rarity=Rarity.COMMON, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "LEMMY": Driver(name='Lemmy', rarity=Rarity.COMMON, special_powerup=POWERUPS['BUBBLE']),
    "LUDWIG": Driver(name='Ludwig', rarity=Rarity.COMMON, special_powerup=POWERUPS['DASH_RING']),
    "MORTON": Driver(name='Morton', rarity=Rarity.COMMON, special_powerup=POWERUPS['GIANT_BANANA']),
    "ROY": Driver(name='Roy', rarity=Rarity.COMMON, special_powerup=POWERUPS['DOUBLE_BOBOMBS']),
    "WENDY": Driver(name='Wendy', rarity=Rarity.COMMON, special_powerup=POWERUPS['HEART']),

    # Super:
    "MARIO": Driver(name='Mario', rarity=Rarity.SUPER, special_powerup=POWERUPS['FIRE_FLOWER']),
    "PEACH": Driver(name='Peach', rarity=Rarity.SUPER, special_powerup=POWERUPS['HEART']),
    "YOSHI": Driver(name='Yoshi', rarity=Rarity.SUPER, special_powerup=POWERUPS['YOSHI_EGG']),
    "DAISY": Driver(name='Daisy', rarity=Rarity.SUPER, special_powerup=POWERUPS['HEART']),
    "TOAD": Driver(name='Toad', rarity=Rarity.SUPER, special_powerup=POWERUPS['TRIPLE_MUSHROOMS']),
    "TOADETTE": Driver(name='Toadette', rarity=Rarity.SUPER, special_powerup=POWERUPS['TRIPLE_MUSHROOMS']),
    "ROSALINA": Driver(name='Rosalina', rarity=Rarity.SUPER, special_powerup=POWERUPS['DASH_RING']),
    "LUIGI": Driver(name='Luigi', rarity=Rarity.SUPER, special_powerup=POWERUPS['FIRE_FLOWER']),
    "PIT_CREW_TOAD": Driver(name='Toad (Pit Crew)', rarity=Rarity.SUPER, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "RED_YOSHI": Driver(name='Red Yoshi', rarity=Rarity.SUPER, special_powerup=POWERUPS['YOSHI_EGG']),
    "BLUE_YOSHI": Driver(name='Blue Yoshi', rarity=Rarity.SUPER, special_powerup=POWERUPS['DASH_RING']),
    "PINK_YOSHI": Driver(name='Pink Yoshi', rarity=Rarity.SUPER, special_powerup=POWERUPS['HEART']),
    "YELLOW_PIT_CREW_TOAD": Driver(name='Yellow Toad (Pit Crew)', rarity=Rarity.SUPER, special_powerup=POWERUPS['GIANT_BANANA']),
    "LIGHT_BLUE_PIT_CREW_TOAD": Driver(name='Light-blue Toad (Pit Crew)', rarity=Rarity.SUPER, special_powerup=POWERUPS['ICE_FLOWER']),
    "BOWSER": Driver(name='Bowser', rarity=Rarity.SUPER, special_powerup=POWERUPS['BOWSER_SHELL']),
    "DONKEY_KONG": Driver(name='Donkey Kong', rarity=Rarity.SUPER, special_powerup=POWERUPS['GIANT_BANANA']),
    "DIDDY_KONG": Driver(name='Diddy Kong', rarity=Rarity.SUPER, special_powerup=POWERUPS['BANANA_BARRELS']),
    "LAKITU": Driver(name='Lakitu', rarity=Rarity.SUPER, special_powerup=POWERUPS['TRIPLE_GREEN_SHELLS']),
    "BOWSER_JR": Driver(name='Bowser Jr.', rarity=Rarity.SUPER, special_powerup=POWERUPS['BOWSER_SHELL']),
    "WARIO": Driver(name='Wario', rarity=Rarity.SUPER, special_powerup=POWERUPS['DOUBLE_BOBOMBS']),
    "WALUIGI": Driver(name='Waluigi', rarity=Rarity.SUPER, special_powerup=POWERUPS['DOUBLE_BOBOMBS']),
    "KING_BOO": Driver(name='King Boo', rarity=Rarity.SUPER, special_powerup=POWERUPS['LUCKY_SEVEN']),
    "BLACK_SHY_GUY": Driver(name='Black Shy Guy', rarity=Rarity.SUPER, special_powerup=POWERUPS['BOBOMB_CANNON']),
    "FREERUNNING_RED_KOOPA": Driver(name='Red Koopa (Freerunning)', rarity=Rarity.SUPER, special_powerup=POWERUPS['FIRE_FLOWER']),
    "BIRDO": Driver(name='Birdo', rarity=Rarity.SUPER, special_powerup=POWERUPS['BIRDO_EGG']),
    "PINK_SHY_GUY": Driver(name='Pink Shy Guy', rarity=Rarity.SUPER, special_powerup=POWERUPS['HEART']),
    "LIGHT_BLUE_BIRDO": Driver(name='Birdo (Light Blue)', rarity=Rarity.SUPER, special_powerup=POWERUPS['BIRDO_EGG']),
    "HAMMER_BRO": Driver(name='Hammer Bro', rarity=Rarity.SUPER, special_powerup=POWERUPS['HAMMER']),
    "BOOMERANG_BRO": Driver(name='Boomerang Bro', rarity=Rarity.SUPER, special_powerup=POWERUPS['BOOMERANG_FLOWER']),
    "ICE_BRO": Driver(name='Ice Bro', rarity=Rarity.SUPER, special_powerup=POWERUPS['ICE_FLOWER']),
    "FIRE_BRO": Driver(name='Fire Bro', rarity=Rarity.SUPER, special_powerup=POWERUPS['FIRE_FLOWER']),
    "YELLOW_BIRDO": Driver(name='Birdo (Yellow)', rarity=Rarity.SUPER, special_powerup=POWERUPS['BIRDO_EGG']),
    "MONTY_MOLE": Driver(name='Monty Mole', rarity=Rarity.SUPER, special_powerup=POWERUPS['MUSHROOM_CANNON']),
    "GREEN_SHY_GUY": Driver(name='Green Shy Guy', rarity=Rarity.SUPER, special_powerup=POWERUPS['TRIPLE_GREEN_SHELLS']),
    "FREERUNNING_BLUE_KOOPA": Driver(name='Blue Koopa (Freerunning)', rarity=Rarity.SUPER, special_powerup=POWERUPS['ICE_FLOWER']),
    "BLUE_BIRDO": Driver(name='Birdo (Blue)', rarity=Rarity.SUPER, special_powerup=POWERUPS['DASH_RING']),
    "FREERUNNING_PURPLE_KOOPA": Driver(name='Purple Koopa (Freerunning)', rarity=Rarity.SUPER, special_powerup=POWERUPS['DOUBLE_BOBOMBS']),
    "LIGHT_BLUE_SHY_GUY": Driver(name='Light-blue Shy Guy', rarity=Rarity.SUPER, special_powerup=POWERUPS['ICE_FLOWER']),

    # High-end:
    "METAL_MARIO": Driver(name='Metal Mario', rarity=Rarity.HIGH_END, special_powerup=POWERUPS['FIRE_FLOWER']),
    "PEACHETTE": Driver(name='Peachette', rarity=Rarity.HIGH_END, special_powerup=POWERUPS['MUSHROOM_CANNON']),
}

TRACKS = {
    "MARIO_CIRCUIT_1": Track(name='Mario Circuit 1', two_item_slot_drivers=[], three_item_slot_drivers=[]),
    "T_MARIO_CIRCUIT_1": Track(name='Mario Circuit 1T', two_item_slot_drivers=[DRIVERS['MARIO']], three_item_slot_drivers=[DRIVERS['BABY_MARIO']]),
    "WALUIGI_PINBALL": Track(name='Waluigi Pinball', two_item_slot_drivers=[], three_item_slot_drivers=[DRIVERS['BABY_MARIO']]),
    "RT_VANILLA_LAKE_1": Track(name='Vanilla Lake 1R/T', two_item_slot_drivers=[], three_item_slot_drivers=[DRIVERS['BABY_MARIO'].lvl(6)]),
}

TOURS = [
    Tour(name='Cat Tour', cups=[
        Cup(name='Test Cup', favored_driver=DRIVERS['WALUIGI'], courses=(
            Course(track=TRACKS['MARIO_CIRCUIT_1'], favored_driver=DRIVERS['MARIO']),
            Course(track=TRACKS['T_MARIO_CIRCUIT_1'], favored_driver=DRIVERS['FREERUNNING_PURPLE_KOOPA']),
            Course(track=TRACKS['WALUIGI_PINBALL'], favored_driver=DRIVERS['WALUIGI']),
            Course(track=TRACKS['RT_VANILLA_LAKE_1'], favored_driver=DRIVERS['SHY_GUY'], is_bonus=True)
        ))
    ])
]
