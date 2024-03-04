import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib import helpers as h


class UrlsearchPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPackageController, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'urlsearch')

    # IPackageController
    def before_search(self, search_params):
        if 'q' in search_params:
            # print(search_params)
            q = search_params['q']
            if h.is_url(q):
                search_params['q'] = f"\"{search_params['q']}\""
                search_params['df'] = "url"
        return search_params
