from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

import mock
from nose.tools import eq_, raises

from lib.marketplace.api import client, UnknownPricePoint


sample_price = {
    u'name': u'Tier 0',
    u'pricePoint': '0',
    u'prices': [{u'amount': u'1.00', u'currency': u'USD'},
                {u'amount': u'3.00', u'currency': u'JPY'}],
    u'resource_uri': u'/api/v1/webpay/prices/1/'
}


@mock.patch('lib.marketplace.api.client.api')
class SolitudeAPITest(TestCase):

    def test_get_prices(self, slumber):
        sample = mock.Mock()
        sample.get_object.return_value = sample_price
        slumber.webpay.prices.return_value = sample
        prices = client.get_price(1)
        eq_(prices['name'], sample_price['name'])

    @raises(UnknownPricePoint)
    def test_invalid_price_point(self, slumber):
        slumber.webpay.prices.side_effect = ObjectDoesNotExist
        client.get_price(1)
