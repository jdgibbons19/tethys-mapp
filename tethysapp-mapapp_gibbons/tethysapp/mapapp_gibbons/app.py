from tethys_sdk.base import TethysAppBase, url_map_maker


class MapappGibbons(TethysAppBase):
    """
    Tethys app class for My Map App.
    """

    name = 'My Map App'
    index = 'mapapp_gibbons:home'
    icon = '/mapapp_gibbons/images/map.png'
    package = 'mapapp_gibbons'
    root_url = 'mapapp-gibbons'
    color = '#32992a'
    description = 'A map app with maps that you can map .'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mapapp_gibbons/home',
                controller='mapapp_gibbons.controllers.home'
            ),

            UrlMap(
                name='mapview',
                url='mapapp_gibbons/mapview',
                controller='mapapp_gibbons.controllers.mapview'
            ),

            UrlMap(
                name='data',
                url='mapapp_gibbons/data',
                controller='mapapp_gibbons.controllers.data'
            ),

            UrlMap(
                name='about',
                url='mapapp_gibbons/about',
                controller='mapapp_gibbons.controllers.about'
            ),

            UrlMap(
                name='proposal',
                url='mapapp_gibbons/proposal',
                controller='mapapp_gibbons.controllers.proposal'
            ),

            UrlMap(
                name='mockups',
                url='mapapp_gibbons/mockups',
                controller='mapapp_gibbons.controllers.mockups'
            ),
        )

        return url_maps
