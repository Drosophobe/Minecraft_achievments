import json
json_name = '3fb42d28-ec47-4290-a097-185cb6e92b79'
# Opening JSON file
file = open(f"{json_name}.json")
data = json.load(file)
biomes_list_to_check = ["Badlands", "Bamboo Jungle", "Beach", "Birch Forest", "Cherry Grove", "Cold Ocean", "Dark Forest", "Deep Cold Ocean", "Deep Dark", "Deep Frozen Ocean", "Deep Lukewarm Ocean", "Deep Ocean" ,"Desert" ,"Dripstone Caves", "Eroded Badlands", "Flower Forest" ,"Forest" ,"Frozen Ocean" ,"Frozen Peaks" ,"Frozen River" ,"Grove", "Ice Spikes" ,"Jagged Peaks", "Jungle" ,"Lukewarm Ocean" ,"Lush Caves", "Mangrove Swamp", "Meadow" ,"Mushroom Fields", "Ocean", "Old Growth Birch Forest" ,"Old Growth Pine Taiga" ,"Old Growth Spruce Taiga", "Plains", "River", "Savanna", "Savanna Plateau", "Snowy Beach", "Snowy Plains", "Snowy Slopes","Snowy Taiga", "Sparse Jungle", "Stony Peaks", "Stony Shore", "Sunflower Plains", "Swamp", "Taiga", "Warm Ocean", "Windswept Forest", "Windswept Gravelly Hills", "Windswept Hills", "Windswept Savanna", "Wooded Badlands"]
biomes_list_to_check_lowered = [x.lower() for x in biomes_list_to_check]
biomes_list_to_check_lowered_corrected = [s.replace(' ', '_') for s in biomes_list_to_check_lowered]

biomes_list_remaining = []
for i in biomes_list_to_check_lowered_corrected:
    if f"minecraft:{i}" in data["minecraft:adventure/adventuring_time"]["criteria"]:
        pass
    else:
        biomes_list_remaining.append(i)
print("There are {} biomes left for you to explore:".format(len(biomes_list_remaining)))
print(biomes_list_remaining)
animals_list_to_check = ["cat", "fox", "pig", "turtle", "frog", "sheep", "hoglin", "mooshroom", "strider", "cow", "goat", "chicken", "wolf", "panda", "rabbit", "bee", "axolotl", "horse", "donkey", "ocelot", "mule", "llama" ]
animals_list_remaining = []
for i in animals_list_to_check:
    if f"minecraft:{i}" in data['minecraft:husbandry/bred_all_animals']['criteria']:
        pass
    else:
        animals_list_remaining.append(i)
print("It remains you the {} following animals to reproduce".format(len(animals_list_remaining)))
print(animals_list_remaining)
nether_biomes_list_to_check = ["Crimson Forest", "Nether Wastes", "Soul Sand Valley", "Basalt Deltas", "Warped Forest"]
nether_biomes_list_to_check_lowered = [x.lower() for x in nether_biomes_list_to_check]
nether_biomes_list_to_check_lowered_corrected = [s.replace(' ', '_') for s in nether_biomes_list_to_check_lowered]
nether_biomes_list_remaining = []
for i in nether_biomes_list_to_check_lowered_corrected:
    if f"minecraft:{i}" in data["minecraft:nether/explore_nether"]["criteria"]:
        pass
    else:
        nether_biomes_list_remaining.append(i)
print("There are {} biomes left for you to explore:".format(len(nether_biomes_list_remaining)))
print(nether_biomes_list_remaining)
food_list_to_check_lowered_corrected  = ['cooked_porkchop', 'chicken', 'honey_bottle', 'cooked_mutton', 'sweet_berries', 'cooked_beef', 'chorus_fruit', 'baked_potato', 'beef', 'porkchop', 'tropical_fish', 'beetroot_soup', 'apple', 'spider_eye', 'potato', 'cooked_cod', 'rabbit', 'poisonous_potato', 'pumpkin_pie', 'mutton', 'pufferfish', 'bread', 'golden_apple', 'cookie', 'rotten_flesh', 'suspicious_stew', 'glow_berries', 'dried_kelp', 'salmon', 'melon_slice', 'beetroot', 'golden_carrot', 'cooked_rabbit', 'cooked_chicken', 'enchanted_golden_apple', 'mushroom_stew', 'cod', 'rabbit_stew', 'cooked_salmon', 'carrot']
food_list_remaining = []
for i in food_list_to_check_lowered_corrected:
    if f"{i}" in data["minecraft:husbandry/balanced_diet"]["criteria"]:
        pass
    else:
        food_list_remaining.append(i)
print("You have the following {} dishes to eat".format(len(food_list_remaining)))
print(food_list_remaining)
cat_variants_to_check = ['white', 'tabby', 'calico', 'siamese', 'jellie', 'persian', 'black', 'ragdoll', 'all_black', 'british_shorthair', 'red']
cat_variants_list_remaining = []
for i in cat_variants_to_check:
    if f"minecraft:{i}" in data["minecraft:husbandry/complete_catalogue"]["criteria"]:
        pass
    else:
        cat_variants_list_remaining.append(i)
print("You have the following {} dishes to eat".format(len(cat_variants_list_remaining)))
print(cat_variants_list_remaining)
