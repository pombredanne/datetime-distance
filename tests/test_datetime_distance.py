import math
from unittest import TestCase

import env
from datetime_distance import DateTimeComparator


class DateTimeTests(TestCase):

    def test_datetime_to_datetime_comparison(self):

        dt1 = '2017-05-25'
        dt2 = '2017-01-01'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(144), 0, 0))

        print(distance)
        print(expected)

        assert (distance == expected)

    def test_datetime_to_timestamp_comparison(self):

        dt1 = '2017-05-25'
        dt2 = '2017-01-01 12:30:05'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(143), 0, 0))

        assert (distance == expected)

    def test_timestamp_to_timestamp_comparison(self):

        dt1 = '2017-05-25 21:08:09'
        dt2 = '2017-01-01 12:30:05'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((1, 0, 0, 0, math.sqrt(12472684), 0, 0, 0))

        assert (distance == expected)

    def test_years(self):

        dt1 = '2012'
        dt2 = '2010'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 0, 0, 1, 0, 0, 0, math.sqrt(2)))

        assert (distance == expected)

    def test_months(self):

        dt1 = 'May 2012'
        dt2 = 'June 2013'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 0, 1, 0, 0, 0, math.sqrt(13), 0))

        assert (distance == expected)

    def test_days(self):

        dt1 = '5 May 2013'
        dt2 = '9 June 2013'

        c = DateTimeComparator()
        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(35), 0, 0))

        assert (distance == expected)

    def test_alternate_formats(self):

        c = DateTimeComparator()

        dt1 = 'May 5th, 2013'
        dt2 = '2013-06-09'

        distance1 = c(dt1, dt2)
        expected1 = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(35), 0, 0))

        assert (distance1 == expected1)

        dt3 = '11am May 5th 2013'
        dt4 = 'June 9th 2013'

        distance2 = c(dt3, dt4)
        expected2 = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(34), 0, 0))

        assert (distance2 == expected2)

        dt5 = '5/5/2013'
        dt6 = '6/9/2013'

        distance3 = c(dt5, dt6)
        expected3 = expected1

        assert (distance3 == expected3)

    def test_zero_seconds(self):

        c = DateTimeComparator()

        dt1 = '2017-05-06 12:00:00'
        dt2 = '2017-05-06 12:00:00'

        distance = c(dt1, dt2)
        expected = c._make_tuple((1, 0, 0, 0, 0, 0, 0, 0))

        assert (distance == expected)

    def test_fuzzy_parse(self):

        c = DateTimeComparator()

        dt1 = 'June 6th 2013'
        dt2 = 'It happened on June 7th, 2013'

        distance = c(dt1, dt2)
        expected = c._make_tuple((0, 1, 0, 0, 0, math.sqrt(1), 0, 0))

        assert (distance == expected)
