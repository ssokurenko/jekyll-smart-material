from pybeerxml import Parser
import pandas as pd

path_to_beerxml_file = "beers/on-tap.xml"

parser = Parser()
recipes = parser.parse(path_to_beerxml_file)


def build_recipe_info():
    dfcols = ['name', 'style', 'abv', 'og', 'fg', 'ibu', 'hops',
              'fermentables', 'yeasts']
    df_xml = pd.DataFrame(columns=dfcols)

    for recipe in recipes:
        # Collect the info about the beer
        name = recipe.name
        style = recipe.style.name
        abv = recipe.abv
        og = recipe.og
        fg = recipe.fg
        ibu = recipe.ibu
        hops = ""
        fermentables = ""
        yeasts = ""

        # iterate over the Hops
        for hop in recipe.hops:
            if hop.name not in hops:  # check if hop is already accounted for
                if len(hops) == 0:
                    hops += hop.name
                else:
                    hops += ", " + hop.name

        # iterate over the fermentables
        for fermentable in recipe.fermentables:
            if fermentable.name not in fermentables:
                if len(fermentables) == 0:
                    fermentables += fermentable.name
                else:
                    fermentables += ", " + fermentable.name

        # iterate over the yeast
        for yeast in recipe.yeasts:
            if yeast.name not in yeasts:
                if len(yeasts) == 0:
                    yeasts += yeast.name
                else:
                    yeasts += ", " + yeast.name

        # Add the recipe items to the data frame
        df_xml = df_xml.append(
            pd.Series([
                name, style, abv, og, fg, ibu, hops, fermentables, yeasts
            ],
             index=dfcols),
            ignore_index=True
        )
    return(df_xml)


foo = build_recipe_info()

foo.to_csv("_data/on-tap.csv")
