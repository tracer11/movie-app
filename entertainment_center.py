import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of toys that come to life",
                        "https://www.amazon.com/Toy-Story-Tim-Allen/dp/B0049J0DC8",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
                      "A story of a alien civilization",
                      "http://www.impawards.com/2009/avatar.html",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")


interstellar = media.Movie("Interstellar",
                            "A team goes to another galaxy to find a earth 2,0",
                            "https://movieweb.com/interstellar-movie-imax-poster/",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

movies = [toy_story, avatar, interstellar]
fresh_tomatoes.open_movies_page(movies)



