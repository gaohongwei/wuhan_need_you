from app.models import Asset

def register_asset_processors(app):
    @app.context_processor
    def inject_asset_processors():
        return {
                '_asset': lambda key: Asset.get_content_by_key(key)
                }
        return True
