import urllib

from .constants import CATEGORY_LABELS, URLS
from .exceptions import UnexpectedDataKindException
from .scraper_generic import ScraperGeneric
from .shared import Global, logger
from .utils import get_api_content


class ScraperCategory(ScraperGeneric):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.category_template = Global.env.get_template("category.html")

    def get_items_name(self):
        return "category"

    def _add_category_to_scrape(self, category_key, category_title, is_expected):
        self.add_item_to_scrape(
            category_key,
            {
                "category_title": category_title,
            },
            is_expected,
        )

    def _get_category_key_from_title(self, category_title):
        return Global.convert_title_to_filename(category_title.lower())

    def _build_category_path(self, category_title):
        href = (
            Global.conf.main_url.geturl()
            + f"/Device/{category_title.replace('/', ' ')}"
        )
        final_href = Global.normalize_href(href)
        return final_href[1:]

    def get_category_link_from_obj(self, category):
        if "title" not in category or not category["title"]:
            raise UnexpectedDataKindException(
                f"Impossible to extract category title from {category}"
            )
        category_title = category["title"]
        return self.get_category_link_from_props(category_title=category_title)

    def get_category_link_from_props(self, category_title):
        category_path = urllib.parse.quote(self._build_category_path(category_title))
        if Global.conf.no_category:
            return f"home/not_scrapped?url={category_path}"
        category_key = self._get_category_key_from_title(category_title)
        if Global.conf.categories:
            is_not_included = True
            for other_category in Global.conf.categories:
                other_category_key = self._get_category_key_from_title(other_category)
                if other_category_key == category_key:
                    is_not_included = False
            if is_not_included:
                return f"home/not_scrapped?url={category_path}"
        self._add_category_to_scrape(category_key, category_title, False)
        return category_path

    def _process_categories(self, categories):
        for category in categories:
            category_key = self._get_category_key_from_title(category)
            self._add_category_to_scrape(category_key, category, True)
            self._process_categories(categories[category])

    def build_expected_items(self):
        if Global.conf.no_category:
            logger.info("No category required")
            return
        if Global.conf.categories:
            logger.info("Adding required categories as expected")
            for category in Global.conf.categories:
                category_key = self._get_category_key_from_title(category)
                self._add_category_to_scrape(category_key, category, True)
            return
        logger.info("Downloading list of categories")
        categories = get_api_content("/categories", includeStubs=True)
        self._process_categories(categories)
        logger.info("{} categories found".format(len(self.expected_items_keys)))

    def get_one_item_content(self, item_key, item_data):
        categoryid = item_key

        category_content = get_api_content(
            f"/wikis/CATEGORY/{categoryid}", langid=Global.conf.lang_code
        )

        if category_content and category_content["revisionid"] > 0:
            return category_content

        logger.warning("Falling back to category in EN")
        category_content = get_api_content(f"/wikis/CATEGORY/{categoryid}", langid="en")

        if category_content and category_content["revisionid"] > 0:
            return category_content

        for lang in URLS.keys():
            logger.warning(f"Falling back to category in {lang}")
            category_content = get_api_content(
                f"/wikis/CATEGORY/{categoryid}", langid=lang
            )

            if category_content and category_content["revisionid"] > 0:
                return category_content

        logger.warning(f"Impossible to get category content: {item_key}")
        Global.null_categories.add(item_key)

        return None

    def add_item_redirect(self, item_key, item_data, redirect_kind):
        path = self._build_category_path(item_data["category_title"])
        Global.add_redirect(
            path=path,
            target_path=f"home/{redirect_kind}?{urllib.parse.urlencode({'url':path})}",
        )

    def process_one_item(self, item_key, item_data, item_content):
        category_content = item_content

        category_rendered = self.category_template.render(
            category=category_content,
            label=CATEGORY_LABELS[Global.conf.lang_code],
            metadata=Global.metadata,
            lang=Global.conf.lang_code,
        )

        Global.add_html_item(
            path=self._build_category_path(category_title=category_content["title"]),
            title=category_content["display_title"],
            content=category_rendered,
        )
