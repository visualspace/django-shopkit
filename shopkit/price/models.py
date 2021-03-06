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

from django.db import models

from django.utils.translation import ugettext_lazy as _

from shopkit.core.basemodels import AbstractPricedItemBase

# Get the currently configured currency field, whatever it is
from shopkit.currency.utils import get_currency_field
PriceField = get_currency_field()


class PricedItemBase(AbstractPricedItemBase):
    """ Abstract base class for priced models with a price field. 
        This base class simply has a price field for storing the price
        of the item.
    """
    
    class Meta:
        abstract = True
    
    price = PriceField(verbose_name=_('price'))
    """ Price for the current product. """

    def get_price(self, **kwargs):
        """ Returns the price property of the current product. """
        return self.price
