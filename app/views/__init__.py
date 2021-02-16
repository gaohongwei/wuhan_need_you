# coding: utf-8

import pkgutil

def register_blueprints(app):
    '''
    Load view sub-modules in current module.
    Assume each sub-module has a Blueprint called app
    '''
    print(__path__)
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        try:
            mod = loader.find_module(module_name).load_module(module_name)
            app.register_blueprint(mod.app)
            app.logger.info('blueprint ' + module_name + ' is loaded')
        except Exception as e:
            print(e)
            app.logger.error('blueprint ' + module_name + ' fails to load')

