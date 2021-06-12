# -*- coding: utf-8 -*-
# -*- coding_Stype: PEP8 -*-

# assets.py
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


from flask_assets import Bundle, Environment
from API.Core import app, Settings
from glob2 import glob as find
from flask_minify import minify


class Site():
    def styles():
        path = Settings.APPLICATION_STATIC+"/site/Master_Mind"
        all_styles = find('%s/**/*.css' % (path))

        for min_items in all_styles:
            if min_items == min_items and 'min.css' in min_items:
                all_styles.remove(min_items)

        for gen in all_styles:
            if 'gen' in gen:
                all_styles.remove(gen)

        return all_styles

    def scripts():
        path = Settings.APPLICATION_STATIC+"/site/Master_Mind"
        all_scripts = find('%s/**/*.js' % (path))

        for min_items in all_scripts:
            if min_items == min_items and 'min.js' in min_items:
                all_scripts.remove(min_items)

        for gen in all_scripts:
            if 'gen' in gen:
                all_scripts.remove(gen)

        return all_scripts


path = {
    "css": Settings.APPLICATION_STATIC + '/site/Master_Mind/css/',
    "js": Settings.APPLICATION_STATIC + '/site/Master_Mind/js/',
    "revolution_css":  Settings.APPLICATION_STATIC +
    '/site/Master_Mind/plugins/revolution/revolution/css/',
    "revolution_js":  Settings.APPLICATION_STATIC +
    '/site/Master_Mind/plugins/revolution/revolution/js/',
    "revolution_addon":  Settings.APPLICATION_STATIC +
    '/site/Master_Mind/plugins/revolution/revolution-addons/',
}


Styles = {
    'Site': [
        path['css'] + "font-awesome.min.css",
        path['css'] + "all.css",
        path['css'] + "preload.min.css",
        path['css'] + "plugins.min.css",
        path['css'] + "style.purple-500.min.css",
        path['css'] + "material-design-iconic-font.min.css",
        path['css'] + "custom.css"
    ],
    'Services': [
        path['revolution_css'] + "settings.css",
        path['revolution_css'] + "layers.css",
        path['revolution_css'] + "navigation.css",
        path['css'] + "preload.min.css",
        path['css'] + "plugins.min.css",
        path['revolution_addon'] +
        "typewriter/js/revolution.addon.typewriter.min.js",
        path['revolution_addon'] + "typewriter/css/typewriter.css",
    ]
}


Script = {
    'Site': [
        path['js'] + "plugins.min.js",
        path['js'] + "app.min.js",
        path['js'] + "index.js",
    ],
    'Services': [
        path['revolution_js'] + "jquery.themepunch.tools.min.js",
        path['revolution_js'] + "jquery.themepunch.revolution.min.js",
        path['js'] + "app.min.js",
        path['js'] + "configurator.min.js",
    ],
}


IE_Script = [
    path['js'] + "html5shiv.min.js",
    path['js'] + "respond.min.js"
]


bundles = {
    'site_js': Bundle(
        # Site.scripts(),
        Script['Site'],
        output='site/Master_Mind/js/site_gen-scripts.min.js',
        filters='jsmin'
    ),

    'IE_Script': Bundle(
        IE_Script,
        output='site/Master_Mind/js/site_gen-ie_scripts.min.js',
        filters='jsmin'
    ),

    'site_css': Bundle(
        # Site.styles(),
        Styles['Site'],
        output='site/Master_Mind/css/site_gen-styles.min.css',
        # filters='cssmin'
    ),

    # 'services_js': Bundle(
    #     Script['Services'],
    #     output='site/Master_Mind/plugins/revolution/revolution/js/services_gen-scripts.min.js',
    #     filters='jsmin'
    # ),
    #
    # 'services_css': Bundle(
    #     Styles['Services'],
    #     output='site/Master_Mind/plugins/revolution/revolution/css/services_gen-styles.min.css',
    #     # filters='cssmin'
    # ),
}

# minify(app=app)

assets = Environment(app)
assets.register(bundles)
