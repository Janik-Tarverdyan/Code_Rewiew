# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-

# routes.py
#
# Copyright 2021 Janik Tarverdyan <Janik.Tarverdyan@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from Core import app


def routes():
    routes = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            routes[rule.rule] = rule.endpoint

        routes_kyes = list(routes.keys())
        routes_value = list(routes.values())

        routes_kyes.pop()
        routes_value.pop()

        routes_value.sort()
        routes_kyes.sort()

        routes_kyes.append(routes_kyes.pop(routes_kyes.index('/#contact')))
        routes_value.append(routes_value.pop(routes_value.index('Contact')))

        # All routes
        routes = dict(zip(routes_kyes, routes_value))

        return routes
