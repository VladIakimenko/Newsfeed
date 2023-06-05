# Newsfeed

    A Django-based web application that develops base functionality for a news platform. The app provides a streamlined interface for administrators to publish and manage articles and their associated thematic sections (scopes). 
    It has a built-in admin panel that allows for the creation of articles with a title, text, publication date, and an optional image. Each article can be associated with one or more thematic sections known as scopes. Every article must have one main scope, and the rest are optional. Each scope is presented as a tag alongside each article, enabling users to understand the thematic area of the article at a glance.
    From a user's perspective, the site lists all the articles with their tags. The main scope of an article is presented first, followed by the rest of the scopes, all in alphabetical order.
    This project is a perfect starting point for any news-oriented web application and offers a high degree of flexibility to adapt to unique requirements.

![Screenshot](./screenshot.png)

## Behind the scene

The database is composed with three models:

- Article Model: This model represents an article on the news site. It holds the article's title, text, date of publication, and an optional image. The articles are ordered by their publication date, with the latest ones appearing first.
- Scope Model: The Scope model represents the thematic area of an article. It's a unique label that is used to categorize the articles.
- ArticleScope Model: This intermediary model links an Article with a Scope. It includes an is_main boolean field to mark the main scope of an article.

The frontend of the project is realized with Django templates (providing server-side html rendering) and uses the popular Bootstrap framework.

The project comes with a json dump with aritcles and sample photos for easy testing and formatting reference. Use Django's built-in "loaddata" command to populate the DB.


## Tech Stack

    Python
    Django
    Bootstrap

