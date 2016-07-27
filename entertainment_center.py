import media
import fresh_tomatoes
# Defines the different movies and the information to be displayed with them
vendetta = media.Movie("V For Vendetta", """Set against the futuristic landscape of totalitarian Britain,
    V For Vendetta tells the story of a mild-mannered young woman named Evey.
    Who is rescued from a life-and-death situation by a masked vigilante known only as "V." """,
    "http://posterwire.com/wp-content/uploads/v_for_vendetta_b.jpg",
    "https://www.youtube.com/watch?v=lSA7mAHolAw",
    "http://www.imdb.com/title/tt0434409/")

sunshine = media.Movie("Sunshine",
    """In the not-too-distant future, Earth's dying sun spells the end for humanity.
    In a last-ditch effort to save the planet, a crew of eight men and women
     ventures into space with a device that could revive the star. """,
     "http://www.gstatic.com/tv/thumb/movieposters/161586/p161586_p_v8_aa.jpg",
     "https://www.youtube.com/watch?v=r8BSlqHAhuY",
     "http://www.imdb.com/title/tt0448134/")

cube = media.Movie("Cube",
    """Without remembering how they got there, several strangers
     awaken in a prison of cubic cells, some of them booby-trapped. """,
     "http://www.gstatic.com/tv/thumb/movieposters/20005/p20005_p_v8_aa.jpg",
     "https://www.youtube.com/watch?v=YAWSkYqqkMA",
     "http://www.imdb.com/title/tt0123755/")

dune = media.Movie("Dune",
    """In the year 10191, a spice called melange is the most valuable substance
     known in the universe, and its only source is the desert planet Arrakis.""",
     "http://t0.gstatic.com/images?q=tbn:ANd9GcQwwPKgIxuvos4p0NuR8SEeaCou_hETH-q4KdRmsrxMaAPlhI6I",
     "https://www.youtube.com/watch?v=KwPTIEWTYEI",
     "http://www.imdb.com/title/tt0087182/")



# Creates a list of the movie instances in list for fresh_tomatoes to open.
movies = [vendetta, sunshine, cube, dune]
fresh_tomatoes.open_movies_page(movies)
