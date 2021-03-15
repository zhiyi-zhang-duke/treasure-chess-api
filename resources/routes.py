from .rest_apis import GamesApi, GameApi, OpeningsApi, OpeningApi

def initialize_routes(api):
    api.add_resource(GamesApi, '/api/games')
    api.add_resource(GameApi, '/api/game/<id>')
    api.add_resource(OpeningApi, '/api/openings/')
    api.add_resource(OpeningsApi, '/api/openings/<name>')
