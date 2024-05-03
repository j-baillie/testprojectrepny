# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Turin = Character('Turin', color="#E03B8B")
define Aerin = Character('Aerin', color="#013220")

# The game starts here.

label start:
    scene bg
    with fade
    show turin
    "Turin" "Lady Aerin, I would beg your pardon once more, if I thought that this churl had ever done you anything but wrong."
    "Turin" "But speak now, and do not deny me! Am I not Turin, Lord of Dor-Lomin? Shall I command you?"
    show turin at left
    with fade
    show aerin at right
    "Aerin" "Command me."
    "Turin" "Who plundered the house of Morwen?"
    "Aerin" "Brodda."
    "Turin" "When did she flee, and whither?"
    "Aerin" "A year and three months gone."
    "Aerin" "Master Brodda and others of the Incomers of the East herabout opressed her sorely."
    "Aerin" "Long ago she was bidden to the Hidden Kingdom; and she went forth at last."
    "Aerin" "For the lands between were then free of evil for a while, because of the prowess of the Blacksword in the south country, it is said.."
    "Aerin" "But that has now ended..."
    "Aerin" "She looked to find her son there awaiting her. But if you be he, then I fear that all has gone awry..."

return