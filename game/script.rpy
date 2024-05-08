# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character('Turin', color="#00008B")
define a = Character('Aerin', color="#013220")
define g = Character ('Glaurung', color="#89a572")

image turin stone = "turin_grey.png"

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

label scenetwo:
    scene nargorthrond with fade
    show glaurung
    g 'Hail, son of Hurin! Well met.'
    show glaurung at left with move
    show turin at right with move
    narrator 'straightway, Turin fell under the dreadful spell of the dragon, and was as one turned to stone'
    show turin stone with fade
    g 'Evil have been all your ways, son of Hurin!'
    g 'Thankless fosterling, outlaw, slayer of your friend, thief of love, usurper of Nargothrond, captain foolhardy, and deserter of your kin!'
    g 'As thralls your mother and your sister live in Dor-Lomin, in misery and want. You are arrayed as a prince, but they go in rags. For you, they yearn. But you care not for that!'
    g 'Glad may your father be to learn that he has such a son! As learn he shall...'
    narrator 'Glaurung withdrew his glance, and waited for Turin to wake from his stupor.'
    show turin with fade
    narrator 'With a loud cry, Turin sprang upon the dragon'
    g 'If you wish to be slain, I will slay you gladly! But small help will that be to Morwen and Nienor, no heed did you give to the cries of the elf woman!'
    g 'Will you deny also the bond of your blood?'
    narrator 'Turin jabbed at the great dragon\'s eye. At which point the wyrm reared up, towering above Turin.'
    g 'Nay, at least you are valiant, beyond all whom i have met. And they lie, who say that we of our part do not honour the valor of foes.'
    g 'See now! I offer you freedom! Go to your kin, if you can. Get you gone! And if elf or man be left to make tale of these days, then surely in scorn they will name you, if you spurn this gift!'
    narrator 'At this point, Turin turned and fled over the bridge'
    hide turin with fade
    g 'Haste you now, son of Hurin to Dor-Lomin, or perhaps the orcs are come before you, once again.'
    g 'And if you tarry for Finduilas, then  never shall you see Morwen or Nienor again, and they will curse you!'

return