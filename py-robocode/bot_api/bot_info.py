import json
from functools import reduce

class BotInfo:
    MAX_NAME_LENGTH: int = 30
    MAX_VERSION_LENGTH: int = 20
    MAX_AUTHOR_LENGTH: int = 50
    MAX_DESCRIPTION_LENGTH: int = 250
    MAX_HOMEPAGE_LENGTH: int = 150
    MAX_GAME_TYPE_LENGTH: int = 20
    MAX_PLATFORM_LENGTH: int = 30
    MAX_PROGRAMMING_LANG_LENGTH: int = 30
    MAX_NUMBER_OF_AUTHORS: int = 5
    MAX_NUMBER_OF_COUNTRY_CODES: int = 5
    MAX_NUMBER_OF_GAME_TYPES: int = 10

    def __init__(self, name: str, version: str, authors: list[str], description: str, homepage: str, country_codes: list[str], game_types: list[str], platform: str, programming_lang: str) -> None:
        self.name = self.process_name(name)
        self.version = self.process_version(version)
        self.authors = self.process_authors(authors)
        self.description = self.process_description(description)
        self.homepage = self.process_homepage(homepage)
        self.country_codes = self.process_country_codes(country_codes)
        self.game_types = self.process_game_types(game_types)
        self.platform = self.process_platform(platform)
        self.programming_lang = self.process_programming_lang(programming_lang)

    @classmethod
    def from_file(cls, path: str):
        file = open(path)
        data = json.load(file)

        return cls(data["name"], data["version"], data["authors"], data["description"], data["homepage"], data["countryCodes"], data["gameTypes"], data["platform"], data["programmingLang"])

    def process_name(self, name: str) -> str:
        if not name:
            raise ValueError("Property \"name\" cannot be empty.")

        if len(name) > self.MAX_NAME_LENGTH:
            raise ValueError(f"Property \"name\" length exceeds the maximum of {self.MAX_NAME_LENGTH} characters")

        return name

    def process_version(self, version: str) -> str:
        if not version:
            raise ValueError("Property \"version\" cannot be empty.")

        if len(version) > self.MAX_VERSION_LENGTH:
            raise ValueError(f"Property \"version\" length exceeds the maximum of {self.MAX_VERSION_LENGTH} characters")

        return version

    def process_authors(self, authors: list[str]) -> list[str]:
        if not authors or not reduce(lambda x, y: x + y, authors):
            raise ValueError("Property \"authors\" cannot be empty.")

        if len(authors) > self.MAX_NUMBER_OF_AUTHORS:
            raise ValueError(f"Size of property \"authors\" exceeds the maximum of {self.MAX_NUMBER_OF_AUTHORS}.")

        for author in authors:
            if len(author) > self.MAX_AUTHOR_LENGTH:
                raise ValueError(f"Property \"author\" length exceeds the maximum of {self.MAX_AUTHOR_LENGTH} characters.")

        return authors

    def process_description(self, description: str) -> str:
        if not description:
            raise ValueError("Property \"description\" cannot be empty.")

        if len(description) > self.MAX_DESCRIPTION_LENGTH:
            raise ValueError(f"Property \"description\" length exceeds the maximum of {self.MAX_DESCRIPTION_LENGTH} characters")

        return description

    def process_homepage(self, homepage: str) -> str:
        if not homepage:
            raise ValueError("Property \"homepage\" cannot be empty.")

        if len(homepage) > self.MAX_HOMEPAGE_LENGTH:
            raise ValueError(f"Property \"homepage\" length exceeds the maximum of {self.MAX_HOMEPAGE_LENGTH} characters")

        return homepage

    def process_country_codes(self, country_codes: list) -> list:
        if len(country_codes) > self.MAX_NUMBER_OF_COUNTRY_CODES:
            raise ValueError(f"Size of property \"countryCodes\" exceeds the maximum of {self.MAX_NUMBER_OF_COUNTRY_CODES}.")

        return country_codes

    def process_game_types(self, game_types: list) -> list:
        if len(game_types) > self.MAX_NUMBER_OF_GAME_TYPES:
            raise ValueError(f"Size of property \"gameTypes\" exceeds the maximum of {self.MAX_NUMBER_OF_GAME_TYPES}.")

        for game_type in game_types:
            if len(game_type) > self.MAX_GAME_TYPE_LENGTH:
                raise ValueError(f"Property \"gameType\" length exceeds the maximum of {self.MAX_GAME_TYPE_LENGTH} characters.")

        return game_types

    def process_platform(self, platform: str) -> str:
        if not platform:
            raise ValueError("Property \"platform\" cannot be empty.")

        if len(platform) > self.MAX_PLATFORM_LENGTH:
            raise ValueError(f"Property \"platform\" length exceeds the maximum of {self.MAX_PLATFORM_LENGTH} characters")

        return platform

    def process_programming_lang(self, programming_lang: str) -> str:
        if not programming_lang:
            raise ValueError("Property \"programmingLang\" cannot be empty.")

        if len(programming_lang) > self.MAX_PROGRAMMING_LANG_LENGTH:
            raise ValueError(f"Property \"programmingLang\" length exceeds the maximum of {self.MAX_PROGRAMMING_LANG_LENGTH} characters")

        return programming_lang

