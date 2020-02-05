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
        return user.allow_role_name(self.role_name) and self.match_route(self.route)
    @classmethod
    def match_route(cls, route):
        return route == RoutePermission.get_current_route()
    @classmethod
    def get_current_route(cls):
        return request.script_root + request.path

permissions = []

def register_permission(permission):
    permissions.append(permission)

def check_permission(user):
    for permission in permissions:
        if permission.allow(user):
            current_app.logger.info('permitted')
            return True
    current_app.logger.info('not permitted')
    return False
