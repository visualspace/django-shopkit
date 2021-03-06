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

import logging
logger = logging.getLogger(__name__)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from shopkit.stock.models import \
    StockedCartItemBase, StockedCartBase, StockedOrderItemBase, \
    StockedOrderBase, StockedItemBase


class StockedCartItemMixin(StockedItemBase, StockedCartItemBase):
    """
    Mixin class for `CartItem`'s containing items for which stock is kept.
    """
    pass


class StockedCartMixin(StockedCartBase):
    """
    Mixin class for `Cart`'s containing items for which stock is kept.
    """
    pass


class StockedOrderItemMixin(StockedItemBase, StockedOrderItemBase):
    """
    Mixin class for `OrderItem`'s containing items for which stock is kept.
    """

    def confirm(self):
        """
        Register lowering of the current item's stock.
        """

        super(StockedOrderItemMixin, self).confirm()

        stocked_item = self.get_stocked_item()

        logger.debug(u'Lowering stock of %d for %s with %d',
                     stocked_item.stock,
                     stocked_item,
                     self.quantity)

        stocked_item.stock -= self.quantity
        stocked_item.save()


class StockedOrderMixin(StockedOrderBase):
    """
    Mixin class for `Order`'s containing items for which stock is kept.
    """
    pass


class StockedItemMixin(models.Model, StockedItemBase):
    """
    Item for which stock is kept in an integer `stock` field.
    """

    class Meta:
        abstract = True

    stock = models.PositiveIntegerField(_('stock'))
    """
    SmallIntegerField storing the amount of items in stock.
    """

    def is_available(self, quantity):
        """
        Method used to determine whether or not the current item is in an
        orderable state.
        """
        logger.debug(u'Checking whether quantity %d of %s is stocked',
                     quantity, self)

        if self.stock >= quantity:
            return True

        return False

