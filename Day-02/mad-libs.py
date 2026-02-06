"""
# Google: 

=> Mad Libs is a popular phrasal template word game where one player prompts others for a list of words—such as nouns, verbs, adjectives, and adverbs—to fill in the blanks of a hidden story.

# Key details about Mad Libs:

(1) Gameplay: A player acting as the "reader" asks for specific parts of speech without revealing the context of the story.

(2) Purpose: It is used as a fun, creative, and educational activity to learn about grammar and parts of speech.

"""

"""
To add: 
Custom written snippet for story.
Formatting the output in proper manner.
...thinking.
"""

# The start of the program.

def main()->None:
    # def askForWords()->list[str]:
    #     wordList:list[str] = []
    #     wordList[0]= input("Enter the name of a person / character: ")       # Our character.
    #     wordList[1] = input("Enter the name of a place / event: ")           # The location
    #     wordList[2] = input("Enter the name of a fruit / vegetable: ")       # a food
    #     wordList[3] = input("Enter the name of an animal / bird: ")          # an animal
    #     wordList[4] = input("Enter an adjective (eg: hot, brave): ")         # an adjective
    #     wordList[5] = input("Enter a subject pronoun (eg: they, he , she): ")# a pronoun
    #     wordList[6] = input("Enter a  verb (in future tense): ")             # verd (future)
    #     wordList[7] = input("Enter an object pronoun (eg: him, them, her, my): ")  #pronoun(2)
    #     wordList[8] = 
    #     return wordList
    # return 


    def askForWords()->dict[str, str]:
        wordsToget: dict[str, str] = {
            "name": "the name of a person / character",
            "location" : "the name of a place / event",
            "foodItem" : "the name of a fruit / vegetable",
            "noun1" : "a noun (plural)",
            "noun2" : "another noun (abstract noun)",
            "noun3" : "yet another noun (uncountable but not abstract)",
            "pronoun1" : "a subjective pronoun (eg: he, she , we)",
            "pronoun2" : "an objective pronoun (eg: him, her, us)",
            "pronoun3" : "a possisive pronoun (eg: his, her, ours)",
            "adjective1": "an adjective of trait (eg: hot, sweet, brave)",
            "adjective2": "an adjective of quantity (eg: much, little, some)",
            "adjective3": "an adjective of color (eg: red, blue, green)",
            "adverb1": "an adverb of time denoting frequency (eg: always, often, usually)",
            "adverb2" : "an adverb of place (eg: here, there, upstairs, nearby)",
            "adverb3" : "an adverb of manner (eg: slowly, beautifully, hardly, perfectly)",
            "interjection": "an interjection (eg: Damn!, Alas! )",
            "conjunction" : "a conjunction (eg: and , so , but , for, nor)"

        }
        for key, value in wordsToget.items():
            wordsToget[key] = input(f"Enter {value}: ")

        print(wordsToget)
        return wordsToget

    
    def createStory()->None:
        words: dict[str, str] = askForWords()
        print(f"""
        ------------------------------------------------------------------------------------------------
        Start:


        "{words["interjection"]}!" {words["name"]} whispered into the comms channel. {words["pronoun1"]} had just landed {words["adverb2"]} on the surface of a planet made entirely of {words["noun1"]}. The air smelled faintly of {words["noun3"]}, which was a strange relief given the overwhelming {words["noun2"]} of deep space.

        Scanning the horizon, {words["name"]} spotted a/an {words["adjective3"]} {words["foodItem"]} growing out of a silver crater. It pulsed {words["adverb3"]}, almost as if it were breathing. {words["adverb1"]}, these alien lifeforms were friendly, {words["conjunction"]} this one looked particularly {words["adjective1"]}.

        "I need to bring {words["adjective2"]} samples back to the ship," {words["name"]} muttered. As the specimen was lifted, the ground began to shake. A voice boomed through the helmet, demanding to know why a stranger was touching {words["pronoun3"]} sacred garden. {words["name"]} froze as the planet itself seemed to reach out to grab {words["pronoun2"]}.


        :end
        ------------------------------------------------------------------------------------------------
        """)
    createStory()
    
    
    # askForWords()

if __name__ == "__main__":
    main()