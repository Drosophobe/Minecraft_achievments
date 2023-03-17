import json
json_name = input('Please enter your json file name (eg : 3fb42d28-ec47-4290-a097-185cb6e92b79)')
file = open(f"{json_name}.json")
data = json.load(file)
biomes_list_to_check = ["minecraft:badlands", "minecraft:bamboo_jungle", "minecraft:beach", "minecraft:birch_forest", "minecraft:cold_ocean", "minecraft:dark_forest", "minecraft:deep_cold_ocean", "minecraft:deep_dark", "minecraft:deep_frozen_ocean", "minecraft:deep_lukewarm_ocean", "minecraft:deep_ocean" ,"minecraft:desert" ,"minecraft:dripstone_caves", "minecraft:eroded_badlands", "minecraft:flower_forest" ,"minecraft:forest" ,"minecraft:frozen_ocean" ,"minecraft:frozen_peaks" ,"minecraft:frozen_river" ,"minecraft:grove", "minecraft:ice_spikes" ,"minecraft:jagged_peaks", "minecraft:jungle" ,"minecraft:lukewarm_ocean" ,"minecraft:lush_caves", "minecraft:mangrove_swamp", "minecraft:meadow" ,"minecraft:mushroom_fields", "minecraft:ocean", "minecraft:old_growth_birch_forest" ,"minecraft:old_growth_pine_taiga" ,"minecraft:old_growth_spruce_taiga", "minecraft:plains", "minecraft:river", "minecraft:savanna", "minecraft:savanna_plateau", "minecraft:snowy_beach", "minecraft:snowy_plains", "minecraft:snowy_slopes","minecraft:snowy_taiga", "minecraft:sparse_jungle", "minecraft:stony_peaks", "minecraft:stony_shore", "minecraft:sunflower_plains", "minecraft:swamp", "minecraft:taiga", "minecraft:warm_ocean", "minecraft:windswept_forest", "minecraft:windswept_gravelly_hills", "minecraft:windswept_hills", "minecraft:windswept_savanna", "minecraft:wooded_badlands"]
animals_list_to_check = ["minecraft:cat", "minecraft:fox", "minecraft:pig", "minecraft:turtle", "minecraft:frog", "minecraft:sheep", "minecraft:hoglin", "minecraft:mooshroom", "minecraft:strider", "minecraft:cow", "minecraft:goat", "minecraft:chicken", "minecraft:wolf", "minecraft:panda", "minecraft:rabbit", "minecraft:bee", "minecraft:axolotl", "minecraft:horse", "minecraft:donkey", "minecraft:ocelot", "minecraft:mule", "minecraft:llama" ]
nether_biomes_list_to_check = ["minecraft:crimson_forest", "minecraft:nether_wastes", "minecraft:soul_sand_valley", "minecraft:basalt_deltas", "minecraft:warped_forest"]
food_list_to_check  = ['cooked_porkchop', 'chicken', 'honey_bottle', 'cooked_mutton', 'sweet_berries', 'cooked_beef', 'chorus_fruit', 'baked_potato', 'beef', 'porkchop', 'tropical_fish', 'beetroot_soup', 'apple', 'spider_eye', 'potato', 'cooked_cod', 'rabbit', 'poisonous_potato', 'pumpkin_pie', 'mutton', 'pufferfish', 'bread', 'golden_apple', 'cookie', 'rotten_flesh', 'suspicious_stew', 'glow_berries', 'dried_kelp', 'salmon', 'melon_slice', 'beetroot', 'golden_carrot', 'cooked_rabbit', 'cooked_chicken', 'enchanted_golden_apple', 'mushroom_stew', 'cod', 'rabbit_stew', 'cooked_salmon', 'carrot']
cat_variants_to_check = ['minecraft:white', 'minecraft:tabby', 'minecraft:calico', 'minecraft:siamese', 'minecraft:jellie', 'minecraft:persian', 'minecraft:black', 'minecraft:ragdoll', 'minecraft:all_black', 'minecraft:british_shorthair', 'minecraft:red']
achievments_dict = {"husbandry/complete_catalogue": cat_variants_to_check, 
                    "husbandry/bred_all_animals": animals_list_to_check,
                    "adventure/adventuring_time":biomes_list_to_check,
                    "nether/explore_nether": nether_biomes_list_to_check,
                    "husbandry/balanced_diet": food_list_to_check}
class checking:
    def __init__(self, list_to_check, category, data = data):
        self.list_to_check = list_to_check
        self.category = category
        self.data = data

    def check_achievment(self):
        self.list_of_remaining = []
        for i in self.list_to_check:
            if i in self.data[f"minecraft:{self.category}"]["criteria"]:
                pass
            else: 
                self.list_of_remaining.append(i)
        print(f"{self.category} remaining {len(self.list_of_remaining)}")
        print(self.list_of_remaining)
for i in achievments_dict:
    checking(achievments_dict[i], i).check_achievment()
