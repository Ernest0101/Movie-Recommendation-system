import spacy #importing the language processing library

nlp = spacy.load('en_core_web_lg') #loading the large english language model

#opening the file and reading its contents
file = open('movies.txt')
movies = file.readlines()



#creating a dictionary using from the txt file
#initialising the empty dictionary
movie_dict = {}

#splitting the contents into lines
movie_lines = movies #.strip()

for line in movie_lines:

    #splitting the line into key and value using :
    parts = line.split(':')

    #creating the key, value pairs
    key = parts[0].strip()
    value = parts[1].strip()
    #adding the movies to the dictionarys
    movie_dict[key] = value

#printing the dictionary to see if it worked
#print(movie_dict['Movie D'])


#The movie reccomendation system
def recommedation_system(movie_description):

    movie_description = nlp(movie_description)

    #dictionary to store the similarity scores
    scores = {}

    for movie, description in movie_dict.items():
        #processing the descriptions
        #tokenising each description
        movie_doc = nlp(description)
        #finding the similarity scores for all the movie descriptions
        similarity = nlp(movie_description).similarity(movie_doc)

        #whatever the similarity were extracting the key, value pair
        scores[movie, description] = similarity

    #reccomending the film with the hoghest similarity
    recommendation = max(scores, key=scores.get)

    print(f"Based on the description provided, I would recommend: {recommendation}")





recomedation_system(hulk)

