from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os

from argparse import ArgumentParser
from imp import load_source
from os.path import join

from injector import AssistedBuilder, Injector

from hal import PROJECT_ROOT
from hal.bot import Bot
from hal.modules import ApplicationModule


def main():
    root_logger = logging.getLogger()
    root_logger.addHandler(logging.StreamHandler())
    root_logger.level = logging.DEBUG

    parser = ArgumentParser(description='HAL bot')
    parser.add_argument('--adapter', dest='adapter', default='shell')
    parser.add_argument('--name', dest='name', default='HAL')
    arguments = parser.parse_args()

    injector = Injector([ApplicationModule])
    bot_builder = injector.get(AssistedBuilder(Bot))
    bot = bot_builder.build(name=arguments.name)

    adapter_directory = os.environ.get('HAL_ADAPTER_DIRECTORY', join(PROJECT_ROOT, 'adapters'))
    adapter_module = load_source('adapter', join(adapter_directory,
                                                 '%s.py' % (arguments.adapter,)))
    bot.adapter = adapter_module.Adapter(bot)
    bot.run()
