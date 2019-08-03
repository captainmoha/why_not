import urllib.request as urllib

LVL_1_TITLES = ["Chapter 01 - This is a song.mp3","Chapter 02 - Hey, taxi!.mp3","Chapter 03 - Hotel Europa.mp3","Chapter 04 - Who’s speaking, please'.mp3","Chapter 05 - That is impolite!.mp3","Chapter 06 - What do you do for a living'.mp3","Chapter 07 - You are strange!.mp3","Chapter 08 - Where do you come from'.mp3","Chapter 09 - You already know that!.mp3","Chapter 10 - Have you got a free room'.mp3","Chapter 11 - Not another of these rooms!.mp3","Chapter 12 - A student or a porter'.mp3","Chapter 13 - Here’s my key!.mp3","Chapter 14 - You will come to Aachen, won't you'.mp3","Chapter 15 - Are you selling the cassettes, too'.mp3","Chapter 16 - Try it on!.mp3","Chapter 17 - Four cups - that’s four marks altogether.mp3","Chapter 18 - No belongings, no luggage.mp3","Chapter 19 - I’d like to go to sleep.mp3","Chapter 20 - Are you ill'.mp3","Chapter 21 - I was in Essen.mp3","Chapter 22 - And what about his wife'.mp3","Chapter 23 - Who’s that speaking'.mp3","Chapter 24 - Would you like another coffee'.mp3","Chapter 25 - I’ll pay the rest.mp3","Chapter 26 - It’s on me.mp3","Appendix 01 - Introduction: How to Use this Handbook.mp3","Appendix 02 - Contents.mp3","Appendix 03 - Summary of grammar.mp3","Appendix 04 - Key to the exercises.mp3","Appendix 05 - Alphabetical list of vocabulary.mp3","Appendix 06 - Translations of the dialogues.mp3"]
LVL_2_TITLES = ["Chapter 01 - Who are you'.mp3","Chapter 02 - What can I do for you'.mp3","Chapter 03 - It is very central.mp3","Chapter 04 - Impossible!.mp3","Chapter 05 - A bus can’t be charming!.mp3","Chapter 06 - Perhaps she needs help'.mp3","Chapter 07 - My plane leaves at nine o’clock.mp3","Chapter 08 - You shouldn’t do that!.mp3","Chapter 09 - Bananas for me!.mp3","Chapter 10 - You always want to know everything.mp3","Chapter 11 - How about going to the theatre'.mp3","Chapter 12 - My studies are going okay.mp3","Chapter 13 - Have you got it in black'.mp3","Chapter 14 - It’s said to be very interesting.mp3","Chapter 15 - A man by the name of Mack the Knife.mp3","Chapter 16 - Somebody heard that.mp3","Chapter 17 - Where does the name \"Aachen\" come from'.mp3","Chapter 18 - He told me that.mp3","Chapter 19 - How do you speak to an emperor'.mp3","Chapter 20 - I’ve booked a room.mp3","Chapter 21 - How do I get to the post office'.mp3","Chapter 22 - At seven o’clock on Wednesday morning.mp3","Chapter 23 - What happened'.mp3","Chapter 24 - I forgot about it.mp3","Chapter 25 - Can you give me some more hand towels'.mp3","Chapter 26 - The trip to the Loreley is wonderful.mp3","Appendix 01 - Introduction: How to Use this Handbook.mp3","Appendix 02 - Contents.mp3","Appendix 03 - Summary of grammar.mp3","Appendix 04 - Key to the exercises.mp3","Appendix 05 - Alphabetical list of vocabulary.mp3","Appendix 06 - Translations of the dialogues.mp3"]
LVL_3_TITLES = ["Chapter 01 - The music is super!.mp3","Chapter 02 - My name is Ex.mp3","Chapter 03 - Will you take me with you'.mp3","Chapter 04 - Have you got a city map'.mp3","Chapter 05 - I’ll serve the drinks.mp3","Chapter 06 - He doesn’t know his date of birth'.mp3","Chapter 07 - Can you give me the brochures'.mp3","Chapter 08 - I haven’t heard any more from her.mp3","Chapter 09 - I sang her a song.mp3","Chapter 10 - I’d like to reserve a room.mp3","Chapter 11 - She scattered peas.mp3","Chapter 12 - Someone was supposed to say the magic word.mp3","Chapter 13 - Where did you park your car'.mp3","Chapter 14 - Then they thought of Frederick.mp3","Chapter 15 - Invisible and cheeky.mp3","Chapter 16 - But today it’s different.mp3","Chapter 17 - I still have a suitcase in Berlin.mp3","Chapter 18 - Bahnhof Zoo.mp3","Chapter 19 - I’m glad you’re in Berlin.mp3","Chapter 20 - Before the Wall went up....mp3","Chapter 21 - Everything is getting very expensive.mp3","Chapter 22 - Berlin Alexanderplatz.mp3","Chapter 23 - The famous Charité hospital.mp3","Chapter 24 - The dead are not always dead.mp3","Chapter 25 - I’d like small assignments to begin with.mp3","Chapter 26 - We just want to be together.mp3","Appendix 01 - Introduction: How to Use this Handbook.mp3","Appendix 02 - Contents.mp3","Appendix 03 - Summary of grammar.mp3","Appendix 04 - Key to the exercises.mp3","Appendix 05 - Alphabetical list of vocabulary.mp3","Appendix 06 - Translations of the dialogues.mp3"]
LVL_4_TITLES = ["Chapter 01 - That’s a great idea!.mp3","Chapter 02 - What would you like to do'.mp3","Chapter 03 - Brandenburg: Water, sand and potatoes.mp3","Chapter 04 - A poem: Herr von Ribbeck auf Ribbeck.mp3","Chapter 05 - The poem was banned.mp3","Chapter 06 - After the fall of the Wall.mp3","Chapter 07 - A multi-cultural society.mp3","Chapter 08 - The UFA film studios in Babelsberg.mp3","Chapter 09 - \"A medicine woman\".mp3","Chapter 10 - Mecklenburg-Vorpommern: Water and shipyards.mp3","Chapter 11 - The island of Rügen.mp3","Chapter 12 - Klaus Störtebecker.mp3","Chapter 13 - A rowing club.mp3","Chapter 14 - Living in a high-rise.mp3","Chapter 15 - Sachsen: Music and Industry.mp3","Chapter 16 - Environmental problems.mp3","Chapter 17 - A walk through Leipzig.mp3","Chapter 18 - Porcelain - the white gold.mp3","Chapter 19 - Sachsen-Anhalt: Nature, Industry and Religion.mp3","Chapter 20 - “The Brocken is German”.mp3","Chapter 21 - Coal - the black gold.mp3","Chapter 22 - Thüringen: The green heart.mp3","Chapter 23 - The legend of Barbarossa.mp3","Chapter 24 - Luther in the Wartburg castle.mp3","Chapter 25 - The Blue Flower.mp3","Chapter 26 - A magic word.mp3","Appendix 01 - Introduction: How to Use this Handbook.mp3","Appendix 02 - Contents.mp3","Appendix 03 - Summary of grammar.mp3","Appendix 04 - Key to the exercises.mp3","Appendix 05 - Alphabetical list of vocabulary.mp3","Appendix 06 - Translations of the dialogues.mp3"]


def download_course_lvl(base_url, lvl, titles_list):
  lvl_pos1 = base_url.find('/eng') - 1
  lvl_pos2 = base_url.find('_Lektion') - 1
  lesson_pos = base_url.find('_dwdownload') - 2

  lvl_url = base_url[0:lvl_pos1] + str(lvl)
  lvl_url += base_url[lvl_pos1+1: lvl_pos2] + str(lvl)
  lvl_url += base_url[lvl_pos2+1: lesson_pos]

  lvl_url_suffex = base_url[lesson_pos + 2:]
  print(lvl_url)
  
  
  for i in range(1, 27):
    lesson_url = lvl_url
    if i < 10:
        lesson_url += '0' + str(i)
    else:
        lesson_url += str(i)

    lesson_url += lvl_url_suffex
    print(titles_list[i-1])
    print(lesson_url)

    # download lesson mp3 file
    urllib.urlretrieve(lesson_url, filename=titles_list[i-1])

    

base_url = 'https://radiodownloaddw-a.akamaihd.net/Events/dwelle/deutschkurse/deutschwarumnicht/serie1/eng/DWN_Englisch_Serie1_Lektion27_dwdownload.mp3'

download_course_lvl(base_url, 1, LVL_1_TITLES)
download_course_lvl(base_url, 2, LVL_2_TITLES)
download_course_lvl(base_url, 3, LVL_3_TITLES)
download_course_lvl(base_url, 4, LVL_4_TITLES)
