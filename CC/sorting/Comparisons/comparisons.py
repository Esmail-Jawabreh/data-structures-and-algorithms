def sort_movies_by_year(movies):
    """
    Sorts a list of movies by their release year in descending order.

    Args:
        movies (list): A list of dictionaries representing movies, each containing a "year" key.

    Returns:
        list: A new list of movies sorted by their release year in descending order.
    """
    sorted_movies = sorted(movies, key=lambda movie: movie["year"], reverse=True)
    return sorted_movies


def sort_movies_by_title(movies):
    """
    Sorts a list of movies by their title, ignoring leading articles (e.g., "The", "An", "A").

    Args:
        movies (list): A list of dictionaries representing movies, each containing a "title" key.

    Returns:
        list: A new list of movies sorted by their title, with leading articles removed.
    """

    def remove_leading_articles(title):
        """
        Removes leading articles from a movie title.

        Args:
            title (str): The movie title.

        Returns:
            str: The title with leading articles removed.
        """
        articles = ["The ", "An ", "A "]
        for article in articles:
            if title.startswith(article):
                return title[len(article) :]
        return title

    sorted_movies = sorted(
        movies, key=lambda movie: remove_leading_articles(movie["title"].lower())
    )
    return sorted_movies
