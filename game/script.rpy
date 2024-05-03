# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character('Turin', color="#00008B")
define a = Character('Aerin', color="#013220")

# The game starts here.
#start is p187 - p188 of my copy of the book
label start:
    scene bg
    with fade
    show turin
    t "Lady Aerin, I would beg your pardon once more, if I thought that this churl had ever done you anything but wrong."
    t "But speak now, and do not deny me! Am I not Turin, Lord of Dor-Lomin? Shall I command you?"
    show turin at left with move
    show aerin at right with move
    a "Command me."
    t "Who plundered the house of Morwen?"
    a "Brodda."
    t "When did she flee, and whither?"
    a "A year and three months gone."
    a "Master Brodda and others of the Incomers of the East herabout opressed her sorely."
    a "Long ago she was bidden to the Hidden Kingdom; and she went forth at last."
    a "For the lands between were then free of evil for a while, because of the prowess of the Blacksword in the south country, it is said.."
    a "But that has now ended..."
    a "She looked to find her son there awaiting her. But if you be he, then I fear that all has gone awry..."

return