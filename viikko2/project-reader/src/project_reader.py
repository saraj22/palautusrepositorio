from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        dependencies = data["tool"]["poetry"]["dependencies"]
        dev_dependencies = data["tool"]["poetry"]["group"]["dev"]["dependencies"]

        license = data["tool"]["poetry"]["license"]
        authors = data["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
