'''

    Given the URLs generated in info_generator/related_links.py,
    extract the corresponding webpage for further analysis.
    Clean to the maximum extent.
    Need not save in HTML format, can be beautiful souped or any other efficient HTML representations.
    Choose efficient storage like Mongo or pickle to save the final output.

    Can save the original HTML just in case. Save it in a separate folder.

'''
from goose import Goose

for url in URLs:
g = Goose({'browser_user_agent': 'Mozilla'})
article = g.extract(url=url)
print article.title
print article.cleaned_text[:500]
