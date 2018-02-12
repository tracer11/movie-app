import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of toys that come to life",
                        "https://ohmy.disney.com/wp-content/uploads/2014/01/toy-story-poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
                      "A story of a alien civilization",
                      "https://vignette.wikia.nocookie.net/avatar/images/3/3f/Avatar-poster.jpg/revision/latest?cb=20091209142005&path-prefix=hu",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")


interstellar = media.Movie("Interstellar",
                            "A team goes to another galaxy to find a earth 2,0",
                            "http://www.joblo.com/posters/images/full/interstellar-mcconaughey.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")



movies = [toy_story, avatar, interstellar]
fresh_tomatoes.open_movies_page(movies)



