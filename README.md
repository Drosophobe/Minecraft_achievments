# Minecraft_achievments
short python program to track Minecraft successes

This small Python program (3.9) has been designed to track the following untraceable completions in game: Nether/Explore all Nether biomes 
      Adventure/Adventuring Time
      Husbandry/Two by Two
      Husbandry/A Complete Catalogue
      Husbandary/A Balanced Diet
At first you have to copy and paste the json file accessible at /Library/Application Support/minecraft/saves/<world>/advancements (MacOS) or C:\Users\<user>\AppData\Roaming\.minecraft\saves<world>\advancements (Windows) in the same directory as the main file.
Then you have to run the following comment (python3 main.py) to launch the program.
Once the program is launched you can copy the name of your json file into the terminal.
After a very short lapse of time the unfulfilled steps will be displayed.


NOTE : The current version of Minecraft is 19.4. You will have to add the new biome (cherry_grove) and new mobs (sniffer & camel) in the next version 20.0. moreover the only used library is json which is native with Python 3.9+.