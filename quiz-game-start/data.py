
def show_categories():
    import re
    html_code = """
    <select name="trivia_category" class="form-control">
        <option value="0">Any Category</option>
        <option value="9">General Knowledge</option>
        <option value="10">Entertainment: Books</option>
        <option value="11">Entertainment: Film</option>
        <option value="12">Entertainment: Music</option>
        <option value="13">Entertainment: Musicals &amp; Theatres</option>
        <option value="14">Entertainment: Television</option>
        <option value="15">Entertainment: Video Games</option>
        <option value="16">Entertainment: Board Games</option>
        <option value="17">Science &amp; Nature</option>
        <option value="18">Science: Computers</option>
        <option value="19">Science: Mathematics</option>
        <option value="20">Mythology</option>
        <option value="21">Sports</option>
        <option value="22">Geography</option>
        <option value="23">History</option>
        <option value="24">Politics</option>
        <option value="25">Art</option>
        <option value="26">Celebrities</option>
        <option value="27">Animals</option>
        <option value="28">Vehicles</option>
        <option value="29">Entertainment: Comics</option>
        <option value="30">Science: Gadgets</option>
        <option value="31">Entertainment: Japanese Anime &amp; Manga</option>
        <option value="32">Entertainment: Cartoon &amp; Animations</option>
    </select>
    """
    # Use regular expression to find all option tags
    options = re.findall(r'<option value="(\d+)">([^<]+)</option>', html_code)

    # Print the pairs in the specified format
    for value, category in options:
        print(f"{value}- {category}")


question_data = [
    {
        "question": "The Konami Code is known as Up, Up, Down, Down, Left, Right, Right, Left, B, A, Start.",
        "correct_answer": "False"
    },
    {
        "question": "The game &quot;Battlefield 1&quot; takes place during World War I.",
        "correct_answer": "True"
    },
    {
        "question": "&quot;Undertale&quot; is an RPG created by Toby Fox and released in 2015.",
        "correct_answer": "True"
    },
    {
        "question": "In the &quot;Half-Life&quot; series, &quot;H.E.V&quot; stands for &quot;Hazardous Evasiveness Vest&quot;",
        "correct_answer": "False"
    },
    {
        "question": "Luigi is taller than Mario?",
        "correct_answer": "True"
    },
    {
        "question": "The game &quot;Jetpack Joyride&quot; was created by &quot;Redbrick Studios&quot;.",
        "correct_answer": "False"
    },
    {
        "question": "Each piece in Tetris is called a tetris.",
        "correct_answer": "False"
    },
    {
        "question": "There are 2 player roles in Trouble in Terrorist Town.",
        "correct_answer": "False"
    },
    {
        "question": "There are 6 legendary cards in &quot;Clash Royale&quot;.",
        "correct_answer": "False"
    },
    {
        "question": "Niko Bellic is the protagonist of Grand Theft Auto IV.",
        "correct_answer": "True"
    },
    {
        "question": "The ghosts in &quot;Pac-Man&quot; and &quot;Ms. Pac-Man&quot; have completely different behavior.",
        "correct_answer": "True"
    },
    {
        "question": "The names of Tom Nook&#039;s cousins in the Animal Crossing franchise are named &quot;Timmy&quot; and &quot;Jimmy&quot;.",
        "correct_answer": "False"
    },
    {
        "question": "In the video game &quot;Splatoon&quot;, the playable characters were originally going to be rabbits instead of squids.",
        "correct_answer": "True"
    },
    {
        "question": "In Terraria, you can craft the Cell Phone pre-hardmode.",
        "correct_answer": "True"
    },
    {
        "question": "In Resident Evil 4, the Chicago Typewriter has infinite ammo.",
        "correct_answer": "True"
    },
    {
        "question": "Peter Molyneux was the founder of Bullfrog Productions.",
        "correct_answer": "True"
    },
    {
        "question": "In Heroes of the Storm, the Cursed Hollow map gimmick requires players to kill the undead to curse the enemy team.",
        "correct_answer": "False"
    },
    {
        "question": "Watch_Dogs 2 is a prequel.",
        "correct_answer": "False"
    },
    {
        "question": "The song &quot;Megalovania&quot; by Toby Fox made its third appearence in the 2015 RPG &quot;Undertale&quot;.",
        "correct_answer": "True"
    },
    {
        "question": "The ultimate phrase used by Pharah from Overwatch is: &quot;Justice rains from above!&quot;",
        "correct_answer": "True"
    },
    {
        "question": "Tetris is the #1 best-selling video game of all-time.",
        "correct_answer": "False"
    },
    {
        "question": "The Mann Co. Store from Team Fortress 2 has the slogan &quot;We hire mercenaries and get in fights&quot;.",
        "correct_answer": "False"
    },
    {
        "question": "In &quot;Super Mario Bros.&quot;, the clouds and bushes have the same artwork and are just different colors.",
        "correct_answer": "True"
    },
    {
        "question": "In Team Fortress 2, being disguised as a scout or medic results in a speed boost.",
        "correct_answer": "False"
    },
    {
        "question": "In RuneScape, one must complete the &quot;Dragon Slayer&quot; quest before equipping Rune Platelegs.",
        "correct_answer": "False"
    },
    {
        "question": "In Pok&eacute;mon Sun and Moon, a male Salandit can evolve to a Salazzle.",
        "correct_answer": "False"
    },
    {
        "question": "In &quot;Undertale&quot;, the main character of the game is Sans.",
        "correct_answer": "False"
    },
    {
        "question": "The end credits sequence in Grand Theft Auto 5 is over half an hour long.",
        "correct_answer": "True"
    },
    {
        "question": "Minecraft can be played with a virtual reality headset.",
        "correct_answer": "True"
    },
    {
        "question": "&quot;Metal Gear Solid 3: Snake Eater&quot; was released in 2004.",
        "correct_answer": "True"
    },
    {
        "question": "Several characters in &quot;Super Mario 64&quot; blink their eyes, including Mario himself.",
        "correct_answer": "True"
    },
    {
        "question": "Big the Cat is a playable character in &quot;Sonic Generations&quot;.",
        "correct_answer": "False"
    },
    {
        "question": "In the Super Mario series, the character Pauline is a Princess like Princess Peach.",
        "correct_answer": "False"
    },
    {
        "question": "The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.",
        "correct_answer": "False"
    },
    {
        "question": "In &quot;Space Station 13&quot;,  the station has a clown aboard it.",
        "correct_answer": "True"
    },
    {
        "question": "The 2005 video game &quot;Call of Duty 2: Big Red One&quot; is not available on PC.",
        "correct_answer": "True"
    },
    {
        "question": "In &quot;Need for Speed: Porsche Unleashed&quot;, the player can only drive cars manufactured by Porsche.",
        "correct_answer": "True"
    },
    {
        "question": "In &quot;Super Mario 3D World&quot;, the Double Cherry power-up originated from a developer accidentally making two characters controllable.",
        "correct_answer": "True"
    },
    {
        "question": "In Kingdom Hearts the Paopu fruit is said to intertwine the destinies for two people forever.",
        "correct_answer": "True"
    },
    {
        "question": "In the Monster Hunter Series, it is possible to capture Elder Dragons.",
        "correct_answer": "False"
    },
    {
        "question": "English new wave musician Gary Numan founded the video game development company Facepunch Studios in March 2009.",
        "correct_answer": "False"
    },
    {
        "question": "In Sonic the Hedgehog universe, Tails&#039; real name is Miles Prower.",
        "correct_answer": "True"
    },
    {
        "question": "Codemasters is the developer of the Gran Turismo series.",
        "correct_answer": "False"
    },
    {
        "question": "The main playable character of the 2015 RPG &quot;Undertale&quot; is a monster.",
        "correct_answer": "False"
    },
    {
        "question": "The shotgun appears in every numbered Resident Evil game.",
        "correct_answer": "True"
    },
    {
        "question": "Activision created Battlefield 1.",
        "correct_answer": "False"
    },
    {
        "question": "Gordon Freeman, the protagonist of &quot;Half-Life&quot;, is said to have once had a ponytail.",
        "correct_answer": "True"
    },
    {
        "question": "In Until Dawn, both characters Sam and Mike cannot be killed under any means until the final chapter of the game.",
        "correct_answer": "True"
    },
    {
        "question": "Tony Hawk&#039;s extreme sports videogames revolve around performing professional BMX tricks.",
        "correct_answer": "False"
    },
    {
        "question": "Ana was added as a new hero for the game Overwatch on July 19th, 2016.",
        "correct_answer": "True"
    }
]