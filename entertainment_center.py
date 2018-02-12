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
                            "A team goes to another galaxy to find a earth 2.0",
                            "http://www.joblo.com/posters/images/full/interstellar-mcconaughey.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

dunkirk = media.Movie("Dunkirk",
                      "A story of British soldiers being rescued from the surrounding Nazi soldiers",
                      "https://images-na.ssl-images-amazon.com/images/I/410yY%2BU925L.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU"
                      )

fury = media.Movie("Fury",
                  "A story about a American Tank Squad",
                  "http://www.joblo.com/posters/images/full/fury-poster-new.jpg",
                  "https://www.youtube.com/watch?v=-OGvZoIrXpg")

hangover = media.Movie("The Hangover",
                      "A group of friends have a crazy adventure in Vegas",
                      "http://www.togomeetings.com/wp-content/uploads/2017/08/luxury-hangover-poster-and-modern-of-delhi-belly-poster-is-copied-from-the-hangover-posters-4.jpg",
                      "https://www.youtube.com/watch?v=tcdUhdOlz9M")



movies = [toy_story, avatar, interstellar, dunkirk, fury, hangover]
fresh_tomatoes.open_movies_page(movies)



