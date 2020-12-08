# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

dist_name = __name__
try:
    dist_version = get_distribution(dist_name).version
    release = '.'.join(dist_version.split('.')[:2])

    __version__ = release
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
