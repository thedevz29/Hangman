import random
words = [
    "Apple", "Blink", "Carpet", "Divide", "Elastic", "Friction", "Gaze", "Harmony", "Iceberg", "Journey",
    "Knot", "Lantern", "Marble", "Nest", "Orbit", "Ponder", "Quiver", "Ripple", "Sparkle", "Timber",
    "Universe", "Venture", "Willow", "Yearn", "Zephyr", "Accord", "Blend", "Canvas", "Delight", "Embrace",
    "Fabric", "Glimpse", "Harbor", "Ignite", "Jewel", "Kindle", "Laurel", "Meadow", "Noble", "Oasis",
    "Prism", "Quilt", "Realm", "Savor", "Tangle", "Unique", "Vessel", "Wander", "Yield", "Zest",
    "Anchor", "Blossom", "Cascade", "Drift", "Echo", "Feather", "Glint", "Harbor", "Ink", "Jigsaw",
    "Karma", "Linger", "Murmur", "Nestle", "Opal", "Pulse", "Quench", "Radiate", "Stumble", "Tidal",
    "Unison", "Veil", "Whisper", "Zeal", "Antique", "Balance", "Charm", "Dusk", "Ember", "Frost",
    "Glow", "Harbor", "Inspire", "Juggle", "Kettle", "Luminous", "Meadow", "Nomad", "Oasis", "Petal",
    "Quota", "Rustle", "Starlit", "Tide", "Umbrella", "Vapor", "Whisk", "Yield", "Zenith", "Adventure",
    "Breeze", "Crimson", "Desert", "Essence", "Flare", "Groove", "Horizon", "Illusion", "Journey", "Kite",
    "Labyrinth", "Moss", "Nectar", "Obelisk", "Pioneer", "Quest", "Ripple", "Sapphire", "Temple", "Unity",
    "Voyage", "Wisp", "Xenon", "Yarn", "Azure", "Blaze", "Cinder", "Dawn", "Echo", "Fable",
    "Glacier", "Haze", "Ivy", "Jungle", "Kin", "Lush", "Mirth", "Nook", "Omen", "Petal",
    "Quartz", "Rhythm", "Serene", "Thorn", "Umbra", "Vista", "Wonder", "Xylo", "Yearning", "Zephyr",
    "Amble", "Brisk", "Cascade", "Daze", "Elder", "Faint", "Glare", "Hymn", "Iota", "Jive",
    "Keen", "Loom", "Myth", "Nest", "Onyx", "Pace", "Quell", "Riddle", "Shiver", "Thrift",
    "Uprise", "Valley", "Whim", "Xyloid", "Yield", "Abyss", "Brood", "Cliff", "Delve", "Erode",
    "Flinch", "Glisten", "Halo", "Iris", "Jolt", "Knack", "Lilt", "Mellow", "Nudge", "Obscure",
    "Pulse", "Quiver", "Rapture", "Sage", "Torch", "Unity", "Vivid", "Whisper", "Zenith", "Blaze",
    "Charm", "Dabble", "Ember", "Floral", "Gale", "Heed", "Ivory", "Jagged", "Kite", "Linger",
    "Mingle", "Nestle", "Oasis", "Ponder", "Quest", "Radiant", "Silken", "Tarnish", "Unfurl", "Veil",
    "Wander", "Xylophone", "Yearning", "Zeal", "Azure", "Bloom", "Cloak", "Dew", "Embrace", "Flutter",
    "Glint", "Harmony", "Ignite", "Jewel", "Kindred", "Lull", "Mirth", "Nest", "Orchid", "Plume",
    "Quirk", "Rustle", "Savor", "Tranquil", "Untamed", "Velvet", "Whirl", "Yonder", "Zephyr", "Allure",
    "Brim", "Creek", "Dapple", "Evoke", "Faint", "Glimmer", "Hollow", "Instinct", "Journey", "Keepsake",
    "Lucid", "Murmur", "Nurture", "Odyssey", "Pinnacle", "Quench", "Riddle", "Scribe", "Thrive", "Umber",
    "Verdant", "Wanderlust", "Xenon", "Yonder", "Zealot", "Affinity", "Benevolent", "Crescent", "Dappled", "Effervescent",
    "Flicker", "Glade", "Hushed", "Inspire", "Jaunt", "Kismet", "Luminous", "Muse", "Nestled", "Oracle",
    "Prowess", "Quarry", "Rapture", "Serenity", "Traverse", "Unity", "Vibrant", "Whispered", "Yoke", "Zeal",
    "Arcane", "Briskly", "Clever", "Dulcet", "Ethereal", "Fable", "Gossamer", "Heirloom", "Idyllic", "Jovial",
    "Keenly", "Lavish", "Mirage", "Nimble", "Obscura", "Periwinkle", "Quasar", "Reverie", "Solace", "Thistle",
    "Undulate", "Verdure", "Whimsy", "Xylem", "Yielding", "Auspice", "Bracken", "Crescendo", "Dewy", "Effulgent",
    "Fen", "Gloaming", "Hallowed", "Inlet", "Jubilant", "Kith", "Lilt", "Meander", "Nocturne", "Oblique",
    "Parch", "Quixotic", "Resonant", "Succulent", "Twill", "Urn", "Valiance", "Winnow", "Yew", "Zealous",
    "Arcadia", "Burgeon", "Crepuscular", "Dappled", "Elixir", "Fissure", "Gossamer", "Hushed", "Incandescent", "Jovial",
    "Kaleidoscope", "Lichen", "Mystique", "Nimbus", "Opalescent", "Petrel", "Quasar", "Rivulet", "Sable", "Tessellate",
    "Ubiquitous", "Virelay", "Whorl", "Yew", "Zeal", "Aegis", "Bliss", "Crystalline", "Dalliance", "Elysian",
    "Fountain", "Glade", "Hinterland", "Illumine", "Jargon", "Keepsake", "Luminous", "Myriad", "Nebula", "Oasis",
    "Paean", "Quietude", "Radiance", "Sanctuary", "Threnody", "Utopia", "Vale", "Whim", "Yen", "Zenith",
    "Arcadia", "Boreal", "Cascade", "Dawn", "Effervesce", "Fey", "Gossamer", "Haunt", "Iridescence", "Journey",
    "Kith", "Lore", "Mirage", "Nimbus", "Oracle", "Petal", "Quotidian", "Realm", "Solitude", "Thistle",
    "Unveil", "Verdure", "Wander", "Xenolith", "Yonder", "Zephyr", "Aura", "Bracken", "Chime", "Drizzle",
    "Ephemeral", "Fervor", "Glimpse", "Hallowed", "Illume", "Jubilance", "Keen", "Luminous", "Muse", "Nestle",
    "Obelisk", "Paragon", "Quietude", "Respite", "Serein", "Traverse", "Uplift", "Vivid", "Wisp", "Yearling",
    "Zephyr", "Abyssal", "Brilliance", "Crescent", "Drift", "Effervescent", "Flora", "Gossamer", "Hollow", "Insignia",
    "Jubilant", "Kismet", "Lush", "Mystic", "Nostalgia", "Oblivion", "Pinnacle", "Questing", "Ripple", "Sublime",
    "Tenacity", "Unity", "Vibrance", "Wander", "Xyloid", "Yearning", "Zealot", "Azure", "Brisk", "Cascade"
]

score = {"1": ("    ")
         ("    ")
         ("    "),
    "2": (" ( ) ")
         ("    ")
         ("    "), # type: ignore
    "3": (" ( )  ")
         ("  |  ")
         ("    "),# type: ignore
    "4": ("  ( )  ")
         ("  -|  ")
         ("    "),# type: ignore
    "5": ("  ( )  ")
         ("  -|-  ")
         ("    "),
         
    "6": ("  ( )  ")
         ("  -|-  ")
         ("  /  "),
    "7": ("  ( )  ")
         ("  -|-  ")
         ("  / \ ")}

class Hangman:
    
    def __init__(self):
        pass
    
    def play(self):
        word = random.choice(words)
        print("Welcome to the hangman game made by Atharv Sharma")
        print(f"word[0]", {" _ "*len(word)-1})
        
        
        
        
        guess = input("Enter your guess: ")
        
        
