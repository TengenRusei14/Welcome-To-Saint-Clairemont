
define mc = Character("[You]")
define gc = Character("[Allora Von Clairemont]")
define e = Character("Erius")

default gc = "???"

label start:
    jump intro

label intro:
    "I have lost my soul"
    "A monster came and took both my soul and body from me"
    "I am now nothing but a disgusting lump of old and rotten flesh"
    "I do not know what to do, where to go, who to stay with"
    "I cannot return home with the form I currently hold, I need to be myself once more"
    "I feel disgusted right to my stomach"
    "I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek, I reek "
    "Not even my bottle of Mr Miyagi's ultimate scent helps get rid of tnis awful smell"
    "Its been 3 days, and each passing day I'm beginning to hate myself more and more and unfortunately I cannot die"
    "Please someone"
    "Save me"
    "I'll do anything, I'll give you anything"

    gc "Even your soul"

    "Who was that?"
    mc "Is anyone there?"

    gc "I have asked you a question, will you give me your soul in return for your humanity?"

    "I'm so confused right now, what am I if not a soul but what is a soul if this is the body that carries it"
    "I prayed for a light and when the light has shun I'm hesitant....."
    mc "YES!!!"
    mc "As long as I can get rid of this wretched form and return to my family"

    gc "We have made a deal"

    "Suddenly a beautiful young lady with velvet hair appeared, she was short with extremely pale skin. If not for the fact that I was dying I would have thought she was a vampire"
    "But I cannot judge my saviour can I?"

    gc "You seem lost in thought"

    mc "I'm both grateful and at a loss of words, and a tiny bit skeptical?"
    mc "How can a girl as young as you save me?"

    gc "My name is Allora Von Clairemont"
    gc "The Empress of Saint Clairemont, And the founder of the Helics Foundation"
    gc "A foundation of Hunters and Investigators who fight against the same ghouls that took both your body and soul"
    gc "They all have their own independant wishes and desires. But one thing is for certain"
    gc "We all hate ghouls"

    "I could feel the anger in her face and her voice. They must have done something really terrible to recieve such hate"
    "But I understood because I felt the same way"

    gc "It's weird talking hear why dont you come with us"

    show text "You decided to follow Allora Von Clairemont since she seemed like your only hope. As you slowlyapproacged her car you could see the gazes of the people looking at you with absolute disgust. Once you arrive at her car, an old man appears and opens the door for you. You feel strange as he is the only one who has'nt shown you indifference in this form, you feel safe.......for now" with dissolve
    pause(2.0)
    hide text with dissolve

    show text "After what seemed like an hour ride you arrive at a huge mansion on a cliff and around it are houses. Like a tiny little kingdom owned by Allora and her family. You all get off" with dissolve
    pause(2.0)
    hide text with dissolve

    gc "Welcome....."
    gc "II still don't know your name"

    $  You = renpy.input("What is your name?")
    mc "My name is [You]"

    gc "Nice to meet you, [You]"

    mc "Likewise"
    mc "If you don't mind me asking where are we?"

    gc "Welcome to Saint Clairemont, a kingdom of people like you who wish to hunt down these ghouls for their own personal reasons"
    gc "Why don't you follow me to the Hall so you can meet up with Erius so hecan brief you on everything"

    show text "You followed her to the Hall. In there was a collection of tools and gears and what seemed like a shop and at the end of the hall was a tall man" with dissolve
    pause(2.0)
    hide text with dissolve

    e "I smell a ghoul."
    e "Empress Clairemont, Why would you bring an a outside ghoul into my holiest sanctuary"

    gc "I'm sorry Father, I found him sulking in an alleyway and thought he would help serve the cause"
    gc "He has lost his soul to a ghoul and has turned him into this hideous form. He could help us attain the Key to Fahmir"

    e "And how can I trust him. How do I know he is not here to destroy us from the inisde"
    e "WHAT IS YOU NAME GHOUL!!!"

    mc  "[You]"

    e "AND WHAT IS YOUR REASON FOR COMING HERE!!!"

    gc "Could you stop screaming?"

    e "SILENCE!!!"

    mc "I do not know where I am, She said she could return my body and soI decided to trust her now I'm here"
    mc "Although she gets to keep my soul, I'm fine as long as I can see my daughter again"

    e "We are the Helics Foundation, a foundation formed in the early 80s to fight off ghouls and retrieve the souls of those who have lost their body and soul"
    e "Unfortunately I do not have time to explain everything to you due to the high level of ghoul cases right now"
    e "Allora escort him to the dorms"

    gc "I apologize but he will handle it on his own"
    gc "Byeee"

    return
