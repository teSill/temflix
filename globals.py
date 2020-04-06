import discord
from imdb_manager import IMDbMovieData, IMDbActorData


class GlobalDiscordMethods:
    latest_movie_query = None

    @classmethod
    async def display_actor_in_chat(cls, name, ctx):
        actor = IMDbActorData(name)

        embedded_msg = discord.Embed(title=str(actor.actor_obj), description="%s" % str(actor.biography),
                                     color=0x00ff00)
        embedded_msg.set_thumbnail(url=actor.thumbnail)
        embedded_msg.set_image(url=actor.cover)

        await ctx.send(embed=embedded_msg)

    @classmethod
    async def display_movie_in_chat(cls, title, ctx):
        imdb = IMDbMovieData(title)
        GlobalDiscordMethods.latest_movie_query = imdb
        print("latest_movie_query set: " + GlobalDiscordMethods.latest_movie_query.title)

        embedded_msg = discord.Embed(title=imdb.title, description=imdb.plot, color=0x00ff00)
        embedded_msg.set_thumbnail(url=imdb.image)
        embedded_msg.add_field(name="Director", value=imdb.director, inline=False)
        embedded_msg.add_field(name="Cast", value=imdb.stars, inline=False)
        embedded_msg.add_field(name="Genres", value=imdb.genre, inline=False)
        embedded_msg.add_field(name="IMDb rating", value=imdb.rating, inline=False)
        embedded_msg.add_field(name="IMDb link", value=imdb.url, inline=False)
        embedded_msg.add_field(name="Release year", value=imdb.year, inline=False)
        embedded_msg.add_field(name="Runtime", value=imdb.runtime, inline=False)

        embedded_msg.set_footer(text="Want to add this title to your watchlist? Type '!temflix save'")

        await ctx.send(embed=embedded_msg)
