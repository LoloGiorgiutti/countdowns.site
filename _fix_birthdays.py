#!/usr/bin/env python3
"""Patch _daily_data.py: replace weak/wrong birthday entries with globally famous people."""

with open('_daily_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # (1,2) Taye Diggs → Isaac Asimov
    ('{"name":"Taye Diggs","known_for":"Actor (How Stella Got Her Groove Back)"}',
     '{"name":"Isaac Asimov","known_for":"Science fiction author (Foundation, I, Robot)"}'),
    # (1,10) Sal Khan (wrong birthday) → George Foreman
    ('{"name":"Sal Khan","known_for":"Founder of Khan Academy"}',
     '{"name":"George Foreman","known_for":"Two-time world heavyweight boxing champion and entrepreneur"}'),
    # (2,25) Tea Leoni → Enrico Caruso
    ('{"name":"Tea Leoni","known_for":"Actress"}',
     '{"name":"Enrico Caruso","known_for":"Italian operatic tenor, considered one of the greatest singers in history"}'),
    # (2,28) Bubba Smith → Brian Jones
    ('{"name":"Bubba Smith","known_for":"NFL player and actor"}',
     '{"name":"Brian Jones","known_for":"Founder and original guitarist of The Rolling Stones"}'),
    # (3,15) Fabio Lanzoni → Andrew Jackson
    ('{"name":"Fabio Lanzoni","known_for":"Model and pop culture icon"}',
     '{"name":"Andrew Jackson","known_for":"7th President of the United States, portrayed on the U.S. $20 bill"}'),
    # (3,24) Star Jones → Steve McQueen
    ('{"name":"Star Jones","known_for":"TV personality and lawyer"}',
     '{"name":"Steve McQueen","known_for":"Actor (Bullitt, The Great Escape, The Magnificent Seven)"}'),
    # (4,1) Asa Butterfield → Debbie Reynolds
    ('{"name":"Asa Butterfield","known_for":"Actor (Ender\'s Game, Sex Education)"}',
     '{"name":"Debbie Reynolds","known_for":"Actress (Singin\' in the Rain, The Unsinkable Molly Brown)"}'),
    # (4,27) Patrick Stump → Lizzo
    ('{"name":"Patrick Stump","known_for":"Lead singer of Fall Out Boy"}',
     '{"name":"Lizzo","known_for":"Singer and rapper (Truth Hurts, About Damn Time, Good as Hell)"}'),
    # (5,21) Gotye → Notorious B.I.G.
    ('{"name":"Gotye","known_for":"Singer (Somebody That I Used to Know)"}',
     '{"name":"Notorious B.I.G.","known_for":"Rapper (Juicy, Big Poppa, Hypnotize)"}'),
    # (5,21) Fairuza Balk → Jeffrey Dahmer
    ('{"name":"Fairuza Balk","known_for":"Actress (The Craft, American History X)"}',
     '{"name":"Jeffrey Dahmer","known_for":"Notorious American serial killer known as the Milwaukee Cannibal"}'),
    # (6,23) Selma Blair → Alan Turing
    ('{"name":"Selma Blair","known_for":"Actress"}',
     '{"name":"Alan Turing","known_for":"Computer science pioneer and WWII codebreaker, father of modern computing"}'),
    # (6,24) Solange Knowles → Lionel Messi
    ('{"name":"Solange Knowles","known_for":"Singer and sister of Beyoncé"}',
     '{"name":"Lionel Messi","known_for":"Football superstar, 8-time Ballon d\'Or winner, 2022 World Cup winner with Argentina"}'),
    # (6,27) Isabelle Adjani → Helen Keller
    ('{"name":"Isabelle Adjani","known_for":"French actress"}',
     '{"name":"Helen Keller","known_for":"Deaf-blind author and disability rights advocate"}'),
    # (7,11) Tab Hunter → Giorgio Armani
    ('{"name":"Tab Hunter","known_for":"1950s Hollywood actor"}',
     '{"name":"Giorgio Armani","known_for":"Italian fashion designer and founder of the Armani brand"}'),
    # (7,14) Tommy Mottola → Ingmar Bergman
    ('{"name":"Tommy Mottola","known_for":"Music executive"}',
     '{"name":"Ingmar Bergman","known_for":"Swedish film director (The Seventh Seal, Wild Strawberries, Persona)"}'),
    # (7,28) Soulja Boy → Beatrix Potter
    ('{"name":"Soulja Boy","known_for":"Rapper (Crank That)"}',
     '{"name":"Beatrix Potter","known_for":"Author and illustrator of Peter Rabbit and other beloved children\'s books"}'),
    # (7,29) Wil Wheaton → Benito Mussolini
    ('{"name":"Wil Wheaton","known_for":"Actor (Stand by Me, Star Trek: The Next Generation)"}',
     '{"name":"Benito Mussolini","known_for":"Italian fascist dictator who led Italy during World War II"}'),
    # (7,29) Josh Radnor → Peter Jennings
    ('{"name":"Josh Radnor","known_for":"Actor (How I Met Your Mother)"}',
     '{"name":"Peter Jennings","known_for":"ABC News anchor and one of America\'s most trusted journalists"}'),
    # (8,22) Paul Molitor → Dua Lipa
    ('{"name":"Paul Molitor","known_for":"Baseball Hall of Famer"}',
     '{"name":"Dua Lipa","known_for":"British-Albanian pop superstar (Levitating, Don\'t Start Now, New Rules)"}'),
    # (9,3) Paulina Porizkova (wrong birthday) → Shaun White
    ('{"name":"Paulina Porizkova","known_for":"Supermodel"}',
     '{"name":"Shaun White","known_for":"Three-time Olympic gold medalist snowboarder and skateboarder"}'),
    # (9,24) Kevin Sorbo → Jim Henson
    ('{"name":"Kevin Sorbo","known_for":"Actor (Hercules)"}',
     '{"name":"Jim Henson","known_for":"Creator of The Muppets (Kermit the Frog, Miss Piggy) and producer of Sesame Street"}'),
    # (10,10) Mya Harrison → Giuseppe Verdi
    ('{"name":"Mya Harrison","known_for":"R&B singer (Lady Marmalade)"}',
     '{"name":"Giuseppe Verdi","known_for":"Italian opera composer (La Traviata, Rigoletto, Aida)"}'),
    # (11,3) Gennaro Contaldo → Charles Bronson
    ('{"name":"Gennaro Contaldo","known_for":"Italian chef"}',
     '{"name":"Charles Bronson","known_for":"Action movie star (Death Wish, The Magnificent Seven, The Great Escape)"}'),
    # (11,10) Josh Peck → Martin Luther
    ('{"name":"Josh Peck","known_for":"Actor (Drake & Josh)"}',
     '{"name":"Martin Luther","known_for":"German theologian who sparked the Protestant Reformation"}'),
    # (11,10) Jack Arnold (wrong birthday) → Roy Scheider
    ('{"name":"Jack Arnold","known_for":"Director"}',
     '{"name":"Roy Scheider","known_for":"Actor (Jaws, The French Connection, All That Jazz)"}'),
    # (11,20) Duane 'Dog' Chapman → Robert F. Kennedy
    ('{"name":"Duane \'Dog\' Chapman","known_for":"TV personality (Dog the Bounty Hunter)"}',
     '{"name":"Robert F. Kennedy","known_for":"U.S. Attorney General and 1968 presidential candidate, brother of President JFK"}'),
    # (12,16) T.J. Miller → Ludwig van Beethoven
    ('{"name":"T.J. Miller","known_for":"Comedian and actor (Silicon Valley, Deadpool)"}',
     '{"name":"Ludwig van Beethoven","known_for":"Classical music composer (Symphony No. 5, Für Elise, Moonlight Sonata)"}'),
]

applied = 0
not_found = []
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        name_old = old.split('"name":"')[1].split('"')[0]
        name_new = new.split('"name":"')[1].split('"')[0]
        print(f"  ✓  {name_old} → {name_new}")
        applied += 1
    else:
        name_old = old.split('"name":"')[1].split('"')[0]
        not_found.append(name_old)
        print(f"  ✗  NOT FOUND: {name_old}")

with open('_daily_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nApplied {applied}/{len(replacements)} replacements.")
if not_found:
    print(f"Not found: {not_found}")
