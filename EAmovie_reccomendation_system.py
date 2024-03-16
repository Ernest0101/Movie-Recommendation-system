import spacy

nlp = spacy.load('en_core_web_lg')

#opening the file and reading its contents
file = open('movies.txt')
movies = file.readlines()

hulk = '''
When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space
 to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar 
where he is sold into slavery and trained as a gladiator
'''
#creating a dictionary using from the txt file


#initialising the empty dictionary
movie_dict = {}

#splitting the contents into lines
movie_lines = movies #.strip()

for line in movie_lines:

    #splitting the line into key and value using :
    parts = line.split(':')

    key = parts[0].strip()
    value = parts[1].strip()
    #adding the movies to the dictionarys
    movie_dict[key] = value

#printing the dictionary to see if it worked
#print(movie_dict['Movie D'])


