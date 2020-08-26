# Fever Hearts
Welcome to the alpha release of Fever Hearts, a puzzle programmed in Python as a component of a larger personal project.
The goal of game is to form a path of open valves (denoted by letters) from one end (the 'hot' red heart) to the other (the 'cold' blue heart), as connected by the veins (denoted by [/], [\\] or [-]).  
## Valves
All valves are closed for a set number of turns, and then open for a set, smaller number of turns. These values are affected by 'temperature'.  
Above each valve is an X (denoting closed) or O (denoting open). Below each valve is a number, denoting how many more turns it will remain closed/open. After every action, every valve's counter is reduced by one.
## Temperature
Every object has a temperature: hot, warm, lukewarm, or cold. Their symbol is colored to demonstrate this state. Temperature only affects valves. Whenever a valve opens, the temperature between it, all veins connected to it, all open other valves connected to those veins, and so on, are averaged. If a heart is connected in this way, its value contributes to the average, but is not changed. The colder a valve is, the longer it stays closed, and the shorter it remains open.  
## Gameplay
To play, simply type in the letter (capital or lowercase) of the valve you would like to target. If that valve is closed, its counter will be reduced by one further, effectively by two. If that valve is open, then the counter will be increased by one, effectively by zero. Use this to your advantage!
