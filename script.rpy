# Define the character
define astro = Character("Астронавт", color="#66ccff")

# Define images
image bg space = "images/bg/back1.png"
image astro normal = "images/characters/astronaut_normal.png"
image astro thinking = "images/characters/astronaut_thinking.png"

# Start of the game
label start:
    scene bg space with fade

    show astro normal at right
    astro "Хм. Ще один супутник… Знову потрібно перевірити сенсори."

    jump chapter1_dialog  # move to the main dialog

# Chapter 1 dialog
label chapter1_dialog:
    show astro thinking at right
    astro "Знаєте, цікаво: мій батько теж літав у космос. Але тоді ніхто серйозно не говорив про погоду в ньому."

    astro "Сонячні бурі здавались рідкістю, дрібницею. Чимось, про що пишуть у журналах, але не думають щодня."

    menu:
        "Продовжити слухати астронавта":
            astro "…Отже, ось чому космічна погода сьогодні важлива."
            jump after_choices

        "А що казав твій батько?":
            show astro normal at right
            astro "Він завжди повторював: «Не недооцінюй сонце»."
            jump after_choices

# After choices
label after_choices:
    astro "Але зараз ми знаємо набагато більше."
    return
