from media import Movie
import fresh_tomatoes

'''-----------Create Movie instances-----------'''

the_intern = Movie("The Intern",
                        "A CEO gets a 70 year old intern.",
                       "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
                        "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

about_time = Movie("About Time",
                     "Tim discovers that he can travel back in time.",
                     "https://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",
                     "https://www.youtube.com/watch?v=7OIFdWk83no")

inception = Movie("Inception",
                  "A dream within a dream within a dream.",
                "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                          "https://www.youtube.com/watch?v=8hP9D6kZseM")

the_dark_knight = Movie("The Dark Knight",
                        "Batman against the Joker",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

interstellar = Movie("Interstellar",
                     "Man was not born to die on Earth",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=0vxOhd4qlnA")

good_will_hunting = Movie("Good Will Hunting",
                          "It's not your fault",
                          "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
                          "https://www.youtube.com/watch?v=z02M3NRtkAA")

#filling up movies in a list
movies = [the_intern, about_time, inception, the_dark_knight, interstellar, good_will_hunting]

#calling the open movies page method to display movie tiles
fresh_tomatoes.open_movies_page(movies)
