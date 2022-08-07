# X 2022

This project is a game based on the above story where you, the character has to move around the map and collect Antenna, Tools, Circuit, Solar Panel, Manual, Food, Fuel, Automatic Guns, Space Satellite and Medication. The game additionally returns the optimum number of days to make it challenging.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install tkinter
pip install turtle
```

## Rules
```
-> The player initially has 50 steps on the first day. (He is human! His stamina is limited) 
-> Every subsequent day you get an additional 5 steps to continue with your character's journey.
-> Each day lasts for 8 hours and every step consumes 30 minutes.
-> Once the 8 hours are over, you have to either be at the start position or resource blocks.
-> The palyer has a total of 3 energy points which refreshes everyday. You cannot go down to 0 energy points and the only way you can lose energy is by passing the sword action blocks.
-> The dotted lines can only be used to travel by the character when they have a launch action in their inventory which has been elaborated below.
-> There is are a few action block which are :
> Negative Steps : -5 Steps if you go over it
> Lock : you can only go through it if you have the key
> Swords : You lose -1 energy when you go through it
> Launch : You can use this ability to go through the dotted lines only               
once.
 -> These action blocks will be randomly generated around the map and the number of each action depends on the input the user makes at the beginning.
-> The key has an extremely crucial role which is that it allows the character to pass through the locks which was earlier not possible without the key.
-> The big blocks containing the resources will remain fixed but the small blocks containing the actions are randomly placed every time the application is run, this means that the action blocks can randomly be placed on the small blocks. keep in mind the total number of action blocks are decided by the user by taking the values of each as an input.
```

## How to run
```
-> Install the following files -:
   1) main.py
   2) MINET_IMAGE.png
   3) KEY.gif, LAUNCH.gif, LOCK.gif, NEGATIVE_STEPS.gif, SWORDS.gif
-> Run the main.py file.
```