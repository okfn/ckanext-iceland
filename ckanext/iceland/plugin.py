import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ModernusException(Exception):
    pass


class IcelandPlugin(plugins.SingletonPlugin):
    '''Iceland theme plugin.

    '''
    # Declare that this class implements IConfigurable and IConfigurer.
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def configure(self, config):
        '''Load settings from the config file for this plugin.'''

        # Something
        if 'iceland.modernus.id' not in config:
            msg = 'Missing iceland.modernus.id in configuration file'
            raise ModernusException(msg)
        self.modernus_id = config['iceland.modernus.id']
	if 'iceland.modernus.portion' not in config:
            msg = 'Missing iceland.modernus.portion in configuration file'
            raise ModernusException(msg)
        self.modernus_portion = config['iceland.modernus.portion']
        self.modernus_name = config.get('iceland.modernus.name', '')
            

    def update_config(self, config):

        # Add this plugin's templates dirs to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_template_directory(config, 'modernus/templates')
        
        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'theme/public')
        
        # Register this plugin's fanstatic directory with CKAN.
        # Here, 'fanstatic' is the path to the fanstatic directory
        # (relative to this plugin.py file), and 'example_theme' is the name
        # that we'll use to refer to this fanstatic directory from CKAN
        # templates.
        toolkit.add_resource('theme/resources', 'iceland-theme')


    def render_modernus(self):
        data = {'modernus_id': self.modernus_id,
                'modernus_portion': self.modernus_portion,
                'modernus_name': self.modernus_name}
        return toolkit.render_snippet(
            'modernus/snippets/counter.html',data)

    def get_helpers(self):
        return {'modernus_counter': self.render_modernus}
        
