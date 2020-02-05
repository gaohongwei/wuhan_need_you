# coding: utf-8

from flask import request, current_app

class UserPermission:
    def __init__(self):
        pass
    def allow(self, user):
        return False

class RoutePermission(UserPermission):
    def __init__(self, route, role_name):
        self.route = route
        self.role_name = role_name
    def allow(self, user):
        if user == None:
            return False
        allow_role_name = getattr(user, 'allow_role_name', None)
        return allow_role_name != None and allow_role_name(self.role_name) and self.match_route(self.route)
    @classmethod
    def match_route(cls, route):
        return route == RoutePermission.get_current_route()
    @classmethod
    def get_current_route(cls):
        return request.script_root + request.path

class ModelViewPermission(UserPermission):
    def __init__(self, modelViewClass, role_name):
        self.modelViewClass = modelViewClass
        self.role_name = role_name
    def allow(self, user):
        if user == None:
            return False
        allow_role_name = getattr(user, 'allow_role_name', None)
        return allow_role_name != None and user.allow_role_name(self.role_name)

route_permissions = []
model_view_permissions = {}

def register_route_permission(route, role_name):
    route_permissions.append(RoutePermission(route, role_name))

def register_model_view_permission(modelViewClass, role_name):
    model_view_permissions[modelViewClass] = ModelViewPermission(modelViewClass, role_name)

def check_route_permission(user):
    for permission in route_permissions:
        if permission.allow(user):
            current_app.logger.info('permitted')
            return True
    current_app.logger.info('not permitted')
    return False

def check_model_view_permission(modelView, user):
    if modelView == None or user == None:
        return False
    permission = model_view_permissions.get(modelView.__class__, None)
    if permission == None:
        return False
    return permission.allow(user)

# check permission for both route and model_view
def check_permission(modelView, user):
    return check_route_permission(user) and check_model_view_permission(modelView, user)

