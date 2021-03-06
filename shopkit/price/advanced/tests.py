# Copyright (C) 2010-2011 Mathijs de Bruin <mathijs@mathijsfietst.nl>
#
# This file is part of django-shopkit.
#
# django-shopkit is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from django.conf import settings

from shopkit.core.utils import get_model_from_string


class AdvancedPriceTestMixin(object):
    """
    Base class for testing advanced prices.
    """
    
    def setUp(self):
        """
        This makes the `Price` class from the `SHOPKIT_PRICE_MODEL` available
        as `self.price_class` for unittests to make use of.
        """

        super(AdvancedPriceTestMixin, self).setUp()
        
        self.price_class = \
            get_model_from_string(settings.SHOPKIT_PRICE_MODEL)
